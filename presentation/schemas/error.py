from typing import Optional, TypeVar

from pydantic import BaseModel, ConfigDict, Field

ErrorSchemaT = TypeVar("ErrorSchemaT", bound="ErrorSchema")


class ErrorSchema(BaseModel):
    code: str
    message: str
    details: str
    location: str
    parameter: Optional[str] = None
    displayable_message: Optional[str] = Field(default=None)

    model_config = ConfigDict(
        populate_by_name=True, use_enum_values=True, extra="allow"
    )
