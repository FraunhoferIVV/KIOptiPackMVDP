from typing import List, Dict

from pydantic import BaseModel

from mvdp.config_model import AssetConfig


class AssetShortview(AssetConfig):
    columns: List[str] = ["All columns"]


class AssetList(BaseModel):
    assets: Dict[str, AssetShortview]