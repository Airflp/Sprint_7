import allure
import requests

from helpers import generate_first_name, generate_password, generate_address, generate_metro_station, \
    generate_phone, generate_rent_time, generate_delivery_date, generate_comment, generate_color, generate_courier_id
from data import MAIN_URL, CREATE_ORDER_URL, LOGIN, PASSWORD, FIRST_NAME, ACCEPT_ORDER_URL, \
    LOGIN_COURIER_URL


class TestAcceptOrder:

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