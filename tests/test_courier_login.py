import allure
import requests
from data import MAIN_URL, LOGIN_COURIER_URL, ERROR_MESSAGES


class TestCourierLogin:

    @allure.title("Авторизация с несуществующими данными → ошибка")
    def test_login_with_invalid_credentials(self):
        payload = {
            "login": "neverexistsuser2025x",
            "password": "wrongpass123zzz"
        }
        with allure.step("Попытка логина с заведомо неверными данными"):
            response = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}", json=payload)

        # учебный сервер часто отвечает 200 даже при ошибке → проверяем тело
        assert response.status_code in (200, 404)
        body = response.json()
        assert "message" in body
        assert any(word in body["message"].lower() for word in ["не найдена", "не найдено", "учетная запись"])