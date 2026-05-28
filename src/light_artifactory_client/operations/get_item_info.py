from ..responses import GetItemInfoResponse
from ..utils import validate_non_empty_string

class GetItemInfoMixin:
    def get_item_info(self, repo_key: str, path: str) -> GetItemInfoResponse:
        """
        Get metadata information for an item (file or folder).

        GET /artifactory/api/storage/{repo_key}/{path}

        Args:
            repo_key: The repository key.
            path: The path within the repository.

        Returns:
            GetItemInfoResponse with item metadata.

        Raises:
            InvalidArgumentError: If repo_key or path is empty/None.
        """

        validate_non_empty_string(repo_key, "repo_key")
        validate_non_empty_string(path, "path")

        url = f"{self.host}artifactory/api/storage/{repo_key}/{path}"
        response = self.session.get(url, timeout=self.timeout)
        return self._handle_response(response, GetItemInfoResponse, success_code=200)
