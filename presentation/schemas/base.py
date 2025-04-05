from dataclasses import asdict, dataclass
from typing import Self


@dataclass
class BaseSchema:
    def dict(self):
        return asdict(self)
