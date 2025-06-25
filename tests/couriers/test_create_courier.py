import pytest
from methods.courier_methods import CourierMethods
from helpers import HelpersMethods
import data
import allure

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Положительный кейс создания курьера")
    def test_create_courier_success(self):
        courier_data = HelpersMethods.generate_courier_data()
        status, message = CourierMethods().create_courier(courier_data)
        assert status == 201 and message == data.CREATE_COURIER_SUCCESS_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка создания дважды одного курьера")
    def test_create_courier_create_twice_error(self, create_courier):
        status, message = CourierMethods().create_courier(create_courier)
        assert status == 409 and message == data.CREATE_COURIER_TWICE_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка создания курьера без заполнения обязательных полей")
    @pytest.mark.parametrize('courier_data', [data.CREATE_COURIER_DATA_WITHOUT_LOGIN, data.CREATE_COURIER_DATA_WITHOUT_PASSWORD])
    def test_create_courier_required_fields_are_not_filled_error(self, courier_data):
        status, message = CourierMethods().create_courier(courier_data)
        assert status == 400 and message == data.CREATE_COURIER_MISSING_REQUIRED_FIELDS_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'