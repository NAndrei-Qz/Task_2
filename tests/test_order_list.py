import allure
from data import TestData
from api_methods import ApiMethods

class TestOrderList:
    @allure.title('Проверка Получения списка заказов конкретного пользователя с токеном авторизации')
    @allure.title('Вызывается фикстура, которая создает аккаунт, проверяется авторизованное получение списка заказов пользователя,'
                        ' проверяется статус-код и сообщение. Аккаунт удаляется.')
    def test_get_order_list_with_auth(self, create_and_delete_user):
        access_token = create_and_delete_user
        response = ApiMethods.get_order_list(access_token)
        assert response.status_code == 200 and TestData.RESPONSE_200 in response.text

    @allure.title('Негативная проверка Получения списка заказов конкретного пользователя без токена авторизации')
    @allure.title('Вызывается фикстура, которая создает аккаунт, проверяется неавторизованное получение списка заказов пользователя,'
        ' проверяется статус-код и сообщение. Аккаунт удаляется.')
    def test_get_order_list_without_auth(self):
        response = ApiMethods.get_order_list(access_token='')
        assert response.status_code == 401 and TestData.RESPONSE_401_UNAUTHORIZED

