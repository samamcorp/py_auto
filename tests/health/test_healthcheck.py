import allure


@allure.feature("Healthcheck")
@allure.story("GET /get")
def test_healthcheck_get(api_client):
    response = api_client.get("/get")

    with allure.step("Check the status code"):
        assert response.status_code == 200

    body = response.json()

    with allure.step("Check the 'url' field exists"):
        assert "url" in body

    with allure.step("Check the URL starts with base"):
        assert body["url"].startswith("https://postman-echo.com")