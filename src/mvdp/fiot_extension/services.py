from typing import List

from fastiot import InfrastructureService, InfrastructureServicePort

from mvdp.env import MVDP_EDC_HOST, MVDP_EDC_PORT


class EclipseDataSpaceConnector(InfrastructureService):
    name: str = "edc"
    image: str = "docker.dev.ivv-dd.fhg.de/kioptipack/test_connector"

    host_name_env_var: str = MVDP_EDC_HOST
    ports: List[InfrastructureServicePort] = [InfrastructureServicePort(container_port=8181,
                                                                        default_port_mount=8181,
                                                                        env_var=MVDP_EDC_PORT)]
