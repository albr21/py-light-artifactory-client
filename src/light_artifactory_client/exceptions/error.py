class LightArtifactoryClientError(Exception):
    """Base exception for all Light Artifactory Client errors"""

    def __init__(self, message: str):
        super().__init__(message)
