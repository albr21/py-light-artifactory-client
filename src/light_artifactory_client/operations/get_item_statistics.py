from ..responses import GetItemStatisticsResponse
from ..utils import validate_non_empty_string

class GetItemStatisticsMixin:
    def get_item_statistics(self, repo_key: str, path: str) -> GetItemStatisticsResponse:
        """
        Get download statistics for an item.

        GET /artifactory/api/storage/{repo_key}/{path}?stats

        Args:
            repo_key: The repository key.
            path: The path within the repository (must not be empty).

        Returns:
            GetItemStatisticsResponse with statistics.

        Raises:
            InvalidArgumentError: If repo_key or path is empty/None.
        """

        validate_non_empty_string(repo_key, "repo_key")
        validate_non_empty_string(path, "path")

        url = f"{self.host}artifactory/api/storage/{repo_key}/{path}?stats"
        response = self.session.get(url, timeout=self.timeout)
        return self._handle_response(response, GetItemStatisticsResponse, success_code=200)
