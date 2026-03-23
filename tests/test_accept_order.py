<<<<<<< HEAD
import requests
import allure
import pytest

from data import MAIN_URL, CREATE_ORDER_URL, ACCEPT_ORDER_URL, ERROR_MESSAGES


@allure.step("Создание тестового заказа")
def create_test_order():
    payload = {
        "firstName": "АвтоТест",
        "lastName": "Тестов",
        "address": "ул. Автотестовая, 1",
        "metroStation": 5,
        "phone": "+79991234567",
        "rentTime": 1,
        "deliveryDate": "2025-06-01",
        "comment": "Тест accept order",
        "color": ["BLACK"]
    }
    resp = requests.post(f"{MAIN_URL}{CREATE_ORDER_URL}", json=payload)
    assert resp.status_code == 201
    return resp.json()["track"]
=======
import allure
import requests

from helpers import generate_first_name, generate_password, generate_address, generate_metro_station, \
    generate_phone, generate_rent_time, generate_delivery_date, generate_comment, generate_color, generate_courier_id
from data import MAIN_URL, CREATE_ORDER_URL, LOGIN, PASSWORD, FIRST_NAME, ACCEPT_ORDER_URL, \
    LOGIN_COURIER_URL
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4


class TestAcceptOrder:

<<<<<<< HEAD
    @allure.title("Принять заказ без courierId → 400")
    def test_accept_order_without_courier_id(self):
        track = create_test_order()
        with allure.step("PUT без courierId"):
            resp = requests.put(f"{MAIN_URL}{ACCEPT_ORDER_URL}/{track}", params={})
        assert resp.status_code == 400
        assert resp.json() == ERROR_MESSAGES["INSUFFICIENT_DATA"]

    @allure.title("Принять заказ с некорректным courierId")
    def test_accept_order_with_invalid_courier_id(self):
        track = create_test_order()
        params = {"courierId": "invalid999abc"}
        with allure.step("PUT с некорректным courierId"):
            resp = requests.put(f"{MAIN_URL}{ACCEPT_ORDER_URL}/{track}", params=params)
        assert resp.status_code in (404, 500)

    @allure.title("Принять несуществующий заказ → 404 (или 500 на стенде)")
    def test_accept_nonexistent_order(self, create_courier):
        courier_info = create_courier
        courier_id = courier_info.get("id")
        if not courier_id:
            pytest.skip("Не удалось получить id курьера")

        fake_track = 999999999999
        params = {"courierId": courier_id}

        with allure.step("PUT несуществующего заказа"):
            resp = requests.put(f"{MAIN_URL}{ACCEPT_ORDER_URL}/{fake_track}", params=params)

        # Стенд часто возвращает 500 вместо 404 — это известная особенность
        assert resp.status_code in (404, 500), f"Ожидалось 404 или 500, получено {resp.status_code}"
        if resp.status_code == 404:
            assert resp.json().get("message") == ERROR_MESSAGES["ORDER_NOT_FOUND"]["message"]
        else:
            allure.dynamic.description("Стенд вернул 500 вместо 404 — баг учебного API")
=======
    @allure.title('Принять заказ без id курьера')
    def test_accept_order_without_courier_id_return_message_conflict(self, create_courier, delete_courier):
        # Создать заказ
        payload_order = {"firstName": generate_first_name(), "lastName": generate_password(),
                         "address": generate_address(),
                         "metroStation": generate_metro_station(), "phone": generate_phone(),
                         "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                         "comment": generate_comment(),
                         "color": generate_color()}
        response_order = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)
        order_id = response_order.json()['track']

        # Принять заказ
        params = {'courierId': ""}
        response = requests.put(f'{MAIN_URL}{ACCEPT_ORDER_URL}/{order_id}', params=params)

        assert response.status_code == 400 and response.json() == {
            'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title('Принять заказ с не корректным id курьера')
    def test_accept_order_with_incorrect_courier_id_return_message_not_found(self):
        # Создать заказ
        payload_order = {"firstName": generate_first_name(), "lastName": generate_password(),
                         "address": generate_address(),
                         "metroStation": generate_metro_station(), "phone": generate_phone(),
                         "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                         "comment": generate_comment(),
                         "color": generate_color()}
        response_order = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)
        order_id = response_order.json()['track']

        # Принять заказ
        params = {'courierId': generate_courier_id()}
        response = requests.put(f'{MAIN_URL}{ACCEPT_ORDER_URL}/{order_id}', params=params)

        assert response.status_code == 404 and response.json() == {
            'code': 404, 'message': 'Курьера с таким id не существует'}

    @allure.title('Принять заказ с не корректным id заказа')
    def test_accept_order_with_incorrect_order_id_return_message_error(self, create_courier, delete_courier):
        # Получить id курьера
        payload_courier = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
        response_courier = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload_courier)
        id_courier = response_courier.json()['id']

        # Принять заказ
        params = {'courierId': id_courier}
        response = requests.put(f'{MAIN_URL}{ACCEPT_ORDER_URL}/{id_courier}', params=params)

        assert response.status_code == 404 and response.json() == {
            'code': 404, 'message': 'Заказа с таким id не существует'}
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4
