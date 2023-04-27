import os
from typing import List

from fastiot.cli.model import InfrastructureService
from fastiot.cli.model.infrastructure_service import InfrastructureServicePort, InfrastructureServiceVolume, \
    InfrastructureServiceEnvVar

from mvdp.env import MVDP_EDC_HOST, MVDP_EDC_PORT, MVDP_EDC_PORT_2, MVDP_EDC_PORT_3, MVDP_EDC_PORT_4


class EclipseDataSpaceConnector(InfrastructureService):
    name: str = "edc"
    image: str = "docker.dev.ivv-dd.fhg.de/kioptipack/man_connector1"

    host_name_env_var: str = MVDP_EDC_HOST

    ports: List[InfrastructureServicePort] = [InfrastructureServicePort(container_port=8181,
                                                                        default_port_mount=8181,
                                                                        env_var=MVDP_EDC_PORT),
                                              InfrastructureServicePort(container_port=8182,
                                                                        default_port_mount=8182,
                                                                        env_var=f"{MVDP_EDC_PORT_2}"),
                                              InfrastructureServicePort(container_port=5005,
                                                                        default_port_mount=5005,
                                                                        env_var=f"{MVDP_EDC_PORT_3}"),
                                              InfrastructureServicePort(container_port=7171,
                                                                        default_port_mount=7171,
                                                                        env_var=f"{MVDP_EDC_PORT_4}"),
                                              ]

    environment: List[InfrastructureServiceEnvVar] = [
        InfrastructureServiceEnvVar(name='IDS_WEBHOOK_ADDRESS',
                                    default=f"http://{name}:{os.environ.get(MVDP_EDC_PORT_2, ports[1].default_port_mount)}")
    ]

    volumes: List[InfrastructureServiceVolume] = [InfrastructureServiceVolume(container_volume='/localFiles/resources',
                                                                              env_var='MVDP_EDC_CONFIG_MOUNT',
                                                                              default_volume_mount='./resources',
                                                                              tmpfs_for_tests=False)]
