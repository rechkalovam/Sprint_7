import pytest
from methods.order_methods import OrdersMethods
import data
import allure

@allure.feature("Принятие заказа")
class TestAcceptOrder:

    @allure.title("Положительный кейс принятия заказа")
    def test_accept_order_success(self, login_courier, get_order_id):
        status, message = OrdersMethods().accept_order(order_id=get_order_id, courier_id=login_courier)
        assert status == 200 and message == data.ACCEPT_ORDER_SUCCESS_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка принять заказ без заполнения id курьера")
    def test_accept_order_courier_id_are_not_filled_error(self, get_order_id):
        status, message = OrdersMethods().accept_order(order_id=get_order_id, courier_id=data.EMPTY_ID)
        assert status == 400 and message == data.ACCEPT_ORDER_COURIER_ID_ARE_NOT_FILLED_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка принять заказ без заполнения id заказа")
    def test_accept_order_id_are_not_filled_error(self, login_courier):
        status, message = OrdersMethods().accept_order(order_id=data.EMPTY_ID, courier_id=login_courier)
        assert status == 404 and message == data.ACCEPT_ORDER_ID_ARE_NOT_FILLED_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка принять заказ с несуществующим id заказа")
    def test_accept_order_id_are_not_valid_error(self, login_courier):
        status, message = OrdersMethods().accept_order(order_id=data.NOT_VALID_ORDER_ID, courier_id=login_courier)
        assert status == 404 and message == data.ACCEPT_ORDER_ID_ARE_NOT_VALID_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка принять заказ с несуществующим id курьера")
    def test_accept_order_courier_id_are_not_valid_error(self, get_order_id):
        status, message = OrdersMethods().accept_order(order_id=get_order_id, courier_id=data.NOT_VALID_COURIER_ID)
        assert status == 404 and message == data.ACCEPT_ORDER_COURIER_ID_ARE_NOT_VALID_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка принять уже принятый заказ")
    def accept_order_already_accepted_error(self, accept_order):
        order_id, courier_id = accept_order
        status, message = OrdersMethods().accept_order(order_id=order_id, courier_id=courier_id)
        assert status == 409 and message == data.ACCEPT_ORDER_ALREADY_ACCEPTED_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    