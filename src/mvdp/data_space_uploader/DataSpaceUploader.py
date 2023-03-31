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
        self.server = server  # Todo: Define http://server:port/something? What parts do we want?
        self.max_post_len = int(1e3)
        self._logger = logging.getLogger('data_space_uploader')

    def set_max_pos_len(self, max_post_len: int):
        if max_post_len < 10:
            self._logger.error("Too small post message length limit. New value not set")
            return
        self.max_post_len = max_post_len

    def upload(self, material_id: str, parameters: DataFrame, values: Optional[DataFrame] = None):

        # Todo: Check if sensor does not have same name as any parameter.

        self._upload_dataframe(material_id, DataFrameType.parameters,
                               DataFrame(parameters))  # make sure all series are dfs
        if values:
            self._upload_dataframe(material_id, DataFrameType.values, DataFrame(values))

    def _upload_dataframe(self, material_id, df_type, dataframe: DataFrame):
        post_url = f"http://{self.server}:{env_dataframe_handler.fastapi_port}/machine_upload"  # Todo: Port handling!
        df_columns = DataSpaceUploader._reduce_dataframe(dataframe)
        post_batches = []
        for column in df_columns:
            split_index = len(column) // self.max_post_len + 1
            post_batches += np.array_split(column, split_index)
        for batch in post_batches:
            msg = {
                "material_id": material_id,
                "df_type": df_type,
                "content": batch.to_json()
            }
            self._logger.debug("Message:" + str(msg))
            try:
                response = rq.post(url=post_url, data=msg)
            except Exception as e:
                self._logger.error(e)
                raise Exception("Sending error")
            self._logger.debug("Response:" + response.text)

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
    dsu = DataSpaceUploader("543")
    dsu.set_max_pos_len(20)
    df = pd.read_excel("/home/drobitko/Downloads/Protokoll_MotiV.xlsx")
    dsu.upload("722", df[["Name", "Parameter"]], df["Werte"])
