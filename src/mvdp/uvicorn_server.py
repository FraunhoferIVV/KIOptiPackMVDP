""" Simple class to provide an async uvicorn server to be started within a SAM module"""
import asyncio
from typing import Optional, List

try:
    from uvicorn import Server, Config
except ImportError:  # We mock some stuff for the following code not to fail
    class Server:
        def __init__(self, *args, **kwargs):
            pass


    class Config:
        def __init__(self, *args, **kwargs):
            pass


class UvicornAsyncServer(Server):
    """Uvicorn async server  """

    def __init__(self, app, port: int, host='0.0.0.0'):
        """Create an Uvicorn test server

        Args:
            app (FastAPI, optional): the FastAPI app. Defaults to main.app.
            host (str, optional): the host ip. Defaults to '0.0.0.0'.
            port (int, optional): the port. Defaults to PORT.
        """
        self._startup_done = asyncio.Event()
        super().__init__(config=Config(app, host=host, port=port))

    async def startup(self, sockets: Optional[List] = None) -> None:
        """Override uvicorn startup"""
        await super().startup(sockets=sockets)
        self.config.setup_event_loop()
        self._startup_done.set()

    async def up(self) -> None:
        """Start up server asynchronously"""
        self._serve_task = asyncio.create_task(self.serve())
        await self._startup_done.wait()

    async def down(self) -> None:
        """Shut down server asynchronously"""
        self.should_exit = True
        await self._serve_task
