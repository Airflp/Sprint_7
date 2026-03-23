import pytest
import requests
<<<<<<< HEAD
import allure

from data import MAIN_URL, CREATE_COURIER_URL, LOGIN_COURIER_URL
from helpers import generate_login, generate_password, generate_first_name


@pytest.fixture(scope="function")
@allure.step("Создание курьера + автоматическая очистка")
def create_courier(request):
    """Возвращает словарь сразу (без yield). Очистка через addfinalizer."""
    payload = {
        "login": generate_login(),
        "password": generate_password(),
        "firstName": generate_first_name()
    }

    # Создаём курьера
    requests.post(f"{MAIN_URL}{CREATE_COURIER_URL}", json=payload)

    # Получаем id
    login_resp = requests.post(
        f"{MAIN_URL}{LOGIN_COURIER_URL}",
        json={"login": payload["login"], "password": payload["password"]}
    )

    courier_id = login_resp.json().get("id") if login_resp.status_code == 200 else None

    courier_info = {
        "login": payload["login"],
        "password": payload["password"],
        "firstName": payload["firstName"],
        "id": courier_id
    }

    # Очистка после теста
    def cleanup():
        if courier_info["id"]:
            requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}/{courier_info['id']}")

    request.addfinalizer(cleanup)

    return courier_info
=======

from data import MAIN_URL, LOGIN, PASSWORD, CREATE_COURIER_URL, LOGIN_COURIER_URL, FIRST_NAME


@pytest.fixture()
def delete_courier():
    yield
    # Получить id курьера
    payload = {"login": LOGIN, "password": PASSWORD}
    response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)
    id_courier = response.json()['id']

    # Удалить курьера, который был создан
    requests.delete(f'{MAIN_URL}{CREATE_COURIER_URL}/{id_courier}')


@pytest.fixture()
def create_courier():
    # Создать нового курьера
    payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
    requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4
