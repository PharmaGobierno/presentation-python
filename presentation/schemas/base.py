from dataclasses import dataclass, asdict
from typing import Self

@dataclass
class BaseSchema:
    def dict(self):
        return asdict(self)

    @classmethod
    def from_params(cls, **kwargs) -> Self:
        return cls(**kwargs)