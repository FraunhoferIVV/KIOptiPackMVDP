""" Various custom messages withing the MVDP """
from typing import Optional

from fastiot.core import FastIoTResponse, FastIoTRequest


class HealthCheckReply(FastIoTResponse):
    edc_health: Optional[bool] = None


class HealthCheckRequest(FastIoTRequest):
    _reply_cls = HealthCheckReply
    request: bool = True
