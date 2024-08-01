import pytest

from constants import Constants
import allure

from scooter_service.description_route import APIScooter

@allure.epic('Делаем проверки создания курьера')
class TestCourierCreate:
    @allure.step("Проверяем, что курьера можно создать и запрос возвращает правильный код ответа 201")
    def test_courier_create_check(self):
        data = {
            "login": Constants.LOGIN,
            "password": Constants.PASSWORD,
            "firstName": Constants.FIRSTNAME
        }
        self.response = APIScooter().post_create_courier(data=data)
        assert self.response.status_code == 201

        try:
        #Удалим созданного курьера
            del (data['firstName'])
            self.response = APIScooter().post_login_courier(data=data)
            id = self.response.json()['id']
            self.response = APIScooter().delete_login_courier(parametr=id)
            assert self.response.status_code == 200
        except Exception as e:
            print(f'Не смогли удалить курьера {id}, ошибка {e}')




    @allure.step("Проверяем, что успешный запрос возвращает правильный ответ")
    def test_courier_create_response_body_valid_true(self):
        data = {
            "login": Constants.LOGIN,
            "password": Constants.PASSWORD,
            "firstName": Constants.FIRSTNAME
        }
        self.response = APIScooter().post_create_courier(data=data)
        assert self.response.json() == Constants.RESPONSE_BODY_CREATE_COURIER

        try:
        #Удалим созданного курьера
            del (data['firstName'])
            self.response = APIScooter().post_login_courier(data=data)
            id = self.response.json()['id']
            self.response = APIScooter().delete_login_courier(parametr=id)
            assert self.response.status_code == 200
        except Exception as e:
            print(f'Не смогли удалить курьера {id}, ошибка {e}')

    @allure.step("Проверяем, что нельзя создать двух одинаковых курьеров")
    def test_create_2identical_courier_response_409conflict(self):
        data = {
            "login": Constants.LOGIN,
            "password": Constants.PASSWORD,
            "firstName": Constants.FIRSTNAME
        }
        self.response_first = APIScooter().post_create_courier(data=data)
        allure.attach(f'Первое создание курьера. Статус ответа {self.response_first.status_code}')

        self.response_second = APIScooter().post_create_courier(data=data)
        allure.attach(f'Повторное создание курьера с тем-же набором данных. Статус ответа {self.response_second.status_code}')

        assert self.response_second.status_code == 409

        try:
            # Удалим созданного курьера
            del (data['firstName'])
            self.response = APIScooter().post_login_courier(data=data)
            id = self.response.json()['id']
            self.response = APIScooter().delete_login_courier(parametr=id)
            assert self.response.status_code == 200
        except Exception as e:
            print(f'Не смогли удалить курьера {id}, ошибка {e}')

    @allure.step("Проверяем, что нельзя создать курьеров с одинаковым логином")
    def test_create_2courier_with_same_login_response_409conflict(self):
        data = {
            "login": Constants.CONS_LOGIN,
            "password": Constants.PASSWORD,
            "firstName": Constants.FIRSTNAME
        }
        self.response_first = APIScooter().post_create_courier(data=data)
        allure.attach(f'Первое создание курьера. Статус ответа {self.response_first.status_code}')
        self.response_second = APIScooter().post_create_courier(data=data)
        allure.attach(f'Повторное создание курьера с тем-же логином. Статус ответа {self.response_second.status_code}')

        assert self.response_second.status_code == 409

    @allure.step("Проверяем создание курьера, когда отсутствует обязательное значение поля")
    @pytest.mark.parametrize('login, password,firstName',
                             [
                                 ['', Constants.PASSWORD, Constants.FIRSTNAME],
                                 [Constants.LOGIN, '', Constants.FIRSTNAME],
                                 ['', '', Constants.FIRSTNAME],
                             ])
    def test_create_courier_without_mandatory_field_response_400bad_request(self, login, password, firstName):
        data = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        self.response = APIScooter().post_create_courier(data=data)
        allure.attach(f'Попытка отправки запроса с логином = {login} и паролем = {password}. Статус ответа {self.response.status_code}')

        assert self.response.status_code == 400

    @allure.step("Проверяем, что если одного из полей нет в запросе - вернется ошибка")
    @pytest.mark.parametrize('data',
                             [
                                 {"password": Constants.PASSWORD, "firstName": Constants.FIRSTNAME},
                                 {"login": Constants.LOGIN,"firstName": Constants.FIRSTNAME}
                             ])
    def test_create_courier_when_one_field_missing_response_400bad_request(self, data):
        self.response = APIScooter().post_create_courier(data=data)
        allure.attach(f'Попытка отправки неполного запроса {data}. Статус ответа {self.response.status_code}')
        assert self.response.status_code == 400
