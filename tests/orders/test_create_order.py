import pytest
from methods.order_methods import OrdersMethods
import data
import allure

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Положительный кейс создания заказов с разными наборами цветов")
    @pytest.mark.parametrize('order_data', [data.ORDER_DATA_1, data.ORDER_DATA_2, data.ORDER_DATA_3, data.ORDER_DATA_4, data.ORDER_DATA_5])
    def test_create_order_success(self, order_data):
        status, message = OrdersMethods().create_order(order_data)
        assert status == 201 and message['track'] is not None, f'Полученный код ответа: {status}, тело ответа: {message}'
        