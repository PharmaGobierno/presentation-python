from .errors import BaseError
from .schemas.error import ErrorSchema
from .schemas.response import ResponseSchema


class Response:
    __version__ = "1.0.0"

    def __init__(
        self,
        *,
        process_id: str,
        version: str = __version__,
    ):
        self.errors = []
        self.data = {}
        self.process_id = process_id
        self.version = version
        self._status = None

    @property
    def status(self) -> int:
        if self._status is None:
            raise ValueError("Status is not set in Presentation.Response object")
        return self._status

    @status.setter
    def status(self, value: int) -> None:
        self._status = value

    @property
    def response(self) -> dict:
        response = ResponseSchema.from_params(
            errors=self.errors,
            data=self.data,
            process_id=self.process_id,
            version=self.version,
            status=self.status,
        )
        return response.dict()

    def update_data(self, result: dict) -> None:
        self.data.update(result)

    def add_error(self, code: BaseError) -> None:
        error = ErrorSchema(**code.error_schema)
        self.errors.append(error.dict())
