import allure
import requests

from helpers import generate_first_name, generate_address, generate_metro_station, generate_rent_time, \
    generate_phone, generate_password, generate_delivery_date, generate_comment, generate_color
from data import MAIN_URL, CREATE_ORDER_URL, GET_ORDER_BY_ID_URL


class TestGetOrderById:

    @allure.title('Получить заказ по его id')
    def test_get_order_by_id_true(self):
        # Создать заказ самоката с ЧЕРНЫМ или СЕРЫМ цветом
        payload_order = {"firstName": generate_first_name(), "lastName": generate_password(),
                         "address": generate_address(),
                         "metroStation": generate_metro_station(), "phone": generate_phone(),
                         "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                         "comment": generate_comment(),
                         "color": generate_color()}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)
        order_id = response.json()['track']

        params = {"t": order_id}
        response = requests.get(f'{MAIN_URL}{GET_ORDER_BY_ID_URL}', params=params)

        assert 'order' in response.json()

    @allure.title('Получить заказ без его id')
    def test_get_order_without_id_return_bad_request(self):
        # Создать заказ самоката с ЧЕРНЫМ или СЕРЫМ цветом
        payload_order = {"firstName": generate_first_name(), "lastName": generate_password(),
                         "address": generate_address(),
                         "metroStation": generate_metro_station(), "phone": generate_phone(),
                         "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                         "comment": generate_comment(),
                         "color": generate_color()}
        requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        params = {"t": ""}
        response = requests.get(f'{MAIN_URL}{GET_ORDER_BY_ID_URL}', params=params)

        assert response.status_code == 400 and response.json() == {'code': 400,
                                                                   'message': 'Недостаточно данных для поиска'}

    @allure.title('Получить заказ id, которого не существует')
    def test_get_order_by_not_exist_id_return_not_found(self):
        # Создать заказ самоката с ЧЕРНЫМ или СЕРЫМ цветом
        payload_order = {"firstName": generate_first_name(), "lastName": generate_password(),
                         "address": generate_address(),
                         "metroStation": generate_metro_station(), "phone": generate_phone(),
                         "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                         "comment": generate_comment(),
                         "color": generate_color()}
        requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        params = {"t": 111111111}
        response = requests.get(f'{MAIN_URL}{GET_ORDER_BY_ID_URL}', params=params)

        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Заказ не найден'}
