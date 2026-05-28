from __future__ import annotations
from typing import Any
from .response import Response

class ListItemsResponse(Response):
    """Response for list_items operation"""

    @property
    def items(self) -> list[dict[str, Any]]:
        """Return the list of files from the response"""
        return self.json().get("files", [])
