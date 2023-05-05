import os

MVDP_DATA_PROVIDER_PORT = 'MVDP_DATA_PROVIDER_PORT'


class DataProviderModuleEnv:

    @property
    def port(self) -> int:
        """ ..envvar:: MVDP_DATA_PROVIDER_PORT

        Set the port for the FastAPI REST interface in the data_provider service.
        """
        return int(os.environ.get(MVDP_DATA_PROVIDER_PORT, "5479"))


env_data_provider = DataProviderModuleEnv()
