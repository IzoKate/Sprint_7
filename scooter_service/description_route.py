import json

from constants import Constants
from scooter_service.scooter_request_maker import RequestProcessing

#Класс описывает ручки сервиса Самокат
class APIScooter:
    host = Constants.URL_SERVICE

    #Создание курьера
    def post_create_courier(self, path="/api/v1/courier", data=None):
        headers = Constants.HEADERS_JSON
        url = f"{self.host}{path}"
        return RequestProcessing().make_request('post', url, data=data, headers=headers)

    #Удаление курьера
    def delete_login_courier(self, path="/api/v1/courier/", data=None, parametr=None):
        url = f'{self.host}{path}{parametr}'
        parametr = str(parametr)
        data_body = {"id": parametr}
        data = json.dumps(data_body)
        return RequestProcessing().make_request(r_type='delete', url=url, data=data, headers=None)


    #Логин курьера
    def post_login_courier(self, path="/api/v1/courier/login", data=None):
        headers = Constants.HEADERS_JSON
        url = f'{self.host}{path}'
        return RequestProcessing().make_request('post', url, data=data, headers=headers)

    #Создание заказа
    def post_order_create(self, path="/api/v1/orders", data=None):
        url = f'{self.host}{path}'
        return RequestProcessing().make_request(r_type='post', url=url, data=data, headers=None)


    #Отмена заказа
    def put_cancel_order(self, path="/api/v1/orders/cancel", data=None):
        headers = Constants.HEADERS_JSON
        url = f'{self.host}{path}'
        return RequestProcessing().make_request(r_type='put', url=url, data=data, headers=headers)


    #Получение списка заказов
    def get_list_orders(self, path="/api/v1/orders", parametr=None):
        url = f'{self.host}{path}{parametr}'
        return RequestProcessing().make_request(r_type='get', url=url)


