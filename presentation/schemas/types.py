import binascii
import json
from base64 import b64decode
from typing import Any, Dict, Type, TypeVar, Union

from pydantic.errors import PydanticUserError

Base64TypeT = TypeVar("Base64TypeT", bound="Base64Type")


class Base64Type:
    class Base64Error(PydanticUserError):
        msg_template = "Value is not valid base64."

    def __init__(self, value: Union[Any, bytes, str, bytearray, memoryview]) -> None:
        self._b64_value = value

    @property
    def value_as_bytes(self):
        return self._b64_value

    @property
    def value_as_str(self):
        return self._b64_value.decode("utf-8")  # type: ignore

    def model_dump(self) -> Dict[str, Any]:
        try:
            _b64 = self.decode(self._b64_value)
            _b64_decoded = _b64.decode("utf-8")
            _json = json.loads(_b64_decoded)
        except json.decoder.JSONDecodeError:
            _json = {}
        return _json

    @staticmethod
    def decode(
        value: Union[Any, bytes, str, bytearray, memoryview], *, validate: bool = False
    ) -> bytes:
        return b64decode(value, validate=validate)

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls: Type[Base64TypeT], value: Any, validation_info) -> Base64TypeT:
        if isinstance(value, cls):
            return value
        if isinstance(value, str):
            value = value.encode("utf-8")
        elif isinstance(value, int):
            raise cls.Base64Error  # type: ignore
        elif not isinstance(value, (bytes, str, bytearray, memoryview)):
            value = bytes(value)
        try:
            cls.decode(value, validate=True)
        except binascii.Error:
            raise cls.Base64Error  # type: ignore
        return cls(value)
