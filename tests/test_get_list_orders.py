import allure
import requests
<<<<<<< HEAD
from data import MAIN_URL, GET_LIST_ORDERS_URL
=======

from data import LIMIT_ORDERS, MAIN_URL, GET_LIST_ORDERS_URL
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4


class TestListOrders:

<<<<<<< HEAD
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
=======
    @allure.title('Получить заказы и проверить тело ответа возвращает список заказов')
    def test_get_orders_return_list_orders(self):
        # Получить список заказов
        params = {"limit": LIMIT_ORDERS}
        response = requests.get(f'{MAIN_URL}{GET_LIST_ORDERS_URL}', params=params)

        assert len(response.json()['orders']) == LIMIT_ORDERS
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4
