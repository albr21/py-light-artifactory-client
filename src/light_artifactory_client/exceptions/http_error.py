from .error import LightArtifactoryClientError

class HTTPError(LightArtifactoryClientError):
    """Base exception for all Light Artifactory Client HTTP errors"""

    def __init__(self, status_code: int, body: str):
        self.status_code = status_code
        self.body = body
        super().__init__(f"HTTP {status_code}: {body}")
