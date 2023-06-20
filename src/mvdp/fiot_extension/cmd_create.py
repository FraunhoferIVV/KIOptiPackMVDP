import logging
import os

import typer as typer
import yaml
from fastiot.cli.env import env_cli
from fastiot.cli.model.deployment import ServiceConfig, DeploymentConfig
from fastiot.cli.typer_app import create_cmd
from fastiot.cli.constants import DEPLOYMENTS_CONFIG_DIR, DEPLOYMENTS_CONFIG_FILE
from fastiot.cli.model.project import ProjectContext


@create_cmd.command()
def mvdp_deployment(deployment_name: str = typer.Argument(None, help="The deployment name to generate"),
                    edc: bool = typer.Option(False,
                                             help="Create a basic setup for an Eclipse Dataspace Connector"),
                    backend: bool = typer.Option(False,
                                                 help="Create a basic deployment for backend services like database."),
                    force: bool = typer.Option(False, '-f', '--force',
                                               help="Force overwriting of existing deployment.")
                    ):
    """
    Create a simple deployment configuration including Eclipse Dataspace Connector and/or some backend services to
    get started. You have to select at least one out of edc and backend.
    """

    if not edc and not backend:
        logging.error("You need to set at least one of --enable-edc or --enabled-backend to set some services.")
        raise typer.Exit(10)

    context = ProjectContext.default

    deployment_dir = os.path.join(context.project_root_dir, DEPLOYMENTS_CONFIG_DIR, deployment_name)
    if os.path.isdir(deployment_dir):
        if force:
            os.removedirs(deployment_dir)
        else:
            logging.error("Deployment already exists. To overwrite use the option `--force`.")
            raise typer.Exit(10)

    os.makedirs(deployment_dir)

    infrastructure_services = {}
    services = {}

    if backend:
        #infrastructure_services = {s: None for s in ['nats', 'mongodb']}
        services = {s: ServiceConfig(image=f"mvdp/{s}", docker_registry=env_cli.docker_registry) for s in
                    ['data_provider', 'frontend']}

    if edc:
        infrastructure_services["edc"]=None
        _create_edc_setup()

    config = DeploymentConfig(name=deployment_name,
                              services=services, infrastructure_services=infrastructure_services)
    with open(os.path.join(deployment_dir, DEPLOYMENTS_CONFIG_FILE), "w") as file:
        yaml.dump(config.dict(), file)


def _create_edc_setup():
    """ Create the files needed for the Eclipse Dataspace Connector to start"""
