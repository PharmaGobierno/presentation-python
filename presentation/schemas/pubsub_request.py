import binascii
from base64 import b64decode
from dataclasses import dataclass
from json import decoder, loads
from typing import Any, Dict, Optional, Union


def decode_b64(
    value: Union[Any, bytes, str, bytearray, memoryview], validate: bool = False
) -> Dict[str, Any]:
    if isinstance(value, str):
        value = value.encode("utf-8")
    elif not isinstance(value, (bytes, str, bytearray, memoryview)):
        # TODO: check this case
        value = bytes(value)
    else:
        raise TypeError("The pubsub data have a value type that cant be decoded")

    try:
        _b64 = b64decode(value, validate=validate)
        _decoded_str = _b64.decode("utf-8")
    except (binascii.Error, ValueError):
        # the value is not base64 encoded
        _decoded_str = value.decode("utf-8")
    try:
        _json = loads(_decoded_str)
    except decoder.JSONDecodeError:
        _json = {}
    return _json


@dataclass
class PubsubMessage:
    data: Union[Any, bytes, str, bytearray, memoryview]
    messageId: str
    message_id: str
    publishTime: str
    publish_time: str
    attributes: Optional[Dict[str, str]] = None
    orderingKey: Optional[str] = None
    decoded_data: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        self.decoded_data = decode_b64(self.data)


@dataclass
class PubsubBody:
    message: dict
    subscription: str
    deliveryAttempt: Optional[int] = None
