from fastapi import APIRouter


class RemoteAssets:

    def __init__(self, service):
        self.router_ = APIRouter()
        self.service = service

        self.router_.get("/")(self._list_remote_assets)

    def _list_remote_assets(self):
        return "To be implemented"

    def _provide_remote_asset(self):
        return "To be implemented"