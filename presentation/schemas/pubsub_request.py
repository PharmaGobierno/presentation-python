from base64 import b64decode
from dataclasses import dataclass
from json import decoder, loads
from typing import Any, Dict, Optional, Union


def decode_b64(
    b64_value: Union[Any, bytes, str, bytearray, memoryview], validate: bool = False
) -> Dict[str, Any]:
    if isinstance(b64_value, str):
        b64_value = b64_value.encode("utf-8")
    elif not isinstance(b64_value, (bytes, str, bytearray, memoryview)):
        # TODO: check this case
        b64_value = bytes(b64_value)
    else:
        raise TypeError("The pubsub data have a value type that cant be decoded")
    try:
        _b64 = b64decode(b64_value, validate=validate)
        _b64_decoded = _b64.decode("utf-8")
        _json = loads(_b64_decoded)
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
