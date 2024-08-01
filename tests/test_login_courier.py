import allure
import pytest

from constants import Constants
from scooter_service.description_route import APIScooter
from scooter_service.register_new_courier import RegisterCourierRandom


@allure.epic('Делаем проверку успешной авторизации курьера')
class TestCourierLogin:
    @allure.step("Проверяем, что курьера может авторизоваться")
    def test_courier_login_auth_200_OK(self):
        login_pass = RegisterCourierRandom.register_new_courier_and_return_login_password(self)
        data = {
            "login": login_pass[0],
            "password": login_pass[1]
                }
        self.response = APIScooter().post_login_courier(data=data)
        assert self.response.status_code == 200



    @allure.step("Проверяем, что для авторизации нужны все обязательные поля")
    @pytest.mark.parametrize('data',
                             [
                                 {"login": '',"password": Constants.VALID_PASS},
                                 {"login": Constants.VALID_LOGIN,"password": ''}
                             ])
    def test_courier_login_without_mandatory_field_response_400bad_request(self, data):
        self.response = APIScooter().post_login_courier(data=data)
        allure.attach(f'Попытка отправки запроса c пустым обязательным полем {data}. Статус ответа {self.response.status_code}')
        assert self.response.status_code == 400

    @allure.step("Проверяем, что успешный запрос возвращает валидный ответ")
    def test_courier_login_response_body_valid(self):
        login_pass = RegisterCourierRandom.register_new_courier_and_return_login_password(self)
        data = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        self.response = APIScooter().post_login_courier(data=data)
        assert 'id' in (self.response.json())


    @allure.step("Проверяем, что если какого-то поля нет в body, запрос возвращает ошибку")
    @pytest.mark.parametrize('data',
                             [
                                 {"login": '',"password": Constants.PASSWORD},
                                 {"login": Constants.LOGIN,"password": ''}
                             ])
    def test_courier_login_when_one_field_missing_response_400bad_request(self, data):
        self.response = APIScooter().post_login_courier(data=data)
        allure.attach(f'Попытка отправки запроса c пустым обязательным полем {data}. Статус ответа {self.response.status_code}')
        assert self.response.status_code == 400

    @allure.step("Проверяем, что система вернёт ошибку, если неправильно указать логин или пароль, несуществующий логин и пароль")
    @pytest.mark.parametrize('data',
                             [
                                 {"login": Constants.VALID_LOGIN,"password": Constants.INVALID_PASS},
                                 {"login": Constants.INVALID_LOGIN,"password": Constants.VALID_PASS},
                                 {"login": Constants.INVALID_LOGIN, "password": Constants.INVALID_PASS},
                             ])
    def test_courier_login_with_invalid_login_or_password_404not_found(self, data):
        self.response = APIScooter().post_login_courier(data=data)
        allure.attach(f'Попытка отправки запроса c невалидным паарметром {data}. Статус ответа {self.response.status_code}')
        assert self.response.status_code == 404

