from __future__ import annotations
from typing import Any
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from .exceptions import (
    AlreadyConnectedError,
    HTTPError,
    ForbiddenError,
    NotAuthenticatedError,
    NotFoundError
)
from .operations import (
    DeleteItemMixin,
    DeployArtifactMixin,
    GetItemInfoMixin,
    GetItemPropertiesMixin,
    GetItemStatisticsMixin,
    ListItemsMixin,
    RetrieveArtifactMixin,
    RetrieveArtifactUsingUriMixin,
    SearchAQLMixin,
    SearchItemsByPropertiesMixin,
)
from .utils import ensure_trailing_slash

class ArtifactoryClient(
    GetItemInfoMixin,
    GetItemPropertiesMixin,
    GetItemStatisticsMixin,
    ListItemsMixin,
    DeployArtifactMixin,
    RetrieveArtifactMixin,
    RetrieveArtifactUsingUriMixin,
    DeleteItemMixin,
    SearchAQLMixin,
    SearchItemsByPropertiesMixin,
):
    """
    A lightweight REST API client for JFrog Artifactory.

    Operations are provided by mixin classes, each in its own module under
    the `operations` package. This allows easy extension and isolation of concerns.
    """

    def __init__(
        self,
        host: str,
        username: str | None = None,
        password: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 3,
        retry_backoff_factor: float = 0.5,
    ):
        self.host = ensure_trailing_slash(host)
        self.username: str | None = None
        self.password: str | None = None
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_backoff_factor = retry_backoff_factor
        self.session = self._create_session()

        if username and password:
            self.login(username, password)

    def _create_session(self) -> requests.Session:
        """Create a requests session with retry strategy."""
        session = requests.Session()
        retry_strategy = Retry(
            total=self.max_retries,
            backoff_factor=self.retry_backoff_factor,
            status_forcelist=[502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    @property
    def is_logged(self) -> bool:
        """Check if the client is logged in."""
        return self.session.auth is not None and self.username is not None and self.password is not None

    def login(self, username: str, password: str, force: bool = False) -> None:
        """
        Login to authenticate subsequent requests.

        Args:
            username: The username.
            password: The password or API key/token.
            force: If True, allow re-login without logout first.

        Raises:
            AlreadyConnectedError: If already logged in and force is False.
        """
        if self.is_logged and not force:
            raise AlreadyConnectedError()

        self.username = username
        self.password = password
        self.session.auth = (username, password)

    def logout(self) -> None:
        """Logout by clearing credentials."""
        self.username = None
        self.password = None
        self.session.auth = None

    def _handle_response(self, response: Any, response_class: type, success_code: int) -> Any:
        """
        Handle HTTP response and raise appropriate exceptions.

        Args:
            response: The requests.Response object.
            response_class: The response class to instantiate on success.
            success_code: The expected success HTTP status code.

        Returns:
            An instance of response_class on success.

        Raises:
            NotAuthenticatedError: On HTTP 401.
            ForbiddenError: On HTTP 403.
            NotFoundError: On HTTP 404.
            HTTPError: On any other non-success code.
        """
        status = response.status_code
        body = response.text

        if status == success_code:
            return response_class(
                status_code=status,
                body=body,
                headers=dict(response.headers),
            )

        if status == 401:
            raise NotAuthenticatedError(body)
        if status == 403:
            raise ForbiddenError(body)
        if status == 404:
            raise NotFoundError(body)

        raise HTTPError(status, body)
