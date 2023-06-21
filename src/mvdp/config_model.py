from enum import Enum
from typing import Union, List, Dict, Optional

from fastiot.util.config_helper import FastIoTConfigModel
from pydantic import BaseModel, validator, root_validator


class AssetServingTypeEnum(str, Enum):
    thing = 'thing'
    json = 'json'


class AssetConfig(BaseModel):
    class Config:
        use_enum_values = True

    description: str
    """ Add a short description of the asset"""
    policy: str = "default"
    """ Define a policy to apply for this asset, defaults to ``default``"""
    asset_serving_type: AssetServingTypeEnum = AssetServingTypeEnum.thing
    """
    How is this asset created? From Things like when uploading tables or machine data or do you provide raw json  
    documents?
    """
    asset_collection: str = ''
    """
    Any collection in the MongoDB set specifically for this asset. Will use the globally configured one in 
    :attr:`mvdp.config_model.DataProviderConfiguration.collection`.
    """
    constraints: Dict[str, Optional[Union[str, dict, list]]] = {}
    """ Define any constraints. Documentation to follow.
        ```
    columns:
      - "Sensor_B"
    measurement_id:
    timestamp:
      - interval:
          start: 09/19/22 13:55:10
          end: 09/19/22 13:55:30
      - 09/19/22 13:55:00
    ```
    """

    calculated_constraints_: dict = {}
    """ Leave empty, will be calculated automatically. """

    def set_constraints(self, constraints: dict):
        self.calculated_constraints_ = constraints


class DataProviderConfiguration(FastIoTConfigModel):
    """
    search_index:
  - measurement_id, _timestamp
  - name
collection: 'thing'
assets:
  - Asset_1:
      description: "Asset Sensor_B"
      policy: default
      constraints:

    """

    class Config:
        arbitrary_types_allowed = True

    search_index: List[Union[str, List[str]]]
    collection: str
    assets: Dict[str, AssetConfig] = {}

    @root_validator()
    def check_collections(cls, v):
        for asset in v['assets'].values():
            if not asset.asset_collection:
                asset.asset_collection = v['collection']
        return v
