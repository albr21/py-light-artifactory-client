from .http_error import HTTPError

class ForbiddenError(HTTPError):
    """Raised when the request is forbidden (HTTP 403)"""

    def __init__(self, message: str = "Forbidden") -> None:
        super().__init__(403, message)
