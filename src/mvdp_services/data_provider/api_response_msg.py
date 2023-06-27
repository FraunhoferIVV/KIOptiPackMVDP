from typing import List, Dict

from fastapi import Query
from pydantic import BaseModel

from mvdp.config_model import AssetConfig


class AssetShortview(AssetConfig):
    columns: List[str] = ["All columns"]


class AssetList(BaseModel):
    assets: Dict[str, AssetShortview]


class QueryConstraint(BaseModel):
    material_id: list = []
    timestamp: list = []
    columns: list = []
    value: list = []
    unit: list = []
    machine: list = []
