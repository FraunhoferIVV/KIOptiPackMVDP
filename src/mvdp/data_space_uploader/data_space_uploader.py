import logging
import numpy as np
import requests as rq

from typing import Optional
from datetime import datetime
from pandas import DataFrame

from fastiot.core.time import get_time_now

from mvdp.data_space_uploader.constants import DataFrameType


class DataSpaceUploader:

    def __init__(self, base_url: str,):
        """
        Instantiate data space uploader
        :param base_url: URL to post the data to, maybe something like
        http://service.kioptipack.ivv-dd.fhg.de:5080/my_uploader
        """
        self.post_url = f"{base_url}/machine_upload"
        self.max_post_len = int(1e3)
        self._logger = logging.getLogger('data_space_uploader_logger')
        # add local logger
        self._logger.info("DataSpaceUploader initialized")

    def set_max_pos_len(self, max_post_len: int):
        """
        Set the maximal message length to be posted to the dataframe_handler_service
        :param max_post_len: the message length to be set up
        """
        # don't allow to small messages cause of the overhead
        if max_post_len < 10:
            self._logger.error("Too small post message length limit. New value not set")
            return
        self.max_post_len = max_post_len

    def upload(self, material_id: str, parameters: DataFrame, values: Optional[DataFrame] = None):
        """
        Upload parameters and values dataframes
        """
        # make sure all series (columns) are dfs
        if not isinstance(parameters, DataFrame):
            parameters = DataFrame(parameters)
            self._logger(parameters)
        if values is not None and not isinstance(values, DataFrame):
            values = DataFrame(values)

        # get starting timestamp for parameters
        try:
            start_timestamp = values.head(1).to_dict().get("Timestamp").get(0)
        except Exception:
            self._logger.warning("No start timestamp found: using the current time for parameters")
            start_timestamp = get_time_now()

        # validate values and parameters
        DataSpaceUploader._dataframes_validation(parameters, values)

        # upload dataframes
        self._upload_dataframe(material_id, DataFrameType.parameters, parameters, start_timestamp)
        if values is not None:
            self._upload_dataframe(material_id, DataFrameType.values, values)

    def _upload_dataframe(self, material_id,
                          df_type: DataFrameType,
                          dataframe: DataFrame,
                          start_timestamp: Optional[datetime] = None):
        """
        Upload a certain dataframe type
        :param material_id: uniquer identifier for dataframe uploading
        :param df_type: dataframe type
        :param dataframe: dataframe to upload
        :param start_timestamp: universal timestamp for the dataframe if needed
        """
        # creating dataframe list
        if df_type == DataFrameType.values:
            # build dataframe list with reduced values
            df_list = DataSpaceUploader._reduce_dataframe(dataframe)
        elif df_type == DataFrameType.parameters:
            # send formatted parameters as single dataframe
            df_list = [dataframe]
        else:
            self._logger.error("No dataframe type: nothing to upload")
            return
        # split dataframe list in batches
        post_batches = []
        for column in df_list:
            split_index = len(column) // self.max_post_len + 1
            post_batches += np.array_split(column, split_index)
        # sending batches as messages
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
                raise e
            self._logger.debug("Response:" + response.text)

    @staticmethod
    def _dataframes_validation(parameters: DataFrame, values: DataFrame):
        """
        check if the dataframes can be loaded correctly
        """
        DataSpaceUploader._dataframes_parameters_validation(parameters)
        DataSpaceUploader._dataframes_names_validation(parameters, values)

    @staticmethod
    def _dataframes_parameters_validation(parameters: DataFrame):
        """
        check if parameters are correctly formatted
        """
        par_columns = list(parameters.columns)
        if not (len(par_columns) == 2
                and 'Parameter' in par_columns
                and 'ParValue' in par_columns):
            raise Exception("Parameters are not formatted as expected")

    @staticmethod
    def _dataframes_names_validation(parameters, values):
        """
        Check if sensor does not have the same name as any parameter
        :param: parameters: properly formatted parameters dataframe
        :values: parameters dataframe or None
        """
        if values is not None:
            # create a set of unique parameters
            unique_params = set()
            for index, row in parameters.iterrows():
                unique_params.add(row["Parameter"])
            # check if values column names aren't the same as unique parameters
            # <=> check if the set intersection is empty
            if bool(unique_params & set(values.columns)):
                raise Exception("Values can't have common names with parameters!")

    @staticmethod
    def _reduce_dataframe(dataframe: DataFrame) -> list:
        """
        reduce values dataframe to a bunch of timestamp-column dataframes
        :param dataframe: dataframe to reduce
        :return: list of dataframes with 2 columns:
            1. column: reduced column of the values dataframe
            2. column: corresponding timestamps for each value in the first column
        """
        if 'Timestamp' not in dataframe:
            raise Exception('Impossible to reduce values dataframe without Timestamp column!')
        # create a list of the reduced columns
        columns_dfs = []
        for column in dataframe:
            if column != 'Timestamp':
                columns_dfs.append(DataSpaceUploader._reduce_columns(dataframe[column]))
        # hang timestamp column on each other column (performs left join)
        columns_dfs = [col_df.join(dataframe[['Timestamp']]) for col_df in columns_dfs]
        return columns_dfs

    @staticmethod
    def _reduce_columns(column) -> DataFrame:
        """
        remove all column entries, that are equal to the previous entry
        :param column: column to reduce
        :return: reduced column
        """
        same_value_indices = []
        items = list(column.items())
        for index, row in items[1:]:
            if row == items[index - 1][1]:  # check if the row equals the previous row
                same_value_indices.append(index)
        column = DataFrame(column).drop(same_value_indices)
        return column


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, force=True)
