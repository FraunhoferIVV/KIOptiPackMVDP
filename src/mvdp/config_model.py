from typing import Union, List, Dict, Optional

from fastiot.util.config_helper import FastIoTConfigModel
from pydantic import BaseModel


class AssetConfig(BaseModel):

    description: str
    """ Add a short description of the asset"""
    policy: str = "default"
    """ Define a policy to apply for this asset, defaults to ``default``"""
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
