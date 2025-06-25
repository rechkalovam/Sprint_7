import random
import string
import data

class HelpersMethods:

    @staticmethod
    def generate_courier_data():
        login = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 8)))
        password = ''.join(random.choice(string.digits) for _ in range(random.randint(4, 8)))
        first_names = ['Михаил', 'Кристина', 'Алексей', 'Мария', 'Анна', 'Андрей', 'Прохор', 'Иван', 'Сергей']
        first_name = random.choice(first_names)
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }
    
    @staticmethod
    def generate_order_data():
        orders_data = [data.ORDER_DATA_1, data.ORDER_DATA_2, data.ORDER_DATA_3, data.ORDER_DATA_4, data.ORDER_DATA_5]
        return random.choice(orders_data)