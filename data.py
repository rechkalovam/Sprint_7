CREATE_COURIER_DATA_WITHOUT_LOGIN = {"password": "12345", "firstName": "Андрей"}
CREATE_COURIER_DATA_WITHOUT_PASSWORD = {"login": "test_login", "firstName": "Андрей"}

LOGIN_COURIER_DATA_WITHOUT_LOGIN = {"password": "12345"}
LOGIN_COURIER_DATA_WITHOUT_PASSWORD = {"login": "test_login"}

EMPTY_ID = ''

CREATE_COURIER_SUCCESS_BODY = {'ok': True}
CREATE_COURIER_TWICE_ERROR_BODY = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
CREATE_COURIER_MISSING_REQUIRED_FIELDS_ERROR_BODY = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

LOGIN_NOT_FOUND_COURIER_ERROR_BODY = {'code': 404, "message": "Учетная запись не найдена"}
LOGIN_COURIER_LOGIN_ARE_NOT_FILLED_ERROR_BODY = {'code': 400, "message":  "Недостаточно данных для входа"}

DELETE_COURIER_SUCCESS_BODY = {'ok': True}
DELETE_NOT_FOUND_COURIER_ERROR_BODY = {"code": 404, "message": "Курьера с таким id нет."}
DELETE_COURIER_MISSING_REQUIRED_FIELDS_ERROR_BODY = {"code": 404, "message": "Not Found."}

ORDER_DATA_1 = {
    "firstName": "Сергей",
    "lastName": "Сергеич",
    "address": "г. Москва, ул. Ленина, д. 1",
    "metroStation": 4,
    "phone": "+7 800 000 00 00",
    "rentTime": 1,
    "deliveryDate": "2025-08-12",
    "comment": "тест черный самокат",
    "color": ["BLACK"]
}

ORDER_DATA_2 = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "г. Москва, ул. Пушкина, д. 88",
    "metroStation": 2,
    "phone": "+7 800 555 00 00",
    "rentTime": 1,
    "deliveryDate": "2025-09-09",
    "comment": "тест серый самокат",
    "color": ["GREY"]
}

ORDER_DATA_3 = {
    "firstName": "Петр",
    "lastName": "Петров",
    "address": "г. Москва, ул. Малышева, д. 1",
    "metroStation": 3,
    "phone": "+7 800 555 33 22",
    "rentTime": 1,
    "deliveryDate": "2025-12-12",
    "comment": "тест серый и черный самокат",
    "color": [
        "BLACK",
        "GREY"
    ]
}

ORDER_DATA_4 = {
    "firstName": "Мария",
    "lastName": "Иванова",
    "address": "г. Москва, ул. Петрова, д. 11",
    "metroStation": 5,
    "phone": "+7 999 555 33 22",
    "rentTime": 2,
    "deliveryDate": "2025-10-12",
    "comment": "тест без выбора цвета",
    "color": []
}

ORDER_DATA_5 = {
    "firstName": "Наталья",
    "lastName": "Иванова",
    "address": "г. Москва, ул. Киселева, д. 21",
    "metroStation": 5,
    "phone": "+7 999 555 33 22",
    "rentTime": 3,
    "deliveryDate": "2025-10-12",
    "comment": "тест без выбора цвета"
}

RANDOM_COURIER_ID = 12345
RANDOM_ORDER_ID = 12345
NOT_VALID_ORDER_ID = 000000
NOT_VALID_COURIER_ID = 000000


ACCEPT_ORDER_SUCCESS_BODY = {'ok': True}
ACCEPT_ORDER_COURIER_ID_ARE_NOT_FILLED_ERROR_BODY = {'code': 400, "message":  "Недостаточно данных для поиска"}
ACCEPT_ORDER_ID_ARE_NOT_FILLED_ERROR_BODY = {"code": 404, "message": "Not Found."}
ACCEPT_ORDER_ID_ARE_NOT_VALID_ERROR_BODY = {'code': 404, "message": "Заказа с таким id не существует"}
ACCEPT_ORDER_COURIER_ID_ARE_NOT_VALID_ERROR_BODY = {"code": 404, "message": "Курьера с таким id не существует"}
ACCEPT_ORDER_ALREADY_ACCEPTED_ERROR_BODY = {"code": 409, "message": "Этот заказ уже в работе"}

GET_ORDER_WITH_ID_ORDER_TRACK_ARE_NOT_FILLED_ERROR_BODY = {'code': 400, "message":  "Недостаточно данных для поиска"}
GET_ORDER_WITH_ID_ORDER_TRACK_ARE_NOT_VALID_ERROR_BODY = {"code": 404, "message": "Заказ не найден"}