from ..responses import RetrieveArtifactResponse
from ..utils import validate_non_empty_string

class RetrieveArtifactMixin:
    def retrieve_artifact(self, repo_key: str, path: str) -> RetrieveArtifactResponse:
        """
        Retrieve an artifact from Artifactory.

        GET /artifactory/{repo_key}/{path}

        Args:
            repo_key: The repository key.
            path: The path to the artifact.

        Returns:
            RetrieveArtifactResponse with artifact content.

        Raises:
            InvalidArgumentError: If repo_key or path is empty/None.
        """

        validate_non_empty_string(repo_key, "repo_key")
        validate_non_empty_string(path, "path")

        url = f"{self.host}artifactory/{repo_key}/{path}"
        response = self.session.get(url, timeout=self.timeout)
        return self._handle_response(response, RetrieveArtifactResponse, success_code=200)
