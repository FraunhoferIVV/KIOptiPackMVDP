import hashlib
import logging

from mvdp.edc_management_client.api import AssetApi
from mvdp.edc_management_client.api_client import ApiClient
from mvdp.edc_management_client.configuration import Configuration
from mvdp.edc_management_client.models import AssetCreationRequestDto, AssetEntryDto, DataAddress
from mvdp.edc_management_client.rest import ApiException
from mvdp.env import mvdp_env


def init_edc():
    config = Configuration()
    config.host = f"http://{mvdp_env.edc_host}:{mvdp_env.edc_port_2}/api/v1/management"
    config.verify_ssl = False
    config.debug = True
    config.api_key = {'X-Api-Key': mvdp_env.edc_api_key}

    return ApiClient(config, header_name='X-Api-Key', header_value=mvdp_env.edc_api_key)


def edc_put_assets(api_client, assets):
    asset_api_instance = AssetApi(api_client)

    for asset_name, asset_body in assets.items():
        asset_id = hashlib.md5(asset_name.encode('utf-8')).hexdigest()
        asset_entry = AssetEntryDto(
            asset=AssetCreationRequestDto(
                id=asset_id,
                properties={"asset:prop:name": "test", "asset:prop:version": "1.0",
                            "asset:prop:id": "DatasetTest", "asset:prop:contenttype": "text/plain"}),
            data_address=DataAddress(
                properties={"type": "LocalFile", "address": "/Files/test.txt"})
        )
        # trying to update an existing asset, otherwise create a new asset
        try:
            response = asset_api_instance.update_asset(body=asset_entry, asset_id=asset_id)
        except ApiException:
            response = asset_api_instance.create_asset(body=asset_entry)
        logging.debug(response)


def edc_get_contract(asset_id: str):
    """
    METHOD STUB!
    Returns the contract for a given (remote) asset
    """
