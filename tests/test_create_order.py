import allure
import pytest

from constants import Constants
from scooter_service.description_route import APIScooter


@allure.epic('Делаем проверку создания заказа')
class TestOrderCreate:
    @allure.step("Проверяем, что заказ можно создать")
    def test_order_create_order_created_201(self):
        data = Constants.DATA_ORDER
        self.response = APIScooter().post_order_create(data=data)
        allure.attach(
            f'Создаем новый заказ {data}. Статус ответа {self.response.status_code}')
        assert self.response.status_code == 201

        try:
        # Отменяем созданный в тесте заказ
            data_cancel = self.response.json()
            self.response_cancel = APIScooter().put_cancel_order(data=data_cancel)
            assert self.response_cancel.status_code == 200
        except Exception as e:
            print(f'Не смогли отменить заказа {data_cancel}, ошибка {e}')


    @allure.step("Проверяем, что тело ответа содержит track")
    def test_order_create_order_response_200(self):
        data = Constants.DATA_ORDER
        self.response = APIScooter().post_order_create(data=data)
        allure.attach(
            f'Создаем новый заказ {data}. Статус ответа {self.response.status_code}')
        assert 'track' in (self.response.json())

        try:
        # Отменяем созданный в тесте заказ
            data_cancel = self.response.json()
            self.response_cancel = APIScooter().put_cancel_order(data=data_cancel)
            assert self.response_cancel.status_code == 200
        except Exception as e:
            print(f'Не смогли отменить заказа {data_cancel}, ошибка {e}')

    @allure.step("Проверяем, указание цветов в запросе")
    @pytest.mark.parametrize('data',
                             [
                                 Constants.DATA_ORDER,
                                 Constants.DATA_ORDER_GREY,
                                 Constants.DATA_ORDER_GREY_BLACK,
                                 Constants.DATA_ORDER_NO_COLOR
                             ])
    def test_order_create_with_different_color_order_created_201(self, data):
        self.response = APIScooter().post_order_create(data=data)
        allure.attach(
            f'Создаем новый заказ с цветом {data}. Статус ответа {self.response.status_code}')
        assert self.response.status_code == 201

        try:
        # Отменяем созданный в тесте заказ
            data_cancel = self.response.json()
            self.response_cancel = APIScooter().put_cancel_order(data=data_cancel)
            assert self.response_cancel.status_code == 200
        except Exception as e:
            print(f'Не смогли отменить заказа {data_cancel}, ошибка {e}')
