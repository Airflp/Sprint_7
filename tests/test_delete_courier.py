import allure
import requests
<<<<<<< HEAD
import pytest

from data import MAIN_URL, CREATE_COURIER_URL, ERROR_MESSAGES
=======

from data import LOGIN, PASSWORD, MAIN_URL, CREATE_COURIER_URL, COURIER_ID, FIRST_NAME, LOGIN_COURIER_URL
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4


class TestDeleteCourier:

<<<<<<< HEAD
    @allure.title("Удаление существующего курьера → ok: true")
    def test_delete_existing_courier(self, create_courier):
        courier_info = create_courier
        courier_id = courier_info.get("id")
        if not courier_id:
            pytest.skip("Не удалось получить id курьера")

        with allure.step(f"DELETE курьера id={courier_id}"):
            resp = requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}/{courier_id}")

        assert resp.status_code == 200
        assert resp.json() == {"ok": True}

    @allure.title("Удаление несуществующего курьера → 404")
    def test_delete_nonexistent_courier(self):
        fake_id = 987654321
        with allure.step(f"DELETE несуществующего id={fake_id}"):
            resp = requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}/{fake_id}")
        assert resp.status_code == 404

    @allure.title("Удаление без id → ошибка")
    def test_delete_without_id(self):
        with allure.step("DELETE без id"):
            resp = requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}")
        assert resp.status_code in (400, 404)
=======
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
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4
