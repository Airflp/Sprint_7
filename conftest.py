import pytest
import requests

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