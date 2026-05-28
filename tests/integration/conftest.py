import os
import pytest

from light_artifactory_client import ArtifactoryClient, NotFoundError

ARTIFACT_PATH = "test-artifact.txt"
ARTIFACT_CONTENT = b"integration test content"

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "integration: marks tests as integration tests (run with --integration)",
    )

def pytest_addoption(parser):
    parser.addoption(
        "--integration",
        action="store_true",
        default=False,
        help="Run integration tests against a real Artifactory server",
    )

def pytest_collection_modifyitems(config, items):
    if not config.getoption("--integration"):
        skip_integration = pytest.mark.skip(reason="Pass --integration to run")
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skip_integration)

@pytest.fixture(scope="session")
def integration_client():
    host = os.environ.get("ARTIFACTORY_URL", "http://localhost:8081/artifactory")
    username = os.environ.get("ARTIFACTORY_USER", "admin")
    password = os.environ.get("ARTIFACTORY_PASSWORD", "password")
    return ArtifactoryClient(host, username=username, password=password)

@pytest.fixture(scope="session")
def integration_repo():
    return os.environ.get("ARTIFACTORY_REPO", "libs-release-local")

@pytest.fixture(scope="session")
def deployed_artifact(integration_client, integration_repo):
    integration_client.deploy_artifact(
        integration_repo,
        ARTIFACT_PATH,
        ARTIFACT_CONTENT,
        properties={"test.source": "integration"},
    )
    yield integration_repo, ARTIFACT_PATH
    try:
        integration_client.delete_item(integration_repo, ARTIFACT_PATH)
    except NotFoundError:
        pass
