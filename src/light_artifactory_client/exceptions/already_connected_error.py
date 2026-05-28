from .error import LightArtifactoryClientError

class AlreadyConnectedError(LightArtifactoryClientError):
    """Exception raised when attempting to connect while already connected."""

    def __init__(self) -> None:
        super().__init__("Already connected. Disconnect first or set force=True.")
