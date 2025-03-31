from typing import Optional
from dataclasses import dataclass
from .base import BaseSchema

@dataclass
class ErrorSchema(BaseSchema):
    code: str
    message: str
    details: Optional[str] = None
    location: Optional[str] = None
    parameter: Optional[str] = None
    displayable_message: Optional[str] = None
