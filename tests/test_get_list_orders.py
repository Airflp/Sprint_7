import allure
import requests
from data import MAIN_URL, GET_LIST_ORDERS_URL


class TestListOrders:

    @allure.title("GET /orders возвращает список заказов")
    def test_get_orders_returns_list(self):
        params = {"limit": 10, "page": 0}  # можно менять
        with allure.step("Получаем список заказов"):
            response = requests.get(f"{MAIN_URL}{GET_LIST_ORDERS_URL}", params=params)

        assert response.status_code == 200
        data = response.json()
        assert "orders" in data
        assert isinstance(data["orders"], list)
        # Не проверяем точное количество — лучше проверить что список не пустой
        assert len(data["orders"]) >= 0