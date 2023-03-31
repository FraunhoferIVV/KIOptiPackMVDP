import logging

import numpy as np
import requests as rq
import pandas as pd

from pandas import DataFrame


class DataSpaceUploader:

    def __init__(self, server: str):
        self.server = server
        self.max_post_len = int(1e3)
        self._logger = logging.getLogger('data_space_uploader')

    def set_max_pos_len(self, max_post_len: int):
        if max_post_len < 10:
            self._logger.error("Too small post message length limit. New value not set")
            return
        self.max_post_len = max_post_len

    def upload(self, material_id: str, parameters: DataFrame, values: DataFrame):
        self._upload_dataframe(material_id, DataFrame(parameters))  # make sure all series are dfs
        self._upload_dataframe(material_id, DataFrame(values))

    def _upload_dataframe(self, material_id, dataframe: DataFrame):
        post_url = "http://0.0.0.0:5480/machine_upload"
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
            response = rq.post(url=post_url, data=msg)
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
