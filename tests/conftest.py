import pytest
from framework.client import ApiClient


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    """
    API Client shared with all tests.
    Instanced once per session.
    """
    client = ApiClient()
    yield client
    client.close()