import allure
import pytest
import requests

from data import MAIN_URL, CREATE_COURIER_URL, LOGIN_COURIER_URL
from helpers import generate_first_name, generate_login, generate_password


@pytest.fixture(scope="function")
def new_create_courier():
    with allure.step("Подготовка данных нового курьера"):
        payload = {
            "login": generate_login(),
            "password": generate_password(),
            "firstName": generate_first_name()
        }

    with allure.step("Создание курьера"):
        create_response = requests.post(
            f"{MAIN_URL}{CREATE_COURIER_URL}",
            json=payload,
            timeout=10
        )
        assert create_response.status_code == 201, (
            f"Не удалось создать курьера: "
            f"status={create_response.status_code}, body={create_response.text}"
        )

    with allure.step("Авторизация созданного курьера для получения id"):
        login_response = requests.post(
            f"{MAIN_URL}{LOGIN_COURIER_URL}",
            json={
                "login": payload["login"],
                "password": payload["password"]
            },
            timeout=10
        )
        assert login_response.status_code == 200, (
            f"Не удалось авторизовать созданного курьера: "
            f"status={login_response.status_code}, body={login_response.text}"
        )

        courier_id = login_response.json().get("id")
        assert courier_id is not None, (
            f"В ответе на логин отсутствует id: {login_response.text}"
        )

    courier_info = {
        "login": payload["login"],
        "password": payload["password"],
        "firstName": payload["firstName"],
        "id": courier_id
    }

    yield courier_info

    with allure.step("Удаление курьера после теста"):
        requests.delete(
            f"{MAIN_URL}{CREATE_COURIER_URL}/{courier_id}",
            timeout=10
        )