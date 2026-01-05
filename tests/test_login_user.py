import allure
import pytest
import requests
from url import Url
from data import TestData
from api_methods import ApiMethods

class TestLoginUser:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Вызывается фикстура, которая создает аккаунт. Осуществляется вход в аккаунт, проверяется статус-код и сообщение')
    def test_login_is_success(self, create_and_delete_user):
        response = ApiMethods.login_user(TestData.EMAIL, TestData.PASSWORD, TestData.NAME)
        assert response.status_code == 200 and TestData.RESPONSE_200 in response.text

    @allure.title('Негативная проверка на авторизацию с неверными данными')
    @allure.description('Попытка авторизации с неверным логином / паролем, проверяется статус-код и сообщение')
    @pytest.mark.parametrize(
        'payload',
        [
            ({"email": f'{TestData.EMAIL}kz', "password": TestData.PASSWORD}),
            ({"password": f'{TestData.PASSWORD}0', "name": TestData.NAME})
        ]
    )
    def test_auth_with_wrong_data(self, create_and_delete_user, payload):
        response = requests.post(url=Url.LOGIN_API, json=payload)
        assert response.status_code == 401 and response.text == TestData.RESPONSE_401_UNAUTHORIZED