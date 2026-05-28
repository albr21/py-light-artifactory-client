from ..responses import ListItemsResponse
from ..utils import validate_non_empty_string
from ..exceptions import InvalidArgumentError

class ListItemsMixin:
    def list_items(
        self,
        repo_key: str,
        path: str = "",
        *,
        deep: bool = False,
        depth: int | None = None,
        list_folders: bool = False,
        include_root: bool = False,
    ) -> ListItemsResponse:
        """
        List items (files) in a repository path.

        GET /artifactory/api/storage/{repo_key}/{path}?list

        Args:
            repo_key: The repository key.
            path: The path within the repository.
            deep: If True, list recursively.
            depth: Depth limit for recursive listing.
            list_folders: If True, include folders in the listing.
            include_root: If True, include the root folder.

        Returns:
            ListItemsResponse with the file listing.

        Raises:
            InvalidArgumentError: For invalid arguments.
        """

        validate_non_empty_string(repo_key, "repo_key")

        if not isinstance(deep, bool):
            raise InvalidArgumentError("deep must be a boolean")
        if not isinstance(list_folders, bool):
            raise InvalidArgumentError("list_folders must be a boolean")
        if not isinstance(include_root, bool):
            raise InvalidArgumentError("include_root must be a boolean")
        if depth is not None and (not isinstance(depth, int) or depth <= 0):
            raise InvalidArgumentError("depth must be None or a positive integer")

        params = (
            f"list&deep={1 if deep else 0}"
            f"&listFolders={1 if list_folders else 0}"
            f"&includeRoot={1 if include_root else 0}"
        )
        if depth is not None:
            params += f"&depth={depth}"

        url = f"{self.host}artifactory/api/storage/{repo_key}/{path}?{params}"
        response = self.session.get(url, timeout=self.timeout)
        return self._handle_response(response, ListItemsResponse, success_code=200)
