import pytest
import allure
from test_data.data import existing_user_id, not_existing_user_id
from request_helper.api_call import api_call
from utils.json_validator import validate_schema


@pytest.mark.positive
@allure.tag('API')
@allure.feature('API')
@allure.story('Get user info')
@allure.title('Get existing user info')
@allure.link('https://reqres.in/')
def test_get_user(base_endpoint):
    response = api_call.send_request('get', base_url=f"{base_endpoint[0]}/{existing_user_id}")

    with allure.step('Check response status code == 200'):
        assert response.status_code == 200
    with allure.step('Check response data'):
        assert response.json()['data']['id'] == existing_user_id
    with allure.step('Validate JSON schema'):
        validate_schema(response.json(), 'get_user.json')


@pytest.mark.negative
@allure.tag('API')
@allure.feature('API')
@allure.story('Get user info')
@allure.title('Get non-existing user info')
@allure.link('https://reqres.in/')
def test_get_not_existing_user(base_endpoint):
    response = api_call.send_request('get', base_url=f"{base_endpoint[0]}/{not_existing_user_id}")

    with allure.step('Check response status code == 404'):
        assert response.status_code == 404
    with allure.step('Check response data'):
        assert response.json() == {}
