from ..responses import SearchItemsByPropertiesResponse
from ..utils import to_query_properties
from ..exceptions import InvalidArgumentError

class SearchItemsByPropertiesMixin:
    def search_items_by_properties(
        self,
        properties: dict[str, str],
        *,
        repos: str | None = None,
        x_result_detail: str | None = None,
    ) -> SearchItemsByPropertiesResponse:
        """Search for items by their properties.

        GET /artifactory/api/search/prop?{properties}

        Args:
            properties: Dictionary of property key-value pairs to search for.
            repos: Optional repository name to limit the search.
            x_result_detail: Optional result detail level.
                Valid values: "info", "properties", "info, properties".

        Returns:
            SearchItemsByPropertiesResponse with search results.

        Raises:
            InvalidArgumentError: For invalid arguments.
        """

        if not isinstance(properties, dict):
            raise InvalidArgumentError("properties must be a dict")

        valid_details = {"info", "properties", "info, properties"}
        if x_result_detail is not None and x_result_detail not in valid_details:
            raise InvalidArgumentError(f"x_result_detail must be one of: {valid_details}")

        aggregated_properties = dict(properties)
        if repos:
            aggregated_properties["repos"] = repos

        query_string = to_query_properties(aggregated_properties)
        url = f"{self.host}artifactory/api/search/prop{query_string}"

        headers: dict[str, str] = {}
        if x_result_detail:
            headers["X-Result-Detail"] = x_result_detail

        response = self.session.get(url, headers=headers, timeout=self.timeout)
        return self._handle_response(response, SearchItemsByPropertiesResponse, success_code=200)
