from time import time
from typing import List, Optional, TypeVar

from pydantic import BaseModel, Field, PositiveInt

from .error import ErrorSchema

ResponseSchemaT = TypeVar("ResponseSchemaT", bound="ResponseSchema")


class ResponseSchema(BaseModel):
    version: str = "1.0.0"
    status: int
    process_id: str
    timestamp: PositiveInt = Field(default_factory=lambda: int(time() * 1000))
    data: Optional[dict] = Field(default=None)
    errors: Optional[List[ErrorSchema]] = Field(default=None)

    def model_dump(self, exclude_none=True, **kwargs):
        kwargs.setdefault("exclude_none", exclude_none)
        return super().model_dump(**kwargs)
