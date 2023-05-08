from fastiot.db.mongodb_helper_fn import get_mongodb_client_from_env


class TableHandler:
    def __init__(self):
        self._database = get_mongodb_client_from_env()

    def edit_data(self):
        pass

