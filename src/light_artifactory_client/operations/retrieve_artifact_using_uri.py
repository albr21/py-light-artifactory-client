from ..responses import RetrieveArtifactUsingUriResponse
from ..exceptions import InvalidArgumentError

class RetrieveArtifactUsingUriMixin:
    def retrieve_artifact_using_uri(self, uri: str) -> RetrieveArtifactUsingUriResponse:
        """
        Retrieve an artifact using its full URI.

        GET {uri}

        Args:
            uri: The full URI of the artifact (must start with http:// or https://
                 and contain 'artifactory').

        Returns:
            RetrieveArtifactUsingUriResponse with artifact content.

        Raises:
            InvalidArgumentError: If the URI is invalid.
        """

        if not uri:
            raise InvalidArgumentError("uri is required")
        if not isinstance(uri, str):
            raise InvalidArgumentError("uri must be a string")
        if not (uri.startswith("http://") or uri.startswith("https://")):
            raise InvalidArgumentError("uri must start with http:// or https://")
        if "artifactory" not in uri:
            raise InvalidArgumentError("uri must contain 'artifactory'")

        response = self.session.get(uri, timeout=self.timeout)
        return self._handle_response(response, RetrieveArtifactUsingUriResponse, success_code=200)
