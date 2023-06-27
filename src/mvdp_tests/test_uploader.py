import os
import time
import unittest
from datetime import datetime

from fastiot.cli.env import env_cli
from fastiot.core.broker_connection import NatsBrokerConnection
from fastiot.db.mongodb_helper_fn import get_mongodb_client_from_env
from fastiot.env import env_mongodb
from fastiot.testlib import populate_test_env, BackgroundProcess
from fastiot.util.ports import get_local_random_port
from pandas import DataFrame

from mvdp.data_space_uploader.data_space_uploader import DataSpaceUploader
from mvdp.tools.dataframe_formatting import reformat_parameters
from mvdp_services.dataframe_handler.dataframe_handler_service import DataframeHandlerService
from mvdp_services.dataframe_handler.env import MVDP_DATAFRAME_HANDLER_PORT


class TestDataSpaceUploader(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        populate_test_env()
        self.broker_connection = await NatsBrokerConnection.connect()

        if env_cli.is_ci_runner or not os.environ.get(MVDP_DATAFRAME_HANDLER_PORT):
            os.environ[MVDP_DATAFRAME_HANDLER_PORT] = str(get_local_random_port())

        db_client = get_mongodb_client_from_env()
        database = db_client.get_database(env_mongodb.name)
        self._db_col = database.get_collection('thing')
        self._db_col.delete_many({})

    async def asyncTearDown(self):
        self._db_col.delete_many({})
        await self.broker_connection.close()

    async def test_upload_empty(self):
        with BackgroundProcess(DataframeHandlerService, startup_time=1.5):

            uploader = DataSpaceUploader(base_url=f'http://localhost:{os.environ[MVDP_DATAFRAME_HANDLER_PORT]}')
            df = DataFrame({
                'ExperimentName': ['exp1', '-', 'exp2'],
                'Parameter': ['param1', 'param2', 'param2'],
                'Value': [False, 42, 42.5]
            })
            # upload empty parameters
            self.assertRaises(Exception,
                              uploader.upload,
                              'experiment324',
                              DataFrame())
            # upload both parameters and value empty
            time.sleep(0.05)
            self.assertRaises(Exception,
                              uploader.upload,
                              'experiment324',
                              DataFrame(),
                              DataFrame())
            results = list(self._db_col.find({}))
            self.assertEqual(0, len(results))

    def test_upload_only_parameters(self):
        with BackgroundProcess(DataframeHandlerService, startup_time=1.5):
            uploader = DataSpaceUploader(base_url=f'http://localhost:{os.environ[MVDP_DATAFRAME_HANDLER_PORT]}')

            parameters = DataFrame({
                'ExperimentName': ['exp1', '-', 'exp2'],
                'Parameter': ['param1', 'param2', 'param2'],
                'Value': [False, 42, 42.5]
            })

            uploader.upload('experiment323', reformat_parameters(parameters, 'Value'))
            time.sleep(0.3)

            results = list(self._db_col.find({}))
            self.assertEqual(3, len(results))

    async def test_upload_integration(self):
        with BackgroundProcess(DataframeHandlerService, startup_time=1.5):
            uploader = DataSpaceUploader(base_url=f'http://localhost:{os.environ[MVDP_DATAFRAME_HANDLER_PORT]}')

            parameters_df = DataFrame({
                'ExperimentName': ['exp1', '-', 'exp2'],
                'Parameter': ['param1', 'param2', 'param2'],
                'Value': [False, 42, 42.5]
            })
            values_df = DataFrame({
                'Timestamp': [
                    datetime(year=2023, month=4, day=13, microsecond=1000),
                    datetime(year=2023, month=4, day=13, microsecond=2000),
                    datetime(year=2023, month=4, day=13, microsecond=3000)
                ],
                'Sensor_1': [3, 7, 7],
                'Sensor_2': [0.2, 'undefined', 2]
            })
            uploader.upload('experiment728', reformat_parameters(parameters_df, 'Value'), values_df)
            time.sleep(2)

            results = list(self._db_col.find({}))
            self.assertEqual(8, len(results))
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

    async def test_unit_parameter_formatting(self):
        parameters_df = DataFrame({
            'ExperimentName': ['exp1', '-', 'exp2'],
            'Parameter': ['param1', 'param2', 'param2'],
            'Value': [False, 42, 42.5]
        })
        formatted_parameters = DataFrame({
            'Parameter': ['::exp1::param1',
                          '::exp1::param2',
                          '::exp2::param2'],
            'ParValue': [False, 42, 42.5]
        })
        result_1 = reformat_parameters(parameters_df, 'Value')
        self.assertTrue(formatted_parameters.equals(result_1))
        result_2 = reformat_parameters(result_1, 'Value')  # result_ 1 has already been formatted
        self.assertTrue(formatted_parameters.equals(result_2))

    async def test_unit_validation(self):
        # test correct
        formatted_parameters = DataFrame({
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
        DataSpaceUploader._dataframes_validation(formatted_parameters, None)

        # test wrong values
        wrong_values = DataFrame({
            'Timestamp': [
                datetime(year=2023, month=4, day=13, microsecond=1000),
                datetime(year=2023, month=4, day=13, microsecond=2000)
            ],
            '::exp1::param2': [16, 2],
            'Sensor_1': [3, 7],
            'Sensor_2': [0.2, 'undefined']
        })
        self.assertRaises(Exception,
                          DataSpaceUploader._dataframes_validation,
                          formatted_parameters,
                          wrong_values)

        # test wrong parameters formatting
        wrong_parameters = DataFrame({
            'Parameter': ['::exp1::param1',
                          '::exp1::param2',
                          '::exp2::param2'],
            'ParValueX': [False, 42, 42.5]
        })
        self.assertRaises(Exception,
                          DataSpaceUploader._dataframes_validation,
                          wrong_parameters,
                          correct_values)

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
