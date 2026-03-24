import allure
import requests

from data import MAIN_URL, GET_LIST_ORDERS_URL


class TestListOrders:

    @allure.title("GET /orders возвращает список заказов")
    def test_get_orders_returns_list(self):
        params = {"limit": 10, "page": 0}

        with allure.step("Получаем список заказов"):
            response = requests.get(
                f"{MAIN_URL}{GET_LIST_ORDERS_URL}",
                params=params,
                timeout=20
            )

        assert response.status_code == 200
        data = response.json()
        assert "orders" in data
        assert isinstance(data["orders"], list)

    @allure.title("Параметр limit ограничивает количество заказов в ответе")
    def test_get_orders_return_list_orders(self):
        limit_orders = 5
        params = {"limit": limit_orders, "page": 0}

        with allure.step(f"Получаем список заказов с limit={limit_orders}"):
            response = requests.get(
                f"{MAIN_URL}{GET_LIST_ORDERS_URL}",
                params=params,
                timeout=20
            )

        assert response.status_code == 200
        data = response.json()
        assert "orders" in data
        assert isinstance(data["orders"], list)
        assert len(data["orders"]) <= limit_orders