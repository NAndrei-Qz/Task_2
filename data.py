class TestData:
    EMAIL = "hungry_boy@yandex.ru"
    PASSWORD = "315478_MS-@y"
    NAME = "Бибиджон"


    RESPONSE_200 = '"success":true'
    RESPONSE_403_USER_EXISTS = '{"success":false,"message":"User already exists"}'
    RESPONSE_403_EMPTY_FIELD = '{"success":false,"message":"Email, password and name are required fields"}'
    RESPONSE_401_UNAUTHORIZED = '{"success":false,"message":"email or password are incorrect"}'
    RESPONSE_401_CHANGE_DATA = '{"success":false,"message":"You should be authorised"}'
    RESPONSE_500 = 'Internal Server Error'
    RESPONSE_400 = '{"success":false,"message":"Ingredient ids must be provided"}'
