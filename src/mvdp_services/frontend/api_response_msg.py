from enum import Enum
from typing import Any

from pydantic import BaseModel


class PossibleFileTypes(str, Enum):
    csv = 'csv'
    json = 'json'
    xlsx = 'xlsx'


class PossibleCSVDelimiters(str, Enum):
    comma = 'comma'
    point = 'point'
    semicolon = 'semicolon'
    tabulator = 'tabulator'

    def to_raw(self) -> str:
        """
        Returns the raw value instead of the name, so ``dot`` becomes ``.``.
        """
        raw_dict = {self.comma: ',', self.point: '.', self.semicolon: ';', self.tabulator: '\t'}
        return raw_dict.get(self)


class HealthResponse(BaseModel):
    overall_status: bool = False
    """ Overall overall_status """

    edc: bool = False
    """ Status of the Eclipse Data Space Connector"""

    broker: bool = False
    """ Status of the connection to the message broker"""


class Table(BaseModel):
    """ Data for editable table """
    headers: list[dict[str, str]]
    items: list[dict[str, Any]]


class FrontendConfiguration(BaseModel):
    """ Some configuration options to be transferred to the frontend """
    title: str
    """ A frontend title configured via the env var ``MVDP_FRONTEND_TITLE`` on server side."""
