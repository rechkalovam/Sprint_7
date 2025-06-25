import requests
import allure
from requests.exceptions import JSONDecodeError
from urls import BASE_URL, COURIERS_URL


class CourierMethods:

    @allure.step("Создание курьера")
    def create_courier(self, data):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    @allure.step("Логин курьера")
    def login_courier(self, data):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', data=data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    @allure.step("Удаление курьера")
    def delete_courier(self, id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}/{id}')
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text