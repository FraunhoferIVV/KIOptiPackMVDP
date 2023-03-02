from fastiot.core.data_models import FastIoTData
from typing import Any
from typing import Optional

from mvdp_services.frontend.FileConfiguration import FileConfiguration


class UploadData(FastIoTData):
    dataFile: Any
    fileConfig: Optional[FileConfiguration]
    materialID: Optional[str]
