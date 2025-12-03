def test_healthcheck_get(api_client):
    """
    Simple test to check the API answers.
    """
    response = api_client.get("/get")

    assert response.status_code == 200
    body = response.json()

    assert "url" in body
