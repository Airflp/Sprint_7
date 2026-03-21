import allure
import requests

from data import LOGIN, PASSWORD, MAIN_URL, CREATE_COURIER_URL, COURIER_ID, FIRST_NAME, LOGIN_COURIER_URL


class TestDeleteCourier:

    @allure.title('Удалить курьера с не существующим id')
    def test_delete_courier_not_exist_id_return_message_error(self):
        response = requests.delete(f'{MAIN_URL}{CREATE_COURIER_URL}/{COURIER_ID}')

        assert response.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}

    @allure.title('Удалить курьера')
    def test_delete_courier_return_ok_true(self, create_courier):
        # Получить id курьера
        payload = {"login": LOGIN, "password": PASSWORD}
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)
        id_courier = response.json()['id']

        # Удалить курьера, который был создан
        response = requests.delete(f'{MAIN_URL}{CREATE_COURIER_URL}/{id_courier}')

        assert response.json() == {'ok': True}

    @allure.title('Удалить курьера без id курьера')
    def test_delete_courier_without_id_return_message_not_found(self):
        response = requests.delete(f'{MAIN_URL}{CREATE_COURIER_URL}')

        assert response.json() == {'code': 404, 'message': 'Not Found.'}
