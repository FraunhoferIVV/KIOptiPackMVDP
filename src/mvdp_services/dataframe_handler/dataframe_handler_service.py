"""
Application logic for dataframe_handler service
"""

import asyncio
import logging
import pandas as pd
from datetime import datetime
from multiprocessing import Process
import uvicorn


from fastapi import FastAPI, Form, HTTPException
from fastiot.core import FastIoTService
from fastiot.core.time import get_time_now
from fastiot.env import env_basic
from fastiot.msg.thing import Thing
from starlette.middleware.cors import CORSMiddleware

from mvdp.data_space_uploader.constants import DataFrameType
from mvdp_services.dataframe_handler.env import env_dataframe_handler


class DataframeHandlerService(FastIoTService):

    def __init__(self, **kwargs):
        """
        init the service
        :param kwargs: arguments for the FastIoTService
        """
        super().__init__(**kwargs)

        self.app = FastAPI(root_path=env_dataframe_handler.base_path)
        self._register_routes()
        self._uvicorn_proc = Process(target=uvicorn.run,
                                     args=(self.app,),
                                     kwargs={"host": "0.0.0.0", "port": env_dataframe_handler.port,
                                             "log_level": env_basic.log_level},
                                     daemon=True)

        # define a test machine for making things
        self.machine = "TEST_MACHINE"

    def _register_routes(self):
        """
        set up the police and define the methods for fastapi
        """
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["POST"],
            allow_headers=["*"]
        )
        self.app.post("/machine_upload")(self._handle_post)

    async def _start(self):
        """ Methods to start once the module is initialized """
        self._uvicorn_proc.start()
        await asyncio.sleep(0.2)  # time for the server to start

    async def _stop(self):
        """ Methods to call on module shutdown """
        self._uvicorn_proc.terminate()

    async def _handle_post(self, material_id: str = Form(...),
                           start_timestamp: datetime = Form(None),
                           df_type: DataFrameType = Form(...),
                           content: str = Form(...)):
        """
        accepts messages from DataSpaceUploader
        :param material_id: unique identifier for the following uploading
        :param start_timestamp: universal timestamp for parameters if exists
        :param df_type: the type of the dataframe, which is currently being loaded
        :param content: a part of the dataframe to upload
        """
        dataframe = pd.read_json(content).sort_index()
        self._logger.debug(dataframe)
        # upload dataframe considering their type
        if df_type == DataFrameType.values:
            await self._send_values_things(material_id, dataframe)
        if df_type == DataFrameType.parameters:
            await self._send_parameters_things(material_id, dataframe, start_timestamp)
        return "successfully uploaded"

    async def _send_parameters_things(self, material_id, dataframe, start_timestamp: datetime):
        """
        sends a part of the parameters dataframe via message broker
        :param material_id: unique identifier for the uploading
        :param dataframe: parameters dataframe
        :param start_timestamp: timestamp for all parameters
        :return:
        """
        for index, row in dataframe.iterrows():
            row = row.to_dict()  # This will make sure, we have python primitives like int and not np.int64
            # create thing from row
            thing = Thing(machine=self.machine,
                          name=row['Parameter'],
                          measurement_id=material_id,
                          value=row['ParValue'],
                          timestamp=start_timestamp
                          )
            self._logger.debug(thing)
            # no unit support yet
            await self.broker_connection.publish(subject=Thing.get_subject("DataFrameImporter"),
                                                 msg=thing)

    async def _send_values_things(self, material_id, dataframe):
        """
        sends a part of the values dataframe via message broker
        :param material_id: unique identifier for the uploading
        :param dataframe: values dataframe
        """
        # timestamp is obligatory for the values dataframe
        if 'Timestamp' not in dataframe:
            raise HTTPException("Can't save values dataframe without Timestamp column")
        # find the column with content (not timestamp within 2 columns)
        attr = next(col_name for col_name in dataframe if col_name != 'Timestamp')

        for index, row in dataframe.iterrows():
            try:
                row = row.to_dict()   # This will make sure, we have python primitives like int and not np.int64
                timestamp = row['Timestamp'].to_pydatetime()
                # create thing from row
                thing = Thing(machine=self.machine,
                              name=attr,
                              measurement_id=material_id,
                              value=row[attr],
                              timestamp=timestamp
                              )
                self._logger.debug(thing)
            except:
                raise HTTPException("Can't build Thing object from a table cell!")
            # no unit support yet
            await self.broker_connection.publish(subject=Thing.get_subject("DataFrameImporter"),
                                                 msg=thing)


if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG, force=True)
    DataframeHandlerService.main()
