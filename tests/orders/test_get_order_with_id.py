import pytest
from methods.order_methods import OrdersMethods
import data
import allure

@allure.feature("Получение заказа по id заказа")
class TestGetOrderWithId:

    @allure.title("Положительный кейс получения заказа по id заказа")
    def test_get_order_with_id_success(self, create_order):
        status, message = OrdersMethods().get_order_with_id(create_order)
        assert status == 200 and message['order'] is not None, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка получения заказа без заполнения id заказа")
    def test_get_order_with_id_order_track_is_empty_error(self):
        status, message = OrdersMethods().get_order_with_id(data.EMPTY_ID)
        assert status == 400 and message == data.GET_ORDER_WITH_ID_ORDER_TRACK_ARE_NOT_FILLED_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка получения заказа с несуществующим id заказа")
    def test_get_order_with_id_order_track_is_not_valid_error(self):
        status, message = OrdersMethods().get_order_with_id(data.NOT_VALID_ORDER_ID)
        assert status == 404 and message == data.GET_ORDER_WITH_ID_ORDER_TRACK_ARE_NOT_VALID_ERROR_BODY, f'Полученный код ответа: {status}, тело ответа: {message}'