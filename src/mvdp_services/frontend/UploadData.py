from fastiot.core.data_models import FastIoTData
from typing import Any
from typing import Optional

from FileConfiguration import FileConfiguration


class UploadData(FastIoTData):
    dataFile: Any
    fileConfig: Optional[FileConfiguration]
    materialID: Optional[str]


# Example:
"""
{
  "dataFile": "data, data, data", 
  "fileConfig": {
     "dataDelimiter": "semicolon",
     "decimalDelimiter": "point"
  },
  "materialID": "Verpackung2"
}
"""
