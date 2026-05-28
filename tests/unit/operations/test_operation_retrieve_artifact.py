import pytest

from unittest.mock import MagicMock

from light_artifactory_client import NotFoundError
from light_artifactory_client.exceptions import InvalidArgumentError
from light_artifactory_client.responses import RetrieveArtifactResponse

from .conftest import mock_response
from .conftest import SERVER_URL

class TestOperationRetrieveArtifact:
    def test_operation_retrieve_artifact_success(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, "binary data"))

        result = client.retrieve_artifact("repo", "org/artifact.jar")

        assert isinstance(result, RetrieveArtifactResponse)
        assert result.body == "binary data"

    def test_operation_retrieve_artifact_empty_repo_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.retrieve_artifact("", "path")

    def test_operation_retrieve_artifact_empty_path_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.retrieve_artifact("repo", "")

    def test_operation_retrieve_artifact_url_construction(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, "data"))
        client.retrieve_artifact("libs-release", "com/example/file.jar")
        called_url = client.session.get.call_args[0][0]
        assert called_url == f"{SERVER_URL}artifactory/libs-release/com/example/file.jar"

    def test_operation_retrieve_artifact_404_raises(self, client):
        client.session.get = MagicMock(return_value=mock_response(404))
        with pytest.raises(NotFoundError):
            client.retrieve_artifact("repo", "path")
