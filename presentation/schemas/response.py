from dataclasses import dataclass, field
from time import time
from typing import List, Optional

from .base import BaseSchema
from .error import ErrorSchema


@dataclass
class ResponseSchema(BaseSchema):
    status: int
    process_id: str
    timestamp: int = field(default_factory=lambda: int(time() * 1000))
    version: str = "1.0.0"
    data: Optional[dict] = None
    errors: List[ErrorSchema] = field(default_factory=list)
