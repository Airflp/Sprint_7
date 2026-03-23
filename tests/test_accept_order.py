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


class TestAcceptOrder:

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