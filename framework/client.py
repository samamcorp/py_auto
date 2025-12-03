import httpx
from .config import get_settings


class ApiClient:
    """
    HTTP client based on httpx.
    For API calls.
    """

    def __init__(self, base_url: str | None = None, timeout: float | None = None):
        settings = get_settings()
        self.base_url = base_url or settings.base_url
        self.timeout = timeout or settings.timeout

        self._client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
        )

    def get(self, path: str, **kwargs) -> httpx.Response:
        return self._client.get(path, **kwargs)

    def post(self, path: str, json: dict | None = None, **kwargs) -> httpx.Response:
        return self._client.post(path, json=json, **kwargs)

    def close(self) -> None:
        self._client.close()