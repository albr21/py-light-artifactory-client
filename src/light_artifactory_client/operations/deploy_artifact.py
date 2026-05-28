from ..responses import DeployArtifactResponse
from ..utils import to_matrix_properties, validate_non_empty_string

class DeployArtifactMixin:
    def deploy_artifact(
        self,
        repo_key: str,
        path: str,
        content: bytes | str,
        *,
        properties: dict[str, str | list[str]] | None = None,
        checksums: dict[str, str] | None = None,
    ) -> DeployArtifactResponse:
        """
        Deploy (upload) an artifact to Artifactory.

        PUT /artifactory/{repo_key}/{path}{;properties}

        Args:
            repo_key: The repository key.
            path: The target path within the repository.
            content: The artifact content (bytes or string).
            properties: Optional matrix properties to attach.
            checksums: Optional checksums dict with keys: sha1, sha256, md5.

        Returns:
            DeployArtifactResponse on success.

        Raises:
            InvalidArgumentError: For invalid arguments.
        """

        validate_non_empty_string(repo_key, "repo_key")
        validate_non_empty_string(path, "path")

        matrix_props = to_matrix_properties(properties) if properties else ""
        url = f"{self.host}artifactory/{repo_key}/{path}{matrix_props}"

        headers: dict[str, str] = {"Content-Type": "application/octet-stream"}
        if checksums:
            if "sha1" in checksums:
                headers["X-Checksum-Sha1"] = checksums["sha1"]
            if "sha256" in checksums:
                headers["X-Checksum-Sha256"] = checksums["sha256"]
            if "md5" in checksums:
                headers["X-Checksum-Md5"] = checksums["md5"]

        response = self.session.put(url, data=content, headers=headers, timeout=self.timeout)
        return self._handle_response(response, DeployArtifactResponse, success_code=201)
