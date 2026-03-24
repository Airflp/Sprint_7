import allure
import requests
import pytest

from data import MAIN_URL, CREATE_COURIER_URL, ERROR_MESSAGES


class TestDeleteCourier:

    @allure.title("Удаление существующего курьера → ok: true")
    def test_delete_existing_courier(self, new_create_courier):
        courier_info = new_create_courier
        courier_id = courier_info.get("id")
        if not courier_id:
            pytest.skip("Не удалось получить id курьера")

        with allure.step(f"Удаляем курьера id={courier_id}"):
            resp = requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}/{courier_id}")

        assert resp.status_code == 200
        assert resp.json() == {"ok": True}

    @allure.title("Удаление несуществующего курьера → 404")
    def test_delete_nonexistent_courier(self):
        fake_id = 987654321
        with allure.step(f"Удаление несуществующего id={fake_id}"):
            resp = requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}/{fake_id}")
        assert resp.status_code == 404

    @allure.title("Удаление без id → ошибка")
    def test_delete_without_id(self):
        with allure.step("DELETE без id"):
            resp = requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}")
        assert resp.status_code in (400, 404)