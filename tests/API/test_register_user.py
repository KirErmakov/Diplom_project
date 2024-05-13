import pytest
import allure
from test_data.data import complete_creds, incomplete_creds
from request_helper.api_call import api_call
from utils.json_validator import validate_schema


@pytest.mark.positive
@allure.tag('API')
@allure.feature('API')
@allure.story('Register User')
@allure.title('Successful user registration')
@allure.link('https://reqres.in/')
def test_register_successful(base_endpoint):
    response = api_call.send_request('post', base_endpoint[2], complete_creds)

    with allure.step('Check response status code == 200'):
        assert response.status_code == 200
    with allure.step('Check response data'):
        assert 'id' in response.json() and 'token' in response.json()
    with allure.step('Validate JSON schema'):
        validate_schema(response.json(), 'register_user.json')


@pytest.mark.negative
@allure.tag('API')
@allure.feature('API')
@allure.story('Register User')
@allure.title('Unsuccessful user registration')
@allure.link('https://reqres.in/')
def test_register_unsuccessful(base_endpoint):
    response = api_call.send_request('post', base_endpoint[2], incomplete_creds)

    with allure.step('Check response status code == 400'):
        assert response.status_code == 400
    with allure.step('Check response data'):
        assert 'error' in response.json()
        assert response.json()["error"] == "Missing password"
