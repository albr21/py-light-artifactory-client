from __future__ import annotations
from typing import Any
from .response import Response

class SearchItemsByPropertiesResponse(Response):
    """Response for search_items_by_properties operation"""

    @property
    def results(self) -> list[dict[str, Any]]:
        """Return the list of results from the property search"""
        return self.json().get("results", [])
