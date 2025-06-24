import requests
import allure
from requests.exceptions import JSONDecodeError
from urls import BASE_URL, ORDERS_URL


class OrdersMethods:

    @allure.step("Создание заказа")
    def create_order(self, data):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Получение списка заказов")    
    def get_order_list(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Принятие заказа")    
    def accept_order(self, order_id, courier_id):
        payload = {'courierId': f'{courier_id}'}
        response = requests.put(f'{BASE_URL}{ORDERS_URL}/accept/{order_id}', params=payload)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Получение заказа по id заказа")    
    def get_order_with_id(self, order_id):
        payload = {'t': f'{order_id}'}
        response = requests.get(f'{BASE_URL}{ORDERS_URL}/track', params=payload)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
        