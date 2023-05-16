import os

MVDP_FRONTEND_PORT = 'MVDP_FRONTEND_PORT'
MVDP_FRONTEND_TITLE = 'MVDP_FRONTEND_TITLE'
MVDP_MONGODB_COLLECTION = 'MVDP_MONGODB_COLLECTION'


class FrontendModuleEnv:

    @property
    def port(self) -> int:
        """ ..envvar:: MVDP_FRONTEND_PORT

        Set the port for the FastAPI REST interface in the frontend service.
        """
        return int(os.environ.get(MVDP_FRONTEND_PORT, "5478"))

    @property
    def frontend_title(self) -> str:
        return os.environ.get(MVDP_FRONTEND_TITLE, "Minimum Viable Dataspace Participant")

    @property
    def mongodb_collection(self) -> str:
        return os.environ.get(MVDP_MONGODB_COLLECTION, "thing")


env_frontend = FrontendModuleEnv()
