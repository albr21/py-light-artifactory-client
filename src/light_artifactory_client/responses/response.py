from __future__ import annotations
import json
from typing import Any


class Response:
    """Base response wrapper around HTTP response data"""

    def __init__(self, status_code: int, body: str, headers: dict[str, str] | None = None) -> None:
        self.status_code = status_code
        self.body = body
        self.headers = {} if headers is None else headers

    def json(self) -> Any:
        """Parse body as JSON."""
        return json.loads(self.body)
