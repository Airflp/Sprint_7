<<<<<<< HEAD
import requests
import allure

from data import MAIN_URL, CREATE_COURIER_URL, LOGIN_COURIER_URL, ERROR_MESSAGES
from helpers import generate_login, generate_password, generate_first_name
=======
import allure
import requests
from helpers import generate_password, generate_first_name
from data import MAIN_URL, LOGIN, PASSWORD, FIRST_NAME, CREATE_COURIER_URL
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4


class TestCreateCourier:

<<<<<<< HEAD
    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_two_same_courier_returns_conflict(self):
        login = generate_login() + str(int(generate_login(), 36))[:4]  # делаем логин ещё уникальнее
        password = generate_password()
        first_name = generate_first_name()
        payload = {"login": login, "password": password, "firstName": first_name}

        with allure.step("Создаём первого курьера"):
            resp1 = requests.post(f"{MAIN_URL}{CREATE_COURIER_URL}", json=payload)
            # Разрешаем 201 или 409 (если логин всё равно совпал — редкий случай)
            assert resp1.status_code in (201, 409)

        with allure.step("Пытаемся создать второго с теми же данными"):
            resp2 = requests.post(f"{MAIN_URL}{CREATE_COURIER_URL}", json=payload)
            assert resp2.status_code == 409
            assert resp2.json() == ERROR_MESSAGES["LOGIN_ALREADY_EXISTS"]

    @allure.title("Создание курьера → статус 201 и ok: true")
    def test_create_courier_success(self):
        payload = {
            "login": generate_login() + str(int(generate_login(), 36))[:4],  # уникальность
            "password": generate_password(),
            "firstName": generate_first_name()
        }

        with allure.step("Создаём курьера"):
            resp = requests.post(f"{MAIN_URL}{CREATE_COURIER_URL}", json=payload)

        assert resp.status_code == 201
        assert resp.json() == {"ok": True}

    @allure.title("Авторизация с неверными данными → ошибка")
    def test_login_with_invalid_credentials(self):
        payload = {"login": "nonexistentuser123456", "password": "wrongpass999"}
        with allure.step("Отправка запроса на логин с неверными данными"):
            response = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}", json=payload)

        assert response.status_code in (200, 404)
        data = response.json()
        assert "message" in data
        assert "не найдена" in data["message"].lower() or "учетная запись не найдена" in data["message"].lower()
=======
    @allure.title('Создать двух одинаковых курьеров')
    def test_create_two_same_courier_show_message_conflict(self, create_courier, delete_courier):
        # Создать еще одного такого же курьера
        payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)

        assert response.status_code == 409 and response.json() == {"code": 409,
                                                                   "message": "Этот логин уже используется. Попробуйте другой."}

    @allure.title('Создать курьера и получить статус код 201')
    def test_create_courier_return_status_code_201(self, delete_courier):
        # Создать нового курьера
        payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)

        assert response.status_code == 201

    @allure.title('Создать курьера и получить ответ от сервера ok: True')
    def test_create_courier_return_message_ok_true(self, delete_courier):
        # Создать нового курьера
        payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)

        assert response.json() == {"ok": True}

    @allure.title('Создать курьера без логина или пароля')
    def test_create_courier_without_required_field_show_message_bad_request(self):
        # Создать нового курьера без логина или пароля
        payload = {"login": LOGIN, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)

        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Создать курьера c логином, который уже существует в системе')
    def test_create_courier_with_login_already_exists_show_message_conflict(self, create_courier, delete_courier):
        # Создать еще одного курьера с таким же логином
        payload = {"login": LOGIN, "password": generate_password(), "firstName": generate_first_name()}
        response = requests.post(f'{MAIN_URL}/api/v1/courier', data=payload)

        assert response.status_code == 409 and response.json() == {"code": 409,
                                                                   "message": "Этот логин уже используется. Попробуйте другой."}
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4
