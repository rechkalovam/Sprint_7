import pytest
from methods.order_methods import OrdersMethods
import allure

@allure.feature("Получение списка заказов")
class TestGetOrderList:

    @allure.title("Положительный кейс получения списка заказов")
    def test_get_order_list_success(self):
        status, message = OrdersMethods().get_order_list()
        assert status == 200 and message['orders'] is not None, f'Полученный код ответа: {status}, тело ответа: {message}'
        