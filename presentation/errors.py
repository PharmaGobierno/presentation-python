from enum import Enum
from typing import Optional


class ErrorLocationEnum(str, Enum):
    PATH = "request.url.path"
    QUERY = "request.url.query_params"
    BODY = "request.body"
    HEADERS = "request.headers"
    AUTHORIZATION = "request.authorization"
    SERVER = "server"
    DATABASE = "database"


class BaseError(Exception):
    __version__ = "1.0.0"
    ERROR_LOCATION = ErrorLocationEnum

    code: str = None
    message: str = None
    http_status: int = 500

    def __init__(
        self,
        details: Optional[str] = None,
        location: Optional[str] = None,
        parameter: Optional[str] = None,
        displayable_message: Optional[str] = None,
    ):
        if not self.code or not self.message:
            raise ValueError("Missing required fields in error subclass")
        
        self.details = details
        self.location = location
        self.parameter = parameter
        self.displayable_message = displayable_message

    @property
    def error_schema(self):
        return {
            "code": self.code,
            "message": self.message,
            "details": self.details,
            "location": self.location,
            "parameter": self.parameter,
            "displayable_message": self.displayable_message,
        }


class DefaultError(BaseError):
    code: str = "UNEXPECTED_ERROR"
    message: str = "An unexpected error occurred. Please try again."
    http_status = 500


class IllegalCharactersError(BaseError):
    code: str = "ILLEGAL_CHARACTERS"
    message: str = "There is an invalid or unexpected character."
    http_status = 422


class InvalidParameterError(BaseError):
    code: str = "INVALID_PARAMETER"
    message: str = "A value provided as parameter is not valid for the request."
    http_status = 422


class MissingParameterError(BaseError):
    code: str = "MISSING_PARAMETER"
    message: str = "The request is missing a required parameter."
    http_status = 422


class NotFoundError(BaseError):
    code: str = "NOT_FOUND"
    message: str = "The specified resource was not found."
    http_status = 404


class ForbiddenError(BaseError):
    code: str = "FORBIDDEN"
    message: str = "The request has been understood but server refuses to authorize it."
    http_status = 403
