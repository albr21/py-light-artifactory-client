from .error import LightArtifactoryClientError

class InvalidArgumentError(LightArtifactoryClientError):
    """Raised when an invalid argument is provided to a method."""
