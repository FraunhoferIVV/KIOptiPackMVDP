import logging
import os
import shutil
import sys

import yaml
from fastiot.cli.constants import DEPLOYMENTS_CONFIG_DIR, DEPLOYMENTS_CONFIG_FILE, FASTIOT_DOCKER_REGISTRY
from fastiot.cli.env import env_cli
from fastiot.cli.model.deployment import ServiceConfig, DeploymentConfig, InfrastructureServiceConfig
from fastiot.cli.model.project import ProjectContext
from fastiot.cli.typer_app import create_cmd

from mvdp.config_model import DataProviderConfiguration, AssetConfig, AssetServingTypeEnum, FrontendConfiguration

try:
    import typer
except ImportError:
    if not env_cli.within_container:
        logging.error("Could not import Typer. To use the CLI you need to install `fastiot[dev]`.")
    sys.exit(1)

try:
    from rich import print  # Should usually be installed because of typer[all]
except ImportError:
    pass  # Just use built-in print command

@create_cmd.command()
def mvdp_deployment(deployment_name: str = typer.Argument(None, help="The deployment name to generate"),
                    force: bool = typer.Option(False, '-f', '--force',
                                               help="Force overwriting of existing deployment.")
                    ):
    """
    Create a simple deployment configuration including Eclipse Dataspace Connector and/or some backend services to
    get started. You have to select at least one out of edc and backend.
    """
    print(f"Creating deployment {deployment_name}")

    context = ProjectContext.default

    deployment_dir = os.path.join(context.project_root_dir, DEPLOYMENTS_CONFIG_DIR, deployment_name)
    if os.path.isdir(deployment_dir):
        if force:
            shutil.rmtree(deployment_dir, ignore_errors=False, onerror=None)
        else:
            print("[bold red]Deployment already exists.[/bold red] To overwrite use the option `--force`.")
            raise typer.Exit(10)

    os.makedirs(os.path.join(deployment_dir, 'config_dir'))

    infrastructure_services = {}
    services = {}

    backend = typer.prompt("Do you want the backend services to be included?",
                           type=bool, default="Yes")
    if backend:
        if context.project_namespace == 'mvdp':  # No need to adjust anything, just use the local image for fiot config
            services['frontend'] = None
            services['data_provider'] = None
        else:
            docker_registry = os.environ.get(FASTIOT_DOCKER_REGISTRY, "")
            services['frontend'] = ServiceConfig(image="mvdp/frontend", docker_registry=docker_registry)
            services['data_provider'] = ServiceConfig(image="mvdp/data_provider", docker_registry=docker_registry)

        infrastructure_services = {i: InfrastructureServiceConfig() for i in ['nats', 'mongodb']}

        serving_type = typer.prompt(
            "Will you be serving »things« (like serving machine data or uploaded tables over the "
            "ui) or »json« Documents?",
            type=AssetServingTypeEnum, default=AssetServingTypeEnum.thing, show_choices=True)

        _create_frontend_config(deployment_dir=deployment_dir, serving_type=serving_type,
                                deployment_name=deployment_name)
        _create_object_storage_config(deployment_dir=deployment_dir, serving_type=serving_type)
        _create_data_provider_config(deployment_dir=deployment_dir, serving_type=serving_type)

    edc = typer.prompt("Do you want the Eclipse Data Space connector to be included?",
                       type=bool, default="No")
    if edc:
        infrastructure_services["edc"] = InfrastructureServiceConfig()
        _create_edc_setup()

    config = DeploymentConfig(name=deployment_name,
                              services=services, infrastructure_services=infrastructure_services)
    with open(os.path.join(deployment_dir, DEPLOYMENTS_CONFIG_FILE), "w") as file:
        yaml.dump(config.dict(), file)

    print(f"[bold green]Successfully created deployment {deployment_name}[/bold green]")
    print("To actually start or deploy your deployment you need to run `fiot config` now!")


def _create_frontend_config(deployment_dir: str, serving_type: AssetServingTypeEnum, deployment_name: str):
    """ Settings for frontend """
    frontend_title = typer.prompt("How do you want your frontend to be titled?", default=deployment_name, type=str)
    if serving_type == AssetServingTypeEnum.thing:
        upload = typer.prompt("Do you want to enable table or json uploads", default="Yes", type=bool)
        edit_table = typer.prompt("Do you want your table to be editable?", default="Yes", type=bool)
    else:  # Editing json is not possible, thus upload needs to be on
        upload = True
        edit_table = False
    config = FrontendConfiguration(frontend_title=frontend_title,
                                   upload_forbidden=not upload,
                                   table_readonly=not edit_table)

    with open(os.path.join(deployment_dir, 'config_dir', 'FrontendService.yaml'), "w") as file:
        yaml.dump(config.dict(), file)


def _create_object_storage_config(deployment_dir: str, serving_type: AssetServingTypeEnum):
    """ Settings for ObjectStorage """
    context = ProjectContext.default

    store_timeseries = typer.prompt("Will you be storing timeseries data in your storage?",
                                    type=bool)

    config = {}

    search_index = {'thing': ['name']}
    if store_timeseries:
        search_index['thing'].append('timestamp')
    config['search_index'] = search_index

    if serving_type == AssetServingTypeEnum.thing:
        subscriptions = {'thing.>': {'collection': serving_type.value,
                                     'reply_subject_name': 'objects',
                                     'enable_overwriting': True,
                                     'identify_object_with': ["measurement_id", "name"]
                                     }}
    elif serving_type == AssetServingTypeEnum.json:
        subscriptions = {'arbitrary_j_s_o_n_message': {'collection': serving_type.value,
                                                       'reply_subject_name': 'json_objects',
                                                       'enable_overwriting': True,
                                                       'identify_object_with': ["json_data.Material_ID"]
                                                       }}
    else:
        print(f"[bold red]:warning: Warning[/bold red]: Object Storage configuration not yet implemented for serving "
              f"type {serving_type.value}.\nNot creating a configuration for object storage!")
        return

    if store_timeseries:
        subscriptions['thing.>']['identify_object_with'].append('_timestamp')
    config['subscriptions'] = subscriptions

    with open(os.path.join(deployment_dir, 'config_dir', 'ObjectStorageService.yaml'), "w") as file:
        yaml.dump(config, file)


def _create_data_provider_config(deployment_dir: str, serving_type: AssetServingTypeEnum):
    """ Setup for frontend """

    asset_full = AssetConfig(description="Complete data", policy="default", constraints={},
                             asset_serving_type=serving_type.value)
    config = DataProviderConfiguration(collection=serving_type.value,
                                       assets={"Full": asset_full},
                                       search_index=[])

    with open(os.path.join(deployment_dir, 'config_dir', 'DataProviderService.yaml'), "w") as file:
        yaml.dump(config.dict(), file)


def _create_edc_setup():
    """ Create the files needed for the Eclipse Dataspace Connector to start"""
    print("[bold red]:warning: Warning[/bold red]: Setting up the EDC has not been implemented yet.")
