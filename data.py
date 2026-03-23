<<<<<<< HEAD
MAIN_URL = 'https://qa-scooter.praktikum-services.ru'

=======
from helpers import generate_login, generate_password, generate_first_name, generate_limit_orders, \
    generate_courier_id

MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4
CREATE_COURIER_URL = '/api/v1/courier'
LOGIN_COURIER_URL = '/api/v1/courier/login'
CREATE_ORDER_URL = '/api/v1/orders'
GET_LIST_ORDERS_URL = '/api/v1/orders'
ACCEPT_ORDER_URL = '/api/v1/orders/accept'
GET_ORDER_BY_ID_URL = '/api/v1/orders/track'
<<<<<<< HEAD

ERROR_MESSAGES = {
    'INSUFFICIENT_DATA':    {'code': 400, 'message': 'Недостаточно данных для поиска'},
    'COURIER_NOT_FOUND':    {'code': 404, 'message': 'Курьера с таким id не существует'},
    'ORDER_NOT_FOUND':      {'code': 404, 'message': 'Заказа с таким id не существует'},
    'LOGIN_FAILED':         {'code': 404, 'message': 'Учетная запись не найдена'},
    'LOGIN_ALREADY_EXISTS': {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'},
}

# Базовый шаблон для заказа (firstName будет добавляться в тестах)
ORDER_TEMPLATE = {
    "lastName": "Тестович",
    "address": "ул. Тестовая, 77",
    "metroStation": 4,
    "phone": "+79998887766",
    "rentTime": 3,
    "deliveryDate": "2025-05-15",
    "comment": "Тестовый заказ из автотеста",
}
=======
LOGIN = generate_login()
PASSWORD = generate_password()
FIRST_NAME = generate_first_name()
LIMIT_ORDERS = generate_limit_orders()
COURIER_ID = generate_courier_id()
>>>>>>> 1c8f3abdddd388d6153b5b0534cd7327089e65e4
