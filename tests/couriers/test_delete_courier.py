import pytest
from methods.courier_methods import CourierMethods
import data
import allure

@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Положительный кейс удаления курьера")
    def test_delete_courier_success(self, login_courier):
        status, message = CourierMethods().delete_courier(login_courier)
        assert status == 200 and message == data.DELETE_COURIER_SUCCESS_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка удаления уже удаленного курьера")
    def test_delete_courier_already_deleted_error(self, delete_courier):
        status, message = CourierMethods().delete_courier(delete_courier)
        assert status == 404 and message == data.DELETE_NOT_FOUND_COURIER_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка удаления курьера без заполнения id курьера")
    def test_delete_courier_required_field_are_not_filled_error(self):
        status, message = CourierMethods().delete_courier(data.EMPTY_ID)
        assert status == 404 and message == data.DELETE_COURIER_MISSING_REQUIRED_FIELDS_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'