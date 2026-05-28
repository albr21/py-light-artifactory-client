from ..responses import SearchAQLResponse

class SearchAQLMixin:
    """Mixin providing the search_aql operation."""

    def search_aql(self, query: str) -> SearchAQLResponse:
        """Execute an AQL (Artifactory Query Language) search.

        POST /artifactory/api/search/aql

        Args:
            query: The AQL query string.

        Returns:
            SearchAQLResponse with search results.
        """

        url = f"{self.host}artifactory/api/search/aql"
        headers = {"Content-Type": "text/plain", "Accept": "application/json"}
        response = self.session.post(url, data=query, headers=headers, timeout=self.timeout)
        return self._handle_response(response, SearchAQLResponse, success_code=200)
