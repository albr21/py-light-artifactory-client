from __future__ import annotations
from typing import Any
from .response import Response

class SearchAQLResponse(Response):
    """Response for search_aql operation"""

    @property
    def results(self) -> list[dict[str, Any]]:
        """Return the list of results from the AQL query"""
        return self.json().get("results", [])
