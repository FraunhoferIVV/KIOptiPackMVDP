import logging
from typing import Optional

import numpy as np
import requests as rq
import pandas as pd

from pandas import DataFrame

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
        self._logger = logging.getLogger('data_space_uploader')

    def set_max_pos_len(self, max_post_len: int):
        if max_post_len < 10:
            self._logger.error("Too small post message length limit. New value not set")
            return
        self.max_post_len = max_post_len

    def upload(self, material_id: str, parameters: DataFrame, values: Optional[DataFrame] = None):

        # make sure all series are dfs
        if not isinstance(parameters, DataFrame):
            parameters = DataFrame(parameters)
        if values and not isinstance(values, DataFrame):
            values = DataFrame(values)

        parameters = self._parse_parameters(parameters)
        self._logger.debug(parameters)
        DataSpaceUploader._dataframes_validation(parameters, values)

        self._upload_dataframe(material_id, parameters)
        if values is None:
            self._upload_dataframe(material_id, values)

    def _upload_dataframe(self, material_id, dataframe: DataFrame):
        df_columns = DataSpaceUploader._reduce_dataframe(dataframe)
        post_batches = []
        for column in df_columns:
            split_index = len(column) // self.max_post_len + 1
            post_batches += np.array_split(column, split_index)
        for batch in post_batches:
            msg = {
                "material_id": material_id,
                "content": batch.to_json()
            }
            self._logger.debug("Message:" + str(msg))
            try:
                response = rq.post(url=self.post_url, data=msg)
            except Exception as e:
                self._logger.error(e)
                raise Exception("Sending error!")
            self._logger.debug("Response:" + response.text)

    def _parse_parameters(self, parameters):  # build tree structured parameters
        try:
            # fill missed parameters and save values
            fill_parameters = {
                "Parameter": [],
                "Value": [],
            }
            for index, row in parameters.iterrows():
                fill_param = dict()
                for attr in list(parameters):
                    if attr == 'Value':
                        fill_parameters["Value"].append(row[attr])
                    else:  # not value => part of that tree parameter (str)
                        cell = row[attr]
                        if cell == '-':
                            cell = fill_parameters["Parameter"][-1][attr]
                        fill_param[attr] = cell
                fill_parameters["Parameter"].append(fill_param)
            # unite parameters into tree parameters
            tree_parameters = {
                "Parameter": [],
                "Value": fill_parameters["Value"]
            }
            for param_dict in fill_parameters["Parameter"]:
                tree_param = ""
                for attr in list(parameters):
                    if attr != 'Value':
                        tree_param += "::" + param_dict.get(attr, "")

                tree_parameters["Parameter"].append(tree_param)
            return DataFrame.from_dict(tree_parameters)
        except Exception as e:
            self._logger.error(e)
            raise Exception("Couldn't parse the parameters dataframe")

    @staticmethod
    def _dataframes_validation(parameters, values):
        # Check if sensor does not have same name as any parameter
        if values:
            unique_params = set(parameters.columns)
            for index, row in parameters.iterrows():
                for attr in list(parameters):
                    unique_params.add(row[attr])
            if bool(unique_params & set(values.columns)):
                raise Exception("Values can't have common names with parameters!")

    @staticmethod
    def _reduce_dataframe(dataframe: DataFrame):
        columns_dfs = [DataSpaceUploader._reduce_columns(dataframe[col]) for col in dataframe]
        return columns_dfs

    @staticmethod
    def _reduce_columns(column):
        same_value_indices = []
        items = list(column.items())
        for index, row in items[1:]:
            if row == items[index - 1][1]:  # check if the row equals the previous row
                same_value_indices.append(index)
        column = DataFrame(column).drop(same_value_indices)
        return column


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    dsu = DataSpaceUploader("localhost")
    dsu.set_max_pos_len(20)
    df = pd.read_excel("/home/drobitko/Downloads/Protokoll_MotiV.xlsx")
    df = df.rename(columns={"Werte": "Value"})
    dsu.upload("722", df[["Name", "Parameter", "Value"]])
