import logging

from typing import Optional
from datetime import datetime

import numpy as np
import requests as rq
import pandas as pd
import setuptools

from pandas import DataFrame
from fastiot.core.time import get_time_now

from mvdp.data_space_uploader.constants import DataFrameType
from mvdp_services.dataframe_handler.env import env_dataframe_handler


class DataSpaceUploader:

    def __init__(self, server: str):
        """
        Instantiate data space uploader
        :param server:
        """
        self.post_url = f"http://{server}:{env_dataframe_handler.fastapi_port}/machine_upload"
        self.max_post_len = int(1e3)
        self._logger = logging.getLogger('data_space_uploader_logger')

        self._logger.info("DataSpaceUploader initialized")

    def set_max_pos_len(self, max_post_len: int):
        if max_post_len < 10:
            self._logger.error("Too small post message length limit. New value not set")
            return
        self.max_post_len = max_post_len

    def upload(self, material_id: str, parameters: DataFrame, values: Optional[DataFrame] = None):

        # make sure all series (columns) are dfs
        if not isinstance(parameters, DataFrame):
            parameters = DataFrame(parameters)
        if values is not None and not isinstance(values, DataFrame):
            values = DataFrame(values)

        # get starting timestamp for parameters
        try:
            start_timestamp = values.head(1).to_dict().get("Timestamp").get(0)
        except:
            self._logger.info("No start timestamp found: using the current time for parameters")
            start_timestamp = get_time_now()

        # parse parameters
        parameters = DataSpaceUploader.parse_parameters(parameters, self._logger)
        self._logger.debug(parameters)

        # validate values and parsed parameters
        DataSpaceUploader._dataframes_validation(parameters, values)

        self._upload_dataframe(material_id, DataFrameType.parameters, parameters, start_timestamp)
        if values is not None:
            self._upload_dataframe(material_id, DataFrameType.values, values)

    def _upload_dataframe(self, material_id,
                          df_type: DataFrameType,
                          dataframe: DataFrame,
                          start_timestamp: Optional[datetime] = None):
        # creating dataframe list
        if df_type == DataFrameType.values:  # list of dataframe columns as dataframes
            df_list = DataSpaceUploader._reduce_dataframe(dataframe)
        elif df_type == DataFrameType.parameters:  # single dataframe of 2 columns
            df_list = [dataframe]
        else:
            self._logger.warning("No dataframe type: uploading nothing")
        # parsing dataframe list in batches
        post_batches = []
        for column in df_list:
            split_index = len(column) // self.max_post_len + 1
            post_batches += np.array_split(column, split_index)
        # sending batches vie message broker
        for batch in post_batches:
            # create message
            msg = {
                "material_id": material_id,
                "df_type": df_type,
                "content": batch.to_json()
            }
            if start_timestamp:
                msg["start_timestamp"] = start_timestamp
            self._logger.debug("Message:" + str(msg))
            # send message
            try:
                response = rq.post(url=self.post_url, data=msg)
            except Exception as e:
                self._logger.error(e)
                raise Exception("Sending error!")
            self._logger.debug("Response:" + response.text)

    @staticmethod
    def parse_parameters(parameters,
                         logger: logging.Logger = logging.getLogger("parameters_parsing_logger")):  # build tree structured parameters
        try:
            # fill missed parameters and save values
            fill_parameters = {
                "Parameter": [],
                "ParValue": [],
            }
            for index, row in parameters.iterrows():
                fill_param = dict()
                for attr in list(parameters):
                    if attr == 'Value':
                        fill_parameters["ParValue"].append(row[attr])
                    else:  # not value => part of that tree parameter (str)
                        cell = row[attr]
                        if cell == '-':
                            cell = fill_parameters["Parameter"][-1][attr]
                        fill_param[attr] = cell
                fill_parameters["Parameter"].append(fill_param)
            # unite parameters into tree parameters
            tree_parameters = {
                "Parameter": [],
                "ParValue": fill_parameters["ParValue"]
            }
            for param_dict in fill_parameters["Parameter"]:
                tree_param = ""
                for attr in list(parameters):
                    if attr != 'Value':
                        tree_param += "::" + param_dict.get(attr, "")

                tree_parameters["Parameter"].append(tree_param)
            return DataFrame.from_dict(tree_parameters)
        except Exception as e:
            logger.error(e)
            raise Exception("Couldn't parse the parameters dataframe")

    @staticmethod
    def _dataframes_validation(parameters, values):
        # Check if sensor does not have same name as any parameter
        if values is not None:
            unique_params = set(parameters.columns)
            for index, row in parameters.iterrows():
                unique_params.add(row["Parameter"])
            if bool(unique_params & set(values.columns)):
                raise Exception("Values can't have common names with parameters!")

    @staticmethod
    def _reduce_dataframe(dataframe: DataFrame) -> list:
        columns_dfs = [DataSpaceUploader._reduce_columns(dataframe[col]) for col in dataframe]
        return columns_dfs

    @staticmethod
    def _reduce_columns(column) -> DataFrame:
        same_value_indices = []
        items = list(column.items())
        for index, row in items[1:]:
            if row == items[index - 1][1]:  # check if the row equals the previous row
                same_value_indices.append(index)
        column = DataFrame(column).drop(same_value_indices)
        return column


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, force=True)
    dsu = DataSpaceUploader("0.0.0.0")
    dsu.set_max_pos_len(20)
    df = pd.read_excel("/home/drobitko/Downloads/Protokoll_MotiV.xlsx")
    df = df.rename(columns={"Werte": "Value"})
    df1 = DataFrame({'Timestamp': [get_time_now(), 42],
                    'Sensor1': [42, 36]})
    df1 = df1.rename(columns={0: 'Timestamp'})
    dsu.upload("722", df[["Name", "Parameter", "Value"]], df1)
    # dsu.upload("733", DataFrame(), df[["Value"]])
