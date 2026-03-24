import allure
import requests

from data import MAIN_URL, CREATE_COURIER_URL, LOGIN_COURIER_URL, ERROR_MESSAGES
from helpers import generate_first_name, generate_login, generate_password


class TestCreateCourier:

    @allure.title("Можно создать нового курьера")
    def test_create_courier_success(self):
        payload = {
            "login": generate_login(),
            "password": generate_password(),
            "firstName": generate_first_name()
        }

        with allure.step("Создание нового курьера"):
            response = requests.post(
                f"{MAIN_URL}{CREATE_COURIER_URL}",
                json=payload,
                timeout=10
            )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        with allure.step("Авторизация созданного курьера для получения id"):
            login_response = requests.post(
                f"{MAIN_URL}{LOGIN_COURIER_URL}",
                json={
                    "login": payload["login"],
                    "password": payload["password"]
                },
                timeout=10
            )
            courier_id = login_response.json().get("id")

        if courier_id:
            with allure.step("Удаление созданного курьера"):
                requests.delete(
                    f"{MAIN_URL}{CREATE_COURIER_URL}/{courier_id}",
                    timeout=10
                )

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_two_same_courier_returns_conflict(self):
        payload = {
            "login": generate_login(),
            "password": generate_password(),
            "firstName": generate_first_name()
        }

        with allure.step("Создание первого курьера"):
            first_response = requests.post(
                f"{MAIN_URL}{CREATE_COURIER_URL}",
                json=payload,
                timeout=10
            )

        assert first_response.status_code == 201

        with allure.step("Создание второго курьера с теми же данными"):
            second_response = requests.post(
                f"{MAIN_URL}{CREATE_COURIER_URL}",
                json=payload,
                timeout=10
            )

        assert second_response.status_code == 409
        assert second_response.json() == ERROR_MESSAGES["LOGIN_ALREADY_EXISTS"]

        with allure.step("Авторизация первого курьера для получения id"):
            login_response = requests.post(
                f"{MAIN_URL}{LOGIN_COURIER_URL}",
                json={
                    "login": payload["login"],
                    "password": payload["password"]
                },
                timeout=10
            )
            courier_id = login_response.json().get("id")

        if courier_id:
            with allure.step("Удаление тестового курьера"):
                requests.delete(
                    f"{MAIN_URL}{CREATE_COURIER_URL}/{courier_id}",
                    timeout=10
                )