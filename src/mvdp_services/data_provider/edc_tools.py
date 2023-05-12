from mvdp.edc_management_client.api_client import ApiClient
from mvdp.edc_management_client.configuration import Configuration
from mvdp.env import mvdp_env


def init_edc():
    config = Configuration()
    config.host = f"http://{mvdp_env.edc_host}:{mvdp_env.edc_port_2}/api/v1/management"
    config.verify_ssl = False
    config.debug = True
    config.api_key = {'X-Api-Key': mvdp_env.edc_api_key}

    return ApiClient(config, header_name='X-Api-Key', header_value=mvdp_env.edc_api_key)


def serialize_asset(asset_name, asset_body):
    serialized_asset = dict()
    serialize_asset_rec(serialized_asset, asset_body, asset_name)
    return serialized_asset


def serialize_asset_rec(serialized_asset, body, property_name):
    if not isinstance(body, dict):
        serialized_asset[property_name] = body
    else:  # body structure is a dictionary
        for key, item in body.items():
            serialize_asset_rec(serialized_asset, item, property_name + ':' + key)
