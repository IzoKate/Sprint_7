from scooter_service.register_new_courier import RegisterCourierRandom


class Constants:
    URL_SERVICE = "https://qa-scooter.praktikum-services.ru"
    HEADERS_JSON ={'Content-type': 'application/json'}

    #Рандомные значения логина, пароля и имени Курьера
    LOGIN = RegisterCourierRandom.generate_random_string(8)
    PASSWORD = RegisterCourierRandom.generate_random_string(8)
    FIRSTNAME = RegisterCourierRandom.generate_random_string(10)
    CONS_LOGIN = "Richard"
    VALID_LOGIN = "ircerxtjyn"
    VALID_PASS = "xkktlgcvby"
    INVALID_LOGIN = "Saren"
    INVALID_PASS = "12345678"

    DATA_ORDER = {
    "firstName": "Екатерина",
    "lastName": "Изосимова",
    "address": "Коммунистическая 11",
    "metroStation": 4,
    "phone": "+7 917 808 59 66",
    "rentTime": 5,
    "deliveryDate": "2024-06-28",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
        }

    DATA_ORDER_GREY = {
    "firstName": "Екатерина",
    "lastName": "Изосимова",
    "address": "Коммунистическая 11",
    "metroStation": 4,
    "phone": "+7 917 808 59 66",
    "rentTime": 5,
    "deliveryDate": "2024-06-28",
    "comment": "Saske, come back to Konoha",
    "color": ["GREY"]
        }

    DATA_ORDER_GREY_BLACK= {
        "firstName": "Екатерина",
        "lastName": "Изосимова",
        "address": "Коммунистическая 11",
        "metroStation": 4,
        "phone": "+7 917 808 59 66",
        "rentTime": 5,
        "deliveryDate": "2024-06-28",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK", "GREY"]
    }

    DATA_ORDER_NO_COLOR = {
        "firstName": "Екатерина",
        "lastName": "Изосимова",
        "address": "Коммунистическая 11",
        "metroStation": 4,
        "phone": "+7 917 808 59 66",
        "rentTime": 5,
        "deliveryDate": "2024-06-28",
        "comment": "Saske, come back to Konoha",
        "color": []
    }
    RESPONSE_BODY_CREATE_COURIER = {"ok":True}
    PARAMETR_GET_ORDER_LIST = "?limit=10&page=0"
