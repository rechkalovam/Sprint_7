import pytest
import data
from methods.courier_methods import CourierMethods
from methods.order_methods import OrdersMethods
from helpers import HelpersMethods


@pytest.fixture()
def create_courier():
    courier_data = HelpersMethods.generate_courier_data()
    CourierMethods().create_courier(courier_data)
    return {"login": courier_data["login"], "password": courier_data["password"]}

@pytest.fixture()
def login_courier(create_courier):
    response = CourierMethods().login_courier(create_courier)
    courier_id = response[1]['id']
    yield courier_id
    CourierMethods().delete_courier(courier_id)

@pytest.fixture()
def delete_courier(login_courier):
    CourierMethods().delete_courier(login_courier)
    return login_courier

@pytest.fixture()
def create_order():
    response = OrdersMethods().create_order(HelpersMethods.generate_order_data())
    return response[1]['track']

@pytest.fixture()
def get_order_id(create_order):
    response = OrdersMethods().get_order_with_id(create_order)
    return response[1]['order']['id']

@pytest.fixture()
def accept_order(get_order_id, login_courier):
    OrdersMethods().accept_order(order_id=get_order_id, courier_id=login_courier)
    return get_order_id, login_courier