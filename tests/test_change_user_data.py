import allure
import pytest
from data import TestData
from api_methods import ApiMethods


class TestChangeUserData:
    @allure.title('Изменение данных пользователя с авторизацией (запрос с токеном)')
    @allure.description('Вызывается фикстура, которая создает аккаунт и получает токен. Изменяются'
                        ' email / password / name, проверяется статус-код и сообщение. Аккаунт удаляется.')
    @pytest.mark.parametrize(
        'new_user_data',
        [
            ({"email":f'{TestData.EMAIL}kz', "password":TestData.PASSWORD, "name":TestData.NAME}),
            ({"email":TestData.EMAIL, "password":f'{TestData.PASSWORD}0', "name":TestData.NAME}),
            ({"email":TestData.EMAIL, "password":TestData.PASSWORD, "name":f'{TestData.NAME}21'})
        ]
    )
    def test_change_user_data_with_auth(self, create_and_delete_user, new_user_data):
        access_token = create_and_delete_user
        response = ApiMethods.change_user_data_with_auth(new_user_data, access_token)
        assert response.status_code == 200 and TestData.RESPONSE_200 in response.text

    @allure.title('Изменение данных пользователя без авторизации (запрос без токена)')
    @allure.description('Вызывается фикстура, которая создает аккаунт. Производится попытка изменить'
                        ' email / password / name без токена в запросе, проверяется статус-код и сообщение. Аккаунт удаляется.')
    @pytest.mark.parametrize(
        'new_user_data',
        [
            ({"email":f'{TestData.EMAIL}kz', "password":TestData.PASSWORD, "name":TestData.NAME}),
            ({"email":TestData.EMAIL, "password":f'{TestData.PASSWORD}0', "name":TestData.NAME}),
            ({"email":TestData.EMAIL, "password":TestData.PASSWORD, "name":f'{TestData.NAME}21'})
        ]
    )
    def test_change_user_data_without_auth(self, create_and_delete_user, new_user_data):
        response = ApiMethods.change_user_data_without_auth(new_user_data)
        assert response.status_code == 401 and TestData.RESPONSE_401_CHANGE_DATA in response.text

    