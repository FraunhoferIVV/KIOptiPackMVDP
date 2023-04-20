import asyncio
import os
import unittest
from datetime import datetime
import pandas as pd
from pandas import DataFrame

from fastiot.core.broker_connection import NatsBrokerConnection
from fastiot.testlib import populate_test_env
from fastiot.util.ports import get_local_random_port
from fastiot.db.mongodb_helper_fn import get_mongodb_client_from_env
from fastiot.env import env_mongodb
from fastiot.msg.thing import Thing
from unittest.mock import patch



from mvdp.data_space_uploader.DataSpaceUploader import DataSpaceUploader
from mvdp_services.dataframe_handler.dataframe_handler_service import DataframeHandlerService
from mvdp_services.dataframe_handler.env import MVDP_DATAFRAME_HANDLER_PORT


class TestDataSpaceUploader(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        populate_test_env()
        self.broker_connection = await NatsBrokerConnection.connect()

        # os.environ[MVDP_DATAFRAME_HANDLER_PORT] = str(get_local_random_port())
        os.environ[MVDP_DATAFRAME_HANDLER_PORT] = '5480'

        db_client = get_mongodb_client_from_env()
        database = db_client.get_database(env_mongodb.name)
        self._db_col = database.get_collection('thing')
        self._db_col.delete_many({})

    async def asyncTearDown(self):
        self.broker_connection.close()

    async def test_upload_empty(self):
        # async with DataframeHandlerService(broker_connection=self.broker_connection) as _:
        self._db_col.delete_many({})
        uploader = DataSpaceUploader(server='localhost',
                                     port=int(os.environ[MVDP_DATAFRAME_HANDLER_PORT]))
        df = DataFrame({
            'ExperimentName': ['exp1', '-', 'exp2'],
            'Parameter': ['param1', 'param2', 'param2'],
            'Value': [False, 42, 42.5]
        })
        # upload empty parameters
        uploader.upload('experiment323', DataFrame())
        await asyncio.sleep(0.05)
        results = list(self._db_col.find({}))
        self.assertEqual(0, len(results))
        # upload both parameters and value empty
        await asyncio.sleep(0.05)
        self.assertRaises(Exception,
                          uploader.upload,
                          'experiment324',
                          DataFrame(),
                          DataFrame())
        results = list(self._db_col.find({}))
        self.assertEqual(0, len(results))

    async def test_upload_only_parameters(self):
        # async with DataframeHandlerService(broker_connection=self.broker_connection) as _:
        self._db_col.delete_many({})
        uploader = DataSpaceUploader(server='localhost',
                                     port=int(os.environ[MVDP_DATAFRAME_HANDLER_PORT]))
        df = DataFrame({
            'ExperimentName': ['exp1', '-', 'exp2'],
            'Parameter': ['param1', 'param2', 'param2'],
            'Value': [False, 42, 42.5]
        })
        uploader.upload('experiment323', df)
        await asyncio.sleep(0.05)
        results = list(self._db_col.find({}))
        self.assertEqual(3, len(results))

    async def test_upload_integration(self):
        # async with DataframeHandlerService(broker_connection=self.broker_connection) as _:
        self._db_col.delete_many({})
        uploader = DataSpaceUploader(server='localhost',
                                     port=int(os.environ[MVDP_DATAFRAME_HANDLER_PORT]))
        parameters_df = DataFrame({
            'ExperimentName': ['exp1', '-', 'exp2'],
            'Parameter': ['param1', 'param2', 'param2'],
            'Value': [False, 42, 42.5]
        })
        values_df = DataFrame({
            'Timestamp': [
                datetime(year=2023, month=4, day=13, microsecond=1000),
                datetime(year=2023, month=4, day=13, microsecond=2000)
            ],
            'Sensor_1': [3, 7],
            'Sensor_2': [0.2, 'undefined']
        })
        uploader.upload('experiment728', parameters_df, values_df)
        await asyncio.sleep(0.05)
        results = list(self._db_col.find({}))
        self.assertEqual(7, len(results))
        thing_parts = [{
            'name': '::exp1::param2',
            'value': 42
        }, {
            'timestamp': datetime(2023, 4, 13, 0, 0, 0, 2000),
            'name': 'Sensor_1',
            'value': 7
        }]
        for thing_part in thing_parts:
            found = False
            for result in results:
                if thing_part.items() <= result.items():
                    found = True
                    break
            self.assertTrue(found)

    async def test_unit_parameter_parsing(self):
        parameters_df = DataFrame({
            'ExperimentName': ['exp1', '-', 'exp2'],
            'Parameter': ['param1', 'param2', 'param2'],
            'Value': [False, 42, 42.5]
        })
        parsed_parameters = DataFrame({
            'Parameter': ['::exp1::param1',
                          '::exp1::param2',
                          '::exp2::param2'],
            'ParValue': [False, 42, 42.5]
        })
        result_1 = DataSpaceUploader.parse_parameters(parameters_df)
        self.assertTrue(parsed_parameters.equals(result_1))
        result_2 = DataSpaceUploader.parse_parameters(result_1)  # preparsed
        self.assertTrue(parsed_parameters.equals(result_2))

    async def test_unit_validation(self):
        parsed_parameters = DataFrame({
            'Parameter': ['::exp1::param1',
                          '::exp1::param2',
                          '::exp2::param2'],
            'ParValue': [False, 42, 42.5]
        })
        correct_values = DataFrame({
            'Timestamp': [
                datetime(year=2023, month=4, day=13, microsecond=1000),
                datetime(year=2023, month=4, day=13, microsecond=2000)
            ],
            'Sensor_1': [3, 7],
            'Sensor_2': [0.2, 'undefined'],
            'Parameter': [1, 2]
        })
        wrong_values = DataFrame({
            'Timestamp': [
                datetime(year=2023, month=4, day=13, microsecond=1000),
                datetime(year=2023, month=4, day=13, microsecond=2000)
            ],
            '::exp1::param2': [16, 2],
            'Sensor_1': [3, 7],
            'Sensor_2': [0.2, 'undefined']
        })
        DataSpaceUploader._dataframes_validation(parsed_parameters, None)
        DataSpaceUploader._dataframes_validation(parsed_parameters, correct_values)
        self.assertRaises(Exception,
                          DataSpaceUploader._dataframes_validation,
                          parsed_parameters,
                          wrong_values)

    async def test_unit_reduce_dataframe(self):
        values_df = DataFrame({
            'Timestamp': [
                datetime(year=2023, month=4, day=13, microsecond=1000),
                datetime(year=2023, month=4, day=13, microsecond=2000),
                datetime(year=2023, month=4, day=13, microsecond=3000),
                datetime(year=2023, month=4, day=13, microsecond=4000)
            ],
            'Sensor_1': [7, 7, 8, 8],
            'Sensor_2': [0.2, 'undefined', 'undefined', 'undefined']
        })
        columns_dfs = [
            DataFrame({
                'Sensor_1': [7, 8],
                'Timestamp': [
                    datetime(year=2023, month=4, day=13, microsecond=1000),
                    datetime(year=2023, month=4, day=13, microsecond=3000)
                ]
            }, index=[0, 2]),
            DataFrame({
                'Sensor_2': [0.2, 'undefined'],
                'Timestamp': [
                    datetime(year=2023, month=4, day=13, microsecond=1000),
                    datetime(year=2023, month=4, day=13, microsecond=2000)
                ]
            }, index=[0, 1])
        ]
        result = DataSpaceUploader._reduce_dataframe(values_df)
        for col_df, res_col_df in zip(columns_dfs, result):
            self.assertTrue(col_df.equals(res_col_df))




if __name__ == '__main__':
    unittest.main()
