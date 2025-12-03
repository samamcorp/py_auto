import allure


@allure.feature("Echo API")
@allure.story("DELETE /delete")
@allure.severity(allure.severity_level.MINOR)
@allure.title("03 — DELETE method should succeed")
def test_03_delete_method(api_client):
    """
    Verifies that the DELETE /delete endpoint responds successfully.
    """
    response = api_client.delete("/delete")

    with allure.step("Check status code"):
        assert response.status_code in (200, 204)