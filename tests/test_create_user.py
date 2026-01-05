import allure
import pytest
import requests
from url import Url
from data import TestData
from api_methods import ApiMethods

class TestCreateUser:
    @allure.title('Проверка регистрации уникального пользователя')
    @allure.description('Создаётся аккаунт, данные из ответа сохраняются в переменную, аккаунт удаляется. '
                        'Затем производится проверка статус-кода ответа и сообщения об успешном создании')
    def test_create_user_is_success(self):
        response = ApiMethods.create_account(TestData.EMAIL, TestData.PASSWORD, TestData.NAME)
        access_token = response.json()['accessToken']
        ApiMethods.delete_account(access_token)
        assert response.status_code == 200 and TestData.RESPONSE_200 in response.text

    @allure.title('Негативная проверка попытки регистрации существующего пользователя')
    @allure.description(
        '(Вызывается фикстура создания аккаунта, затем производится попытка создания курьера с теми же данными. '
        'Проверяется статус-код и сообщения ответа. Аккаунт удаляется')
    def test_create_with_duplicate_data(self, create_and_delete_user):
        response = ApiMethods.create_account(TestData.EMAIL, TestData.PASSWORD, TestData.NAME)
        assert response.status_code == 403 and response.text == TestData.RESPONSE_403_USER_EXISTS

    @allure.title('Негативная проверка на заполнение не всех обязательных полей при регистрации аккаунта')
    @allure.description('Попытка регистрации без передачи одного из обязательных полей, проверяется статус-код и сообщение')
    @pytest.mark.parametrize(
        'payload',
        [
            ({"email": TestData.EMAIL, "password": TestData.PASSWORD}),
            ({"password": TestData.PASSWORD, "name": TestData.NAME}),
            ({"email": TestData.EMAIL, "name": TestData.NAME})
        ]
    )
    def test_create_without_required_fields(self, payload):
        response = requests.post(url=Url.REGISTRATION_API, json=payload)
        assert response.status_code == 403 and response.text == TestData.RESPONSE_403_EMPTY_FIELD