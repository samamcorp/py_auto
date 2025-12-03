import allure


@allure.feature("Echo API")
@allure.story("POST /post")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("01 — POST method should echo JSON payload successfully")
def test_01_post_method(api_client):
    """
    Verifies that the POST /post endpoint echoes back the JSON payload sent.
    """
    payload = {"name": "Samuel", "age": 40}

    response = api_client.post("/post", json=payload)

    with allure.step("Check status code"):
        assert response.status_code == 200

    body = response.json()

    with allure.step("Check response contains the JSON we sent"):
        assert body["json"] == payload