import logging
import json

import numpy as np
import requests as rq
import pandas as pd
from pandas import DataFrame


class DataSpaceUploader:

    def __init__(self, server: str):
        self._logger = logging.getLogger('data_space_uploader')
        self.server = server
        self.max_post_len = int(1e4)

    def set_max_pos_len(self, max_post_len: int):
        if max_post_len < 10:
            self._logger.error("Too small maximal post message length. New value not set")
            return
        self.max_post_len = max_post_len

    def upload(self, material_id: str, parameters: DataFrame, values: DataFrame):
        post_url = "http://0.0.0.0:5480"
        # parameters df to message batches
        # parameters = self._build_dataframe_differnces(parameters)
        parameters_batches = np.array_split(parameters, len(parameters) / self.max_post_len + 1)
        # values df to message batches
        # values = self._build_dataframe_differnces(values)
        values_batches = np.array_split(values, len(values) / self.max_post_len + 1)
        # all message batches
        post_batches = parameters_batches + values_batches  # list of dataframes
        for batch in post_batches:
            msg = {
                "material_id": material_id,
                "content": batch.to_json()
            }
            # rq.post(post_url, msg)


    """
    def upload(self, material_id: str, parameters: DataFrame, values: DataFrame):
        post_url = "http://0.0.0.0:5480"
        post_object = self._create_post_object(material_id, parameters, values)
        try:
            response = rq.post(post_url, post_object)
        except Exception as e:
            self._logger.error(e)
            raise Exception("Sending error")
        self._logger.debug(response)
        return response

    def _create_post_object(self, material_id: str, parameters: DataFrame, values: DataFrame):
        return {
            "config": {
                "server": self.server
            },
            "parameters": parameters.to_json(),
            "values": values.to_json()
        }
    """


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    dsu = DataSpaceUploader("543")
    dsu.set_max_pos_len(10)
    df = pd.read_excel("/home/drobitko/Downloads/Protokoll_MotiV.xlsx")
    res = dsu.upload("722", df["Name"], df[["Parameter", "Werte"]])
    print(res)
