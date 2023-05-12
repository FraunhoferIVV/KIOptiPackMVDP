import os

MVDP_DATA_PROVIDER_PORT = 'MVDP_DATA_PROVIDER_PORT'
MVDP_DATA_PROVIDER_BASE_PATH = 'MVDP_DATA_PROVIDER_BASE_PATH'


class DataProviderModuleEnv:

    @property
    def port(self) -> int:
        """ ..envvar:: MVDP_DATA_PROVIDER_PORT

        Set the port for the FastAPI REST interface in the data_provider service.
        """
        return int(os.environ.get(MVDP_DATA_PROVIDER_PORT, "5479"))

    @property
    def base_path(self) -> str:
        return os.environ.get(MVDP_DATA_PROVIDER_BASE_PATH, "")


env_data_provider = DataProviderModuleEnv()
