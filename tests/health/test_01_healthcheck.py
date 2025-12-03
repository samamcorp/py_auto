import allure


@allure.feature("Healthcheck")
@allure.story("GET /get")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("01 — Healthcheck endpoint should respond correctly")
def test_01_healthcheck(api_client):
    """
    Simple healthcheck test to ensure that the API is alive and reachable.
    Calls GET /get on Postman Echo and verifies the basic response integrity.
    """
    response = api_client.get("/get")

    with allure.step("Check status code"):
        assert response.status_code == 200

    body = response.json()

    with allure.step("Check 'url' field is present"):
        assert "url" in body

    with allure.step("Check the URL begins with expected base"):
        assert body["url"].startswith("https://postman-echo.com")