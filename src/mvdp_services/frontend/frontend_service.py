"""
Application logic for frontend service
"""
import asyncio
import io
import json
import logging
import os
from typing import Optional

import pandas as pd
from fastapi import File, Form, FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastiot.core import FastIoTService, ReplySubject
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from mvdp.msg import HealthCheckRequest, HealthCheckReply, ArbitraryJSONMessage
from mvdp.uvicorn_server import UvicornAsyncServer
from mvdp_services.frontend.api_response_msg import HealthResponse, PossibleFileTypes, PossibleCSVDelimiters, \
    FrontendConfiguration
from mvdp_services.frontend.env import env_frontend
from mvdp_services.frontend.table_handler import TableHandler


class FrontendService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = FastAPI()
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_frontend.port)

    def _register_routes(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.app.get("/api/health_check")(self._health_check)
        self.app.get("/api/frontend_config")(self._send_config)
        self.app.post("/api/upload_data")(self._handle_upload)
        self.app.put("/api/change_data")(self._handle_changes)

        table_editor = TableHandler()
        self.app.get("/api/table/data")(table_editor.return_table)

        self.app.exception_handler(404)(self.redirect_all_requests_to_frontend)
        self.app.mount("/",
                       StaticFiles(directory=os.path.join(os.path.dirname(__file__), "vue", "dist"), html=True),
                       name="static")

    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

    async def redirect_all_requests_to_frontend(self, _: Request, __: HTTPException):
        """ Some special to allow the vue.js adjusted paths to actually show up e.g. on page refresh """
        vue_index_file = os.path.join(os.path.dirname(__file__), "vue", "dist", "index.html")
        if os.path.isfile(vue_index_file):
            return HTMLResponse(open(vue_index_file).read())
        self._logger.warning("Vue.js application has not been build, can’t serve any page, not even error page!")
        return JSONResponse(content={"Error": 404, "Description": "File not found. Vue.js application has not been "
                                                                  "built to serve proper error page."}, status_code=404)

    async def _health_check(self) -> HealthResponse:
        """ Performs a health check against message broker and edc, more maybe to follow."""

        try:
            edc_status = await self.broker_connection.request(subject=ReplySubject(name="data_provider",
                                                                                   msg_cls=HealthCheckRequest,
                                                                                   reply_cls=HealthCheckReply),
                                                              msg=HealthCheckRequest(),
                                                              timeout=3)
            edc_health = True if edc_status.edc_health else False  # May provide None => Adjust to False
        except asyncio.exceptions.TimeoutError:
            edc_health = False

        response = HealthResponse(broker=self.broker_connection.is_connected,
                                  edc=edc_health,
                                  overall_status=self.broker_connection.is_connected and edc_health)
        return response

    @staticmethod
    async def _send_config() -> FrontendConfiguration:
        """ Returns some configurations to set up the frontend """
        return FrontendConfiguration(title=env_frontend.frontend_title)

    async def _handle_upload(self, data_file: bytes = File(),
                             file_type: PossibleFileTypes = Form(...),
                             data_delimiter: Optional[PossibleCSVDelimiters] = Form(None),
                             decimal_delimiter: Optional[PossibleCSVDelimiters] = Form(None),
                             material_id: Optional[str] = Form(None)):
        """
        Endpoint to upload files formed as table (Excel .xlsx-files or comma separated values .csv) or plain JSON.
        If CSV is used decimal and data delimiter must be set.
        """
        data_frame = await self._parse_file(data_file=data_file, file_type=file_type,
                                            data_delimiter=data_delimiter, decimal_delimiter=decimal_delimiter, )
        if data_frame is not None:
            timestamp_in_table = 'Timestamp' in data_frame
            self._data_frame_validation(data_frame, material_id, timestamp_in_table)
            await self._data_frame_send_things(data_frame, material_id, timestamp_in_table)
        return "File successfully uploaded"

    async def _handle_changes(self, changed_items: str = Form(...)):
        changes = json.loads(changed_items)
        self._logger.debug(changes)
        for row in changes:
            pass

    async def _parse_file(self, data_file, data_delimiter: PossibleCSVDelimiters,
                          decimal_delimiter: PossibleCSVDelimiters, file_type) -> Optional[pd.DataFrame]:
        file_type = file_type.lower()
        file_type = file_type if not file_type.startswith('.') else file_type[1:]
        try:
            if file_type == PossibleFileTypes.csv:
                data_frame = pd.read_csv(io.StringIO(data_file.decode('utf-8')),
                                         delimiter=data_delimiter.to_raw(), decimal=decimal_delimiter.to_raw())
            elif file_type == PossibleFileTypes.xlsx:
                data_frame = pd.read_excel(data_file)
            elif file_type == PossibleFileTypes.json:
                await self._send_json_message(data_file)
                data_frame = None
            else:
                raise HTTPException(status_code=500, detail=f'Unknown extension {file_type}.')
        except:
            raise HTTPException(status_code=500, detail='Could not parse the file!')
        return data_frame

    @staticmethod
    def _data_frame_validation(data_frame, material_id, timestamp_in_table):
        if len(data_frame.columns) <= 1:
            raise HTTPException(status_code=500, detail='Potentially wrong configuration!')
        material_id_exists = material_id or "Material_ID" in data_frame
        if not material_id_exists or ("Material_ID" not in data_frame and "Timestamp" not in data_frame):
            raise HTTPException(status_code=500, detail="No Material_ID or no Timestamp!")
        if timestamp_in_table:
            try:
                data_frame.Timestamp = pd.to_datetime(data_frame.Timestamp)
            except (pd.ParseError, ValueError):
                raise HTTPException(status_code=500, detail="Could not parse datetimes")
        return timestamp_in_table

    async def _data_frame_send_things(self, data_frame, material_id, timestamp_in_table):
        attributes = [column for column in data_frame
                      if (column != 'Material_ID' and column != 'Timestamp')]
        # create things from table
        for index, row in data_frame.iterrows():
            row = row.to_dict()  # This will make sure, we have python primitives like int and not np.int64
            row_timestamp = get_time_now()  # the same timestamp for each thing from row
            for attr in attributes:
                measurement_id = material_id or row['Material_ID']

                if timestamp_in_table:
                    timestamp = row['Timestamp'].to_pydatetime()
                else:
                    timestamp = row_timestamp

                # create thing
                thing = Thing(machine=env_frontend.frontend_title,
                              name=attr, measurement_id=measurement_id,
                              value=row[attr], timestamp=timestamp)

                await self.broker_connection.publish(subject=Thing.get_subject("DataImporter"), msg=thing)

    async def _send_json_message(self, data_file):
        """ Transfer a received JSON document to the message broker to be stored by the object storage """
        json_content = json.loads(data_file)
        message = ArbitraryJSONMessage(json_data=json_content)
        await self.broker_connection.publish(subject=ArbitraryJSONMessage.get_subject(),
                                             msg=message)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    FrontendService.main()
