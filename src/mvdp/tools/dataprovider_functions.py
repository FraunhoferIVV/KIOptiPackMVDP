import pandas as pd
from typing import List

from fastiot.msg import Thing

from mvdp.env import mvdp_env
from mvdp.edc_management_client.api_client import ApiClient
from mvdp.edc_management_client.configuration import Configuration


def init_edc():
    config = Configuration()
    config.host = f"http://{mvdp_env.edc_host}:{mvdp_env.edc_port_2}/api/v1/management"
    config.verify_ssl = False
    config.debug = True
    config.api_key = {'X-Api-Key': mvdp_env.edc_api_key}

    return ApiClient(config, header_name='X-Api-Key', header_value=mvdp_env.edc_api_key)


def calculate_constraints(constraints_object):
    constraints = {}
    for constraint_attr, constraint_content in constraints_object.items():
        constraints[constraint_attr] = (
            calculate_single_constraint(constraint_attr, constraint_content)
        )
    return constraints


def calculate_single_constraint(attribute: str, constraint_values : list):
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


def build_query(constraints):
    # TODO: fix types in queries (make compatible with database) + add url queries
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


def things_to_rows(things: List[Thing]):
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


def serialize_asset(asset_name, asset_body):
    serialized_asset = dict()
    serialize_asset_rec(serialized_asset, asset_body, asset_name)
    return serialized_asset


def serialize_asset_rec(serialized_asset, body, property_name):
    if not isinstance(body, dict):
        serialized_asset[property_name] = body
    else:  # body structure is a dictionary
        for key, item in body.items():
            serialize_asset_rec(serialized_asset, item, property_name + ':' + key)

