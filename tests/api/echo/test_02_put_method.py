import allure


@allure.feature("Echo API")
@allure.story("PUT /put")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("02 — PUT method should echo updated JSON payload successfully")
def test_02_put_method(api_client):
    """
    Verifies that the PUT /put endpoint echoes back the JSON payload sent.
    """
    payload = {"status": "updated"}

    response = api_client.put("/put", json=payload)

    with allure.step("Check status code"):
        assert response.status_code == 200

    body = response.json()

    with allure.step("Check response contains the updated JSON we sent"):
        assert body["json"] == payload