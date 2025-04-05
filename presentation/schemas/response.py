from dataclasses import dataclass, field
from time import time
from typing import List, Optional, TypeVar

from .base import BaseSchema
from .error import ErrorSchema

ResponseSchemaT = TypeVar("ResponseSchemaT", bound="ResponseSchema")

@dataclass
class ResponseSchema(BaseSchema):
    status: int
    process_id: str
    timestamp: int = field(default_factory=lambda: int(time() * 1000))
    version: str = "1.0.0"
    data: Optional[dict] = None
    errors: Optional[List[ErrorSchema]] = None
