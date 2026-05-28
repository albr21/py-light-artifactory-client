import pytest

from light_artifactory_client import ArtifactoryClient

SERVER_URL = "https://artifactory.example.com/"

@pytest.fixture
def client():
    return ArtifactoryClient(SERVER_URL)

@pytest.fixture
def authed_client():
    return ArtifactoryClient(SERVER_URL, username="user", password="pass")
