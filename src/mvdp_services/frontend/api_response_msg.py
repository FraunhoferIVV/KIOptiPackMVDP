from typing import Any

from pydantic import BaseModel


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
