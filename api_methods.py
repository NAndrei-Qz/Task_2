import allure
import requests
from url import Url

class ApiMethods:
    @staticmethod
    @allure.step('Регистрация пользователя')
    def create_account(email: str, password: str, name: str):
        return requests.post(url=Url.REGISTRATION_API, json={"email": email, "password": password, "name": name})
    
    @staticmethod
    @allure.step('Удаление аккаунта пользователя')
    def delete_account(access_token: str):
        response = requests.delete(url=Url.USER_API, headers={'Authorization': access_token})
        return response
    
    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(email: str, password: str, name: str):
        return requests.post(url=Url.LOGIN_API, json={"email": email, "password": password, "name": name})
    
    @staticmethod
    @allure.step('Изменение данных пользователя с токеном')
    def change_user_data_with_auth(new_user_data, access_token: str):
        response = requests.patch(url=Url.USER_API, json=new_user_data, headers={'Authorization': access_token})
        return response

    @staticmethod
    @allure.step('Изменение данных пользователя без токена')
    def change_user_data_without_auth(new_user_data):
        response = requests.patch(url=Url.USER_API, json=new_user_data)
        return response

    @staticmethod
    @allure.step('Создание заказа с токеном')
    def create_order_with_auth(order_data, access_token: str):
        response = requests.post(Url.ORDERS_API, json=order_data, headers={'Authorization': access_token})
        return response

    @staticmethod
    @allure.step('Создание заказа без токена')
    def create_order_without_auth(order_data):
        response = requests.post(Url.ORDERS_API, json=order_data)
        return response

    @staticmethod
    @allure.step('Получение данных об ингредиентах')
    def get_ingredients():
        response = requests.get(Url.INGREDIENTS_API)
        return response

    @staticmethod
    @allure.step('Получение списка заказов конкретного пользователя')
    def get_order_list(access_token: str):
        response = requests.get(Url.ORDERS_API, headers={'Authorization': access_token})
        return response
