import pandas as pd

from fastapi import Depends
from fastiot.db.mongodb_helper_fn import get_mongodb_client_from_env
from fastiot.env import env_mongodb
from fastiot.msg import Thing
from fastiot.msg.custom_db_data_type_conversion import from_mongo_data
from fastiot.util.object_helper import parse_object_list

from mvdp.tools.dataprovider_functions import things_to_rows
from mvdp_services.frontend.api_response_msg import Table
from mvdp_services.frontend.env import env_frontend
from mvdp_services.frontend.manager import manager


class TableHandler:
    def __init__(self):
        database = get_mongodb_client_from_env().get_database(env_mongodb.name)
        self.mongodb_col = database.get_collection(env_frontend.mongodb_collection)

    def return_table(self, user=Depends(manager)) -> Table:
        """ Transfer the table
        """

        result = self.mongodb_col.find({})  # create list of things
        things = parse_object_list(list(map(from_mongo_data, result)), Thing)
        rows = things_to_rows(things)
        data_frame = pd.DataFrame.from_records(rows)
        # sort columns and log the table
        data_frame = data_frame[list(data_frame.columns.values)[:2] +
                                sorted(list(data_frame.columns.values)[2:])]

        # quickfix for table with different columns
        data_frame = data_frame.fillna('no_value')

        if len(data_frame.columns) > 0:
            response = Table(headers=[{'text': str(c), 'value': str(c), 'sortable': True} for c in data_frame.columns],
                             items=data_frame.to_dict(orient="records"))
        else:
            response = Table(headers=[{"text": "No Data", "value": "No Data"}], items=[])

        return response
