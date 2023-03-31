from typing import List

from fastiot.cli.model import InfrastructureService
from fastiot.cli.model.infrastructure_service import InfrastructureServicePort

from mvdp.env import MVDP_EDC_HOST, MVDP_EDC_PORT, MVDP_EDC_PORT_2, MVDP_EDC_PORT_3


class EclipseDataSpaceConnector(InfrastructureService):
    name: str = "edc"
    image: str = "docker.dev.ivv-dd.fhg.de/kioptipack/man_connector2"

    host_name_env_var: str = MVDP_EDC_HOST
    ports: List[InfrastructureServicePort] = [InfrastructureServicePort(container_port=8181,
                                                                        default_port_mount=8181,
                                                                        env_var=MVDP_EDC_PORT),
                                              InfrastructureServicePort(container_port=8182,
                                                                        default_port_mount=8182,
                                                                        env_var=f"{MVDP_EDC_PORT_2}"),
                                              InfrastructureServicePort(container_port=8183,
                                                                        default_port_mount=8183,
                                                                        env_var=f"{MVDP_EDC_PORT_3}"),
                                              ]
