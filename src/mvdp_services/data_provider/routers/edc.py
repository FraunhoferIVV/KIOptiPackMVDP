from fastapi import APIRouter


class EDCCommunication:

    def __init__(self, service):
        self.router_ = APIRouter()
        self.service = service

        self.router_.get("/contracts")(self._list_contracts)

    async def _list_contracts(self):
        return "OK"
