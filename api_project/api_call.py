import allure
from utils.api_logger import send_request_logger


class ApiCall:

    @allure.step('Send API Request')
    def send_request(self, method, base_url, payload=None):
        response = send_request_logger(method=method.upper(), url=base_url, data=payload)
        return response


api_call = ApiCall()
