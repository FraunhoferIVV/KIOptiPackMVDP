"""
Application logic for data_provider service
"""
import asyncio
import logging
import time
import uuid
from typing import List

import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from fastiot.core import FastIoTService
from fastiot.db.mongodb_helper_fn import get_mongodb_client_from_env
from fastiot.env import env_mongodb
from fastiot.msg.custom_db_data_type_conversion import from_mongo_data
from fastiot.util.read_yaml import read_config
from starlette.middleware.cors import CORSMiddleware

from mvdp.uvicorn_server import UvicornAsyncServer
from mvdp_services.data_provider.env import env_data_provider
from mvdp.edc_management_client.api import ApplicationObservabilityApi, AssetApi
from mvdp.edc_management_client.api_client import ApiClient
from mvdp.edc_management_client.configuration import Configuration
from mvdp.edc_management_client.models import AssetCreationRequestDto, AssetEntryDto, DataAddress
from mvdp.env import mvdp_env


class DataProviderService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init database
        self.mongo_db_client = get_mongodb_client_from_env()
        database = self.mongo_db_client.get_database(env_mongodb.name)
        # potentially load asset from the database (db queries: Asset_x -> [column1, column2, ...])
        # read configuration
        service_config = read_config(self)
        if not service_config:
            self._logger.error('Please set the config as shown in the documentation! Aborting service!')
            time.sleep(10)
            raise RuntimeError
        self.mongodb_col = database.get_collection(service_config['collection'])
        self._parse_config(service_config)

        # init FastAPI and server
        self.app = FastAPI()
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_data_provider.fastapi_port)

        # init edc
        config = Configuration()
        config.host = f"http://{mvdp_env.edc_host}:{mvdp_env.edc_port_2}/api/v1/management"
        config.verify_ssl = False
        config.debug = True
        config.api_key = {'X-Api-Key': 'ApiKeyDefaultValue'}

        self.api_client = ApiClient(config, header_name='X-Api-Key', header_value='ApiKeyDefaultValue')

        self._edc_put_assets()

        # additional
        self.message_received = asyncio.Event()
        self.last_msg = None

    def _register_routes(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['GET'],
            allow_headers=["*"],
        )
        self.app.get("/assets/{asset_name}")(self._handle_get)
        # no mounting apps

    def _parse_config(self, config):
        self.assets = {}
        if 'assets' not in config.keys():
            return
        for asset in config['assets']:
            asset_name = list(asset.keys())[0]
            asset_content = asset[asset_name]
            self.assets[asset_name] = {}
            for asset_attr, asset_attr_content in asset_content.items():
                if asset_attr == 'constraints':
                    self.assets[asset_name]['constraints'] = (
                        DataProviderService._calculate_constraints(asset_attr_content)
                    )
                else:
                    self.assets[asset_name][asset_attr] = asset_attr_content

    @staticmethod
    def _calculate_constraints(constraints_object):
        constraints = {}
        for constraint_attr, constraint_content in constraints_object.items():
            constraints[constraint_attr] = (
                DataProviderService._calculate_single_constraint(constraint_attr, constraint_content)
            )
        return constraints

    @staticmethod
    def _calculate_single_constraint(attribute: str, constraint_values : list):
        if not constraint_values:
            return None
        constraint = {
            'intervals': [],
            'values': []
        }
        if attribute == 'timestamp':  # include special datetime conversion
            for item in constraint_values:
                if isinstance(item, dict) and 'interval' in item.keys():
                    constraint['intervals'].append((pd.Timestamp(item['interval']['start']).to_pydatetime(),
                                                    pd.Timestamp(item['interval']['end']).to_pydatetime()))
                else:
                    constraint['values'].append(pd.Timestamp(item).to_pydatetime())
        else:
            for item in constraint_values:
                if isinstance(item, dict) and 'interval' in item.keys():
                    constraint['intervals'].append((item['interval']['start'],
                                                    item['interval']['end']))
                else:
                    constraint['values'].append(item)
        return constraint

    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

    def _handle_get(self, asset_name: str,
                    material_id: list = Query([]),
                    timestamp: list = Query([]),
                    columns: list = Query([]),
                    value: list = Query([]),
                    unit: list = Query([]),
                    machine: list = Query([])):
        if asset_name not in list(self.assets.keys()):
            raise HTTPException(status_code=500, detail='Asset not configured!')
        # TODO: enable one bounded range constraints + certain time ago
        # TODO: enable url interval queries
        # create custom_query
        custom_constraint_object = {
            'machine': machine,
            'measurement_id': material_id,
            'timestamp': timestamp,
            'name': columns,
            'value': value,
            'unit': unit
        }
        custom_constraints = DataProviderService._calculate_constraints(custom_constraint_object)
        custom_query = DataProviderService._build_query(custom_constraints)
        # create asset_query
        asset_constraints = self.assets[asset_name].get('constraints', {})
        asset_query = self._build_query(asset_constraints)
        # create data_query (query intersection)
        if custom_query or asset_query:
            data_query = {"$and": [custom_query, asset_query]}
        else:
            data_query = {}
        result = self.mongodb_col.find(data_query)  # create list of things
        things = list(map(from_mongo_data, result))
        rows = DataProviderService._things_to_rows(things)
        data_frame = pd.DataFrame.from_records(rows)
        # sort columns and log the table
        data_frame = data_frame[list(data_frame.columns.values)[:2] +
                                sorted(list(data_frame.columns.values)[2:])]
        self._logger.debug('\n' + str(data_frame))
        return data_frame.to_json()

    @staticmethod
    def _build_query(constraints):
        # TODO: fix types in queries (make compatible with database) + add url queries
        query = {"$and": []}
        conditions = []
        for constraint_attr, constraint_content in constraints.items():
            # prepare data
            if not constraint_content:
                continue
            query_key = constraint_attr if constraint_attr != 'columns' else 'name'
            # create query_value with query_key
            query_value = {"$or": [
                {query_key: {"$in": constraint_content['values']}}
            ]}
            for interval in constraint_content['intervals']:
                query_value["$or"].append({query_key: {"$gte": interval[0], "$lte": interval[1]}})
            # add query_key options to the query
            conditions.append(query_value)
        if conditions:
            return {"$and": conditions}
        return {}

    @staticmethod
    def _things_to_rows(things: List):
        # empty list (exception state)
        if not things:
            return []
        # (timestamp, measurement_id) identifies row; make things order row by row
        things.sort(key=lambda th: (th['timestamp'], th['measurement_id']))
        rows = []
        # possibly columns from different tables (otherwise only check index instead of key)
        # init helper variables for the first list element
        key_now = (things[0]['timestamp'], things[0]['measurement_id'])
        row_now = {'Timestamp': things[0]['timestamp'],
                   'Material_ID': things[0]['measurement_id']}
        for ind, thing in enumerate(things):
            thing_key = (thing['timestamp'], thing['measurement_id'])
            if thing_key != key_now:  # this thing is from new row
                rows.append(row_now)  # push previous row
                row_now = {'Timestamp': thing['timestamp'],
                           'Material_ID': thing['measurement_id']}  # init current row
                key_now = thing_key  # set current key_now
            row_now[thing['name']] = str(thing['value']) + ' ' + str(thing['unit'])  # create new table cell
        rows.append(row_now)  # push the last row
        return rows

    def _edc_put_assets(self):
        asset_api_instance = AssetApi(self.api_client)

        for asset_name, asset_body in self.assets.items():
            asset_entry = AssetEntryDto(asset=AssetCreationRequestDto(
                id=hash(asset_name),
                properties=DataProviderService._serialize_asset(asset_name, asset_body)),
                data_address=DataAddress(
                    properties={"type": "LocalFile", "address": "/Files/test.txt"})
            )
            # trying to update an existing asset, otherwise create a new asset
            try:
                response = asset_api_instance.update_asset(body=asset_entry)
            except TypeError:
                response = asset_api_instance.create_asset(body=asset_entry)
            self._logger.debug(response)

    @staticmethod
    def _serialize_asset(asset_name, asset_body):
        serialized_asset = dict()
        DataProviderService._serialize_asset_rec(serialized_asset, asset_body, asset_name)
        return serialized_asset

    @staticmethod
    def _serialize_asset_rec(serialized_asset, body, property_name):
        if not isinstance(body, dict):
            serialized_asset[property_name] = body
        else:  # body structure is a dictionary
            for key, item in body.items():
                DataProviderService._serialize_asset_rec(serialized_asset, item, property_name + ':' + key)



if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataProviderService.main()
