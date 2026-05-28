from .http_error import HTTPError

class NotFoundError(HTTPError):
    """Raised when the resource is not found (HTTP 404)"""

    def __init__(self, message: str = "Not found") -> None:
        super().__init__(404, message)