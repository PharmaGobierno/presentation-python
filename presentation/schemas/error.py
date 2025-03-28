from typing import Optional

from .base import BaseSchema


class ErrorSchema(BaseSchema):
    code: str
    message: str
    details: str
    location: Optional[str] = None
    parameter: Optional[str] = None
    displayable_message: Optional[str] = None
