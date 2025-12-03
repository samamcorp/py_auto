import httpx
from allure_commons.types import AttachmentType
import allure

from .config import get_settings


class ApiClient:
    """
    HTTP client based on httpx.
    Central entry point for all API calls.
    """

    def __init__(self, base_url: str | None = None, timeout: float | None = None):
        settings = get_settings()
        self.base_url = base_url or settings.base_url
        self.timeout = timeout or settings.timeout

        self._client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
        )

    @allure.step("GET {path}")
    def get(self, path: str, **kwargs) -> httpx.Response:
        """
        Send a GET request and log it in Allure.
        """
        response = self._client.get(path, **kwargs)
        self._attach_response("GET", path, response)
        return response

    @allure.step("POST {path}")
    def post(self, path: str, json: dict | None = None, **kwargs) -> httpx.Response:
        """
        Send a POST request and log it in Allure.
        """
        response = self._client.post(path, json=json, **kwargs)
        self._attach_response("POST", path, response)
        return response

    @allure.step("PUT {path}")
    def put(self, path: str, json: dict | None = None, **kwargs) -> httpx.Response:
        """
        Send a PUT request and log it in Allure.
        """
        response = self._client.put(path, json=json, **kwargs)
        self._attach_response("PUT", path, response)
        return response

    @allure.step("DELETE {path}")
    def delete(self, path: str, **kwargs) -> httpx.Response:
        """
        Send a DELETE request and log it in Allure.
        """
        response = self._client.delete(path, **kwargs)
        self._attach_response("DELETE", path, response)
        return response

    def close(self) -> None:
        self._client.close()

    def _attach_response(self, method: str, path: str, response: httpx.Response) -> None:
        """
        Attach basic request/response info into Allure report.
        """
        info = (
            f"{method} {path}\n"
            f"URL: {response.url}\n"
            f"Status: {response.status_code}\n"
            f"Headers:\n{response.headers}\n"
        )

        # Attach request/response info
        allure.attach(
            info,
            name="Request / response info",
            attachment_type=AttachmentType.TEXT,
        )

        # Attach response body (as TEXT to be safe)
        allure.attach(
            response.text,
            name="Response body",
            attachment_type=AttachmentType.TEXT,
        )