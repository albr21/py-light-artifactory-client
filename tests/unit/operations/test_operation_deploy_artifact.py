import json
import pytest

from unittest.mock import MagicMock

from light_artifactory_client import ForbiddenError, NotAuthenticatedError
from light_artifactory_client.exceptions import InvalidArgumentError
from light_artifactory_client.responses import DeployArtifactResponse

from .conftest import mock_response

class TestOperationDeployArtifact:
    def test_operation_deploy_artifact_success(self, client):
        body = json.dumps({"repo": "libs-release", "path": "/artifact.jar"})
        client.session.put = MagicMock(return_value=mock_response(201, body))

        result = client.deploy_artifact("libs-release", "org/artifact.jar", b"binary content")

        assert isinstance(result, DeployArtifactResponse)
        assert result.status_code == 201

    def test_operation_deploy_artifact_empty_repo_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.deploy_artifact("", "path", b"content")

    def test_operation_deploy_artifact_empty_path_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.deploy_artifact("repo", "", b"content")

    def test_operation_deploy_artifact_with_properties_in_url(self, client):
        client.session.put = MagicMock(return_value=mock_response(201, "{}"))
        client.deploy_artifact("repo", "path/file.jar", b"data", properties={"build": "1"})
        called_url = client.session.put.call_args[0][0]
        assert ";build=1" in called_url

    def test_operation_deploy_artifact_sha1_checksum_header(self, client):
        client.session.put = MagicMock(return_value=mock_response(201, "{}"))
        client.deploy_artifact("repo", "file.jar", b"data", checksums={"sha1": "abc123", "md5": "def456"})
        headers = client.session.put.call_args[1]["headers"]
        assert headers["X-Checksum-Sha1"] == "abc123"
        assert headers["X-Checksum-Md5"] == "def456"

    def test_operation_deploy_artifact_sha256_checksum_header(self, client):
        client.session.put = MagicMock(return_value=mock_response(201, "{}"))
        client.deploy_artifact("repo", "file.jar", b"data", checksums={"sha256": "xyz789"})
        headers = client.session.put.call_args[1]["headers"]
        assert headers["X-Checksum-Sha256"] == "xyz789"

    def test_operation_deploy_artifact_content_type_header(self, client):
        client.session.put = MagicMock(return_value=mock_response(201, "{}"))
        client.deploy_artifact("repo", "file.jar", b"data")
        headers = client.session.put.call_args[1]["headers"]
        assert headers["Content-Type"] == "application/octet-stream"

    def test_operation_deploy_artifact_401_raises(self, client):
        client.session.put = MagicMock(return_value=mock_response(401))
        with pytest.raises(NotAuthenticatedError):
            client.deploy_artifact("repo", "path", b"content")

    def test_operation_deploy_artifact_403_raises(self, client):
        client.session.put = MagicMock(return_value=mock_response(403))
        with pytest.raises(ForbiddenError):
            client.deploy_artifact("repo", "path", b"content")
