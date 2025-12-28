import pytest
import requests
from url import Url
from data import TestData
from api_methods import ApiMethods

@pytest.fixture
def create_and_delete_user():
    response = ApiMethods.create_account(TestData.EMAIL, TestData.PASSWORD, TestData.NAME)
    access_token = response.json().get('accessToken')
    yield access_token
    requests.delete(Url.USER_API, headers={'Authorization': access_token})