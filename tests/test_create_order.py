import allure
import random
from api_methods import ApiMethods
from data import TestData

class TestCreateOrder:
    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description('Вызывается фикстура, которая создает аккаунт, проверяется авторизованное создание заказа со случайным ингредиентом'
                        ' из доступных, проверяется статус-код и сообщение. Аккаунт удаляется.')
    def test_create_order_with_auth(self, create_and_delete_user):
        access_token = create_and_delete_user
        ingredients = {'ingredients': ApiMethods.get_ingredients().json()['data'][random.randint(0, 14)]['_id']}
        response = ApiMethods.create_order_with_auth(ingredients, access_token)
        assert response.status_code == 200 and TestData.RESPONSE_200 in response.text

    @allure.title('Негативная проверка создания заказа без авторизации')
    @allure.description(
        'Вызывается фикстура, которая создает аккаунт, проверяется создание заказа без токена авторизации со случайным ингредиентом'
        ' из доступных, проверяется статус-код и сообщение. Аккаунт удаляется.')
    def test_create_order_without_auth(self, create_and_delete_user):
        ingredients = {'ingredients': ApiMethods.get_ingredients().json()['data'][random.randint(0, 14)]['_id']}
        response = ApiMethods.create_order_without_auth(ingredients)
        assert response.status_code == 200 and TestData.RESPONSE_200 in response.text

    @allure.title('Негативная проверка создания заказа с пустым списком ингредиентов')
    @allure.description('Вызывается фикстура, которая создает аккаунт, проверяется создание заказа с пустым списком ингредиентов,'
        ' проверяется статус-код и сообщение. Аккаунт удаляется.')
    def test_create_order_without_ingredients(self, create_and_delete_user):
        access_token = create_and_delete_user
        ingredients = {}
        response = ApiMethods.create_order_with_auth(ingredients, access_token=access_token)
        assert response.status_code == 400 and TestData.RESPONSE_400 in response.text

    @allure.title('Негативная проверка создания заказа с неверным хэшем ингредиентов')
    @allure.description('Вызывается фикстура, которая создает аккаунт, проверяется создание заказа с неверным хешем ингредиентов (генерация рандомного значения),'
        ' проверяется статус-код и сообщение. Аккаунт удаляется.')
    def test_create_orders_with_wrong_hash(self, create_and_delete_user):
        access_token = create_and_delete_user
        ingredients = {'ingredients': f'{random.randint(100000000, 900000000)}'}
        response = ApiMethods.create_order_with_auth(ingredients, access_token=access_token)
        assert response.status_code == 500 and TestData.RESPONSE_500 in response.text

