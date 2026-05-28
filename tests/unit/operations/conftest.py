import pytest

from unittest.mock import MagicMock
from light_artifactory_client import ArtifactoryClient

SERVER_URL = "https://artifactory.example.com/"

def mock_response(status_code: int, body: str = "", headers: dict | None = None) -> MagicMock:
    resp = MagicMock()
    resp.status_code = status_code
    resp.text = body
    resp.headers = headers or {}
    return resp

@pytest.fixture
def client():
    return ArtifactoryClient(SERVER_URL, username="user", password="pass")
