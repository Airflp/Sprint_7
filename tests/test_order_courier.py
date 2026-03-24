import allure
import pytest
import requests

from data import MAIN_URL, LOGIN_COURIER_URL, ERROR_MESSAGES
from helpers import generate_login, generate_password


class TestLoginCourier:

    @allure.title("Успешный логин курьера возвращает id")
    def test_login_courier_success_return_id(self, new_create_courier):
        payload = {
            "login": new_create_courier["login"],
            "password": new_create_courier["password"]
        }

        with allure.step("Логин существующего курьера"):
            response = requests.post(
                f"{MAIN_URL}{LOGIN_COURIER_URL}",
                json=payload,
                timeout=10
            )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин существующего курьера с неверным паролем возвращает ошибку")
    def test_login_existing_courier_with_wrong_password(self, new_create_courier):
        payload = {
            "login": new_create_courier["login"],
            "password": generate_password()
        }

        with allure.step("Логин существующего пользователя с неверным паролем"):
            response = requests.post(
                f"{MAIN_URL}{LOGIN_COURIER_URL}",
                json=payload,
                timeout=10
            )

        assert response.status_code == 404
        assert response.json() == ERROR_MESSAGES["LOGIN_FAILED"]

    @allure.title("Логин несуществующего пользователя возвращает ошибку")
    def test_login_non_existent_user(self):
        payload = {
            "login": generate_login(),
            "password": generate_password()
        }

        with allure.step("Логин полностью несуществующего пользователя"):
            response = requests.post(
                f"{MAIN_URL}{LOGIN_COURIER_URL}",
                json=payload,
                timeout=10
            )

        assert response.status_code == 404
        assert response.json() == ERROR_MESSAGES["LOGIN_FAILED"]

    @allure.title("Логин без логина или пароля возвращает ошибку 400")
    @pytest.mark.parametrize(
        "login_value,password_value",
        [
            ("", generate_password()),
            (generate_login(), ""),
            ("", "")
        ]
    )
    def test_login_without_login_or_password(self, login_value, password_value):
        payload = {
            "login": login_value,
            "password": password_value
        }

        with allure.step(
            f"Логин без обязательных данных: login={login_value}, password={password_value}"
        ):
            response = requests.post(
                f"{MAIN_URL}{LOGIN_COURIER_URL}",
                json=payload,
                timeout=10
            )

        assert response.status_code == 400
        assert response.json() == ERROR_MESSAGES["LOGIN_INSUFFICIENT_DATA"]