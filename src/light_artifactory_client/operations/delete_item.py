from ..responses import DeleteItemResponse
from ..utils import validate_non_empty_string

class DeleteItemMixin:
    def delete_item(self, repo_key: str, path: str) -> DeleteItemResponse:
        """Delete an item (file or folder) from Artifactory.

        DELETE /artifactory/{repo_key}/{path}

        Args:
            repo_key: The repository key.
            path: The path to the item to delete.

        Raises:
            InvalidArgumentError: If repo_key or path is empty/None.
        """

        validate_non_empty_string(repo_key, "repo_key")
        validate_non_empty_string(path, "path")

        url = f"{self.host}artifactory/{repo_key}/{path}"
        response = self.session.delete(url, timeout=self.timeout)
        return self._handle_response(response, DeleteItemResponse, success_code=204)
