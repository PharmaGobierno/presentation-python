from dataclasses import asdict, dataclass
from typing import Self


@dataclass
class BaseSchema:
    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}

    @classmethod
    def from_params(cls, **kwargs) -> Self:
        return cls(**kwargs)
