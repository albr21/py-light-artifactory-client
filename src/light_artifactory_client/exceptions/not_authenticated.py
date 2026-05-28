from .http_error import HTTPError

class NotAuthenticatedError(HTTPError):
    """Raised when the request is not authenticated (HTTP 401)"""

    def __init__(self, message: str = "Not authenticated") -> None:
        super().__init__(401, message)
