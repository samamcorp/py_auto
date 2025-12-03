import allure


@allure.step("Appeler GET {path}")
def step_get(api_client, path: str):
    """
    Step Allure pour encapsuler un appel GET.
    """
    return api_client.get(path)