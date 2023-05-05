import os

MVDP_EDC_HOST = 'MVDP_EDC_HOST'
MVDP_EDC_API_KEY = 'MVDP_EDC_API_KEY'
MVDP_EDC_PORT = 'MVDP_EDC_PORT'
MVDP_EDC_PORT_2 = 'MVDP_EDC_PORT_2'
MVDP_EDC_PORT_3 = 'MVDP_EDC_PORT_3'
MVDP_EDC_PORT_4 = 'MVDP_EDC_PORT_4'


class MVDPEnv:
    """ Environment variables for the MVDP"""

    @property
    def edc_host(self) -> str:
        return os.environ.get(MVDP_EDC_HOST)

    @property
    def edc_api_key(self) -> str:
        return os.environ.get(MVDP_EDC_API_KEY, 'ApiKeyDefaultValue')

    @property
    def edc_port(self) -> int:
        return int(os.environ.get(MVDP_EDC_PORT))

    @property
    def edc_port_2(self) -> int:
        from mvdp.fiot_extension import EclipseDataSpaceConnector
        return int(os.environ.get(MVDP_EDC_PORT_2, EclipseDataSpaceConnector().get_default_port(MVDP_EDC_PORT_2)))

    @property
    def edc_port_3(self) -> int:
        return int(os.environ.get(MVDP_EDC_PORT_3))

    @property
    def edc_port_4(self) -> int:
        return int(os.environ.get(MVDP_EDC_PORT_4))


mvdp_env = MVDPEnv()
