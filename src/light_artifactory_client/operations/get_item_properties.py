from ..responses import GetItemPropertiesResponse
from ..utils import validate_non_empty_string

class GetItemPropertiesMixin:
    def get_item_properties(self, repo_key: str, path: str) -> GetItemPropertiesResponse:
        """
        Get properties of an item.

        GET /artifactory/api/storage/{repo_key}/{path}?properties

        Args:
            repo_key: The repository key.
            path: The path within the repository.

        Returns:
            GetItemPropertiesResponse with item properties.

        Raises:
            InvalidArgumentError: If repo_key or path is empty/None.
        """

        validate_non_empty_string(repo_key, "repo_key")
        validate_non_empty_string(path, "path")

        url = f"{self.host}artifactory/api/storage/{repo_key}/{path}?properties"
        response = self.session.get(url, timeout=self.timeout)
        return self._handle_response(response, GetItemPropertiesResponse, success_code=200)
