"""
Application logic for dataframe_handler service
"""

import asyncio
import logging

import pandas as pd

from fastiot.core import FastIoTService


class DataframeHandlerService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass


if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataframeHandlerService.main()
