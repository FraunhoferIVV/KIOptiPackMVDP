import os

MVDP_EDC_HOST = 'MVDP_EDC_HOST'
MVDP_EDC_PORT = 'MVDP_EDC_PORT'


class MVDPEnv:
    """ Environment variables for the MVDP"""

    @property
    def edc_host(self) -> str:
        return os.environ.get(MVDP_EDC_HOST)

    @property
    def edc_port(self) -> int:
        return int(os.environ.get(MVDP_EDC_PORT))


mvdp_env = MVDPEnv()
