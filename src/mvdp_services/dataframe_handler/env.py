import os

MVDP_DATAFRAME_HANDLER_PORT = 'MVDP_DATAFRAME_HANDLER_PORT'
MVDP_DATAFRAME_HANDLER_BASE_PATH = 'MVDP_DATAFRAME_HANDLER_BASE_PATH'


class DataframeHandlerModuleEnv:

    @property
    def port(self) -> int:
        """ ..envvar:: MVDP_DATAFRAME_HANDLER_PORT

        Set the port for the FastAPI REST interface in the dataframe_handler service.
        """
        return int(os.environ.get(MVDP_DATAFRAME_HANDLER_PORT, "5480"))

    @property
    def base_path(self) -> str:
        return os.environ.get(MVDP_DATAFRAME_HANDLER_BASE_PATH, "")


env_dataframe_handler = DataframeHandlerModuleEnv()
