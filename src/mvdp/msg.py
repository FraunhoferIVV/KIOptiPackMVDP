""" Various custom messages withing the MVDP """
from typing import Optional

from fastiot.core import FastIoTResponse, FastIoTRequest, FastIoTPublish


class HealthCheckReply(FastIoTResponse):
    edc_health: Optional[bool] = None


class HealthCheckRequest(FastIoTRequest):
    _reply_cls = HealthCheckReply
    request: bool = True


class ArbitraryJSONMessage(FastIoTPublish):
    """ Class used to send any type of JSON message received as data upload """
    _handles_hierarchical_subjects = False
    json_data: dict
