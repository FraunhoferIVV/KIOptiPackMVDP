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
from fastapi import FastAPI, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastiot.core import FastIoTService, ReplySubject
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse

from mvdp.msg import HealthCheckRequest, HealthCheckReply, ArbitraryJSONMessage
from mvdp.uvicorn_server import UvicornAsyncServer
from mvdp_services.frontend.api_response_msg import HealthResponse
from mvdp_services.frontend.env import env_frontend
from mvdp_services.frontend.table_handler import TableHandler


class FrontendService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = FastAPI()
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_frontend.port)

        # define machine for this frontend service
        self.machine = "TEST_MACHINE"

    def _register_routes(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.app.get("/api/health_check")(self._health_check)
        self.app.get("/api/frontend_title")(self._send_title)
        self.app.post("/api/upload_data")(self._handle_upload)

        table_editor = TableHandler()
        self.app.get("/api/table/data")(table_editor.return_table)

        try:
            self.app.mount("/",
                           StaticFiles(directory=os.path.join(os.path.dirname(__file__), "vue", "dist"),
                                       html=True),
                           name="static")

            self.app.exception_handler(404)(self.redirect_all_requests_to_frontend)

        except RuntimeError:
            pass

    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

    async def redirect_all_requests_to_frontend(self, _: Request, __: HTTPException):
        vue_index_file = os.path.join(os.path.dirname(__file__), "vue", "dist", "index.html")
        if os.path.isfile(vue_index_file):
            return HTMLResponse(open(vue_index_file).read())
        self._logger.warning("Vue.js application has not been build, can’t serve any page, not even error page!")
        return JSONResponse(content={"Error": 404, "Description": "File not found. Vue.js application has not been "
                                                                  "built to serve proper error page."})

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
    async def _send_title():
        """ Returns the title for the frontend configured via the env var ``MVDP_FRONTEND_TITLE`` on server side. """
        return {'title': env_frontend.frontend_title}

    async def _handle_upload(self, data_file: bytes = File(),
                             file_type: str = Form(...),
                             data_delimiter: str = Form(...),
                             decimal_delimiter: str = Form(...),
                             material_id: Optional[str] = Form(None)):

        data_frame = await self._parse_file(data_delimiter, data_file, decimal_delimiter, file_type)
        if data_frame:
            timestamp_in_table = 'Timestamp' in data_frame
            self._data_frame_validation(data_frame, material_id, timestamp_in_table)
            await self._data_frame_send_things(data_frame, material_id, timestamp_in_table)
        return "File successfully uploaded"

    async def _parse_file(self, data_delimiter, data_file, decimal_delimiter, file_type) -> Optional[pd.DataFrame]:
        file_type = file_type.lower()
        try:
            if file_type == '.csv':
                decimal_delimiter = ',' if decimal_delimiter == 'comma' else '.'
                data_delimiters = {'comma': ',', 'semicolon': ';'}
                data_frame = pd.read_csv(io.StringIO(data_file.decode('utf-8')),
                                         delimiter=data_delimiters.get(data_delimiter, ","),
                                         decimal=decimal_delimiter)
            elif file_type == '.xlsx':
                data_frame = pd.read_excel(data_file)
            elif file_type == '.json':
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
                thing = Thing(machine=self.machine,
                              name=attr,
                              measurement_id=measurement_id,
                              value=row[attr],
                              timestamp=timestamp)
                # get unit after parsing the value in thing

                await self.broker_connection.publish(subject=Thing.get_subject("DataImporter"),
                                                     msg=thing)

    async def _send_json_message(self, data_file):
        json_content = json.loads(data_file)
        message = ArbitraryJSONMessage(json_data=json_content)
        await self.broker_connection.publish(subject=ArbitraryJSONMessage.get_subject(),
                                             msg=message)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    FrontendService.main()
