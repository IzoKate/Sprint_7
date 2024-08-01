from constants import Constants
import allure

from scooter_service.description_route import APIScooter

@allure.epic('Делаем проверку на получение списка заказов')
class TestGetOrderList:
    @allure.step("Проверяем, что по запросу получаем список заказов, отбираем первые 10")
    def test_get_oder_list_state200(self):
        self.response = APIScooter().get_list_orders(parametr=Constants.PARAMETR_GET_ORDER_LIST)
        assert self.response.status_code == 200

    @allure.step("Проверяем, что по запросу получаем список заказов, в body")
    def test_get_oder_list_order_response_body_include_orders(self):
        #Получаем список заказов
        self.response = APIScooter().get_list_orders(parametr=Constants.PARAMETR_GET_ORDER_LIST)
        body_elements = self.response.json()['orders']
        assert len(body_elements) > 0