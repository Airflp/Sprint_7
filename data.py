MAIN_URL = 'https://qa-scooter.praktikum-services.ru'

CREATE_COURIER_URL = '/api/v1/courier'
LOGIN_COURIER_URL = '/api/v1/courier/login'
CREATE_ORDER_URL = '/api/v1/orders'
GET_LIST_ORDERS_URL = '/api/v1/orders'
ACCEPT_ORDER_URL = '/api/v1/orders/accept'
GET_ORDER_BY_ID_URL = '/api/v1/orders/track'

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