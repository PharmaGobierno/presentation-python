from dataclasses import asdict, dataclass


@dataclass
class BaseSchema:
    def dict(self):
        return asdict(self)
