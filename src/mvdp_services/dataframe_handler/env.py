import os

MVDP_DATAFRAME_HANDLER_PORT = 'MVDP_DATAFRAME_HANDLER_PORT'


class DataframeHandlerModuleEnv:

    @property
    def port(self) -> int:
        """ ..envvar:: MVDP_DATAFRAME_HANDLER_PORT

        Set the port for the FastAPI REST interface in the dataframe_handler service.
        """
        return int(os.environ.get(MVDP_DATAFRAME_HANDLER_PORT, "5480"))


env_dataframe_handler = DataframeHandlerModuleEnv()
