import pytest
from methods.courier_methods import CourierMethods
from helpers import HelpersMethods
import data
import allure

@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Положительный кейс логина курьера")
    def test_login_courier_success(self, create_courier):
        status, message = CourierMethods().login_courier(create_courier)
        assert status == 200 and message['id'] is not None, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка логина не созданного курьера")
    def test_login_courier_not_found_error(self):
        courier_data = HelpersMethods.generate_courier_data()
        status, message = CourierMethods().login_courier(courier_data)
        assert status == 404 and message == data.LOGIN_NOT_FOUND_COURIER_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка логина без заполнения логина в теле запроса")
    def test_login_courier_login_are_not_filled_error(self):
        status, message = CourierMethods().login_courier(data.LOGIN_COURIER_DATA_WITHOUT_LOGIN)
        assert status == 400 and message == data.LOGIN_COURIER_LOGIN_ARE_NOT_FILLED_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка логина без заполнения пароля в теле запроса")
    def test_login_courier_password_are_not_filled_error(self):
        status, message = CourierMethods().login_courier(data.LOGIN_COURIER_DATA_WITHOUT_PASSWORD)
        assert status == 504, f'Полученный код ответа: {status}, тело ответа: {message}'

