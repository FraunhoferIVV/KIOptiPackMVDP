import os

MVDP_FRONTEND_PORT = 'MVDP_FRONTEND_PORT'


class FrontendModuleEnv:

    @property
    def fastapi_port(self) -> int:
        """ ..envvar:: MVDP_FRONTEND_PORT

        Set the port for the FastAPI REST interface in the frontend service.
        """
        return int(os.environ.get(MVDP_FRONTEND_PORT, "5478"))


env_frontend = FrontendModuleEnv()
