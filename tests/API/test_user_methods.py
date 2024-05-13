import allure
from reqres_tests.test_data.data import data_for_post, data_for_update
from reqres_tests.request_helper.api_call import api_call
from reqres_tests.utils.json_validator import validate_schema


@allure.tag('API')
@allure.feature('API')
@allure.story('Create user')
@allure.title('Create new user')
@allure.link('https://reqres.in/')
def test_create_user(base_endpoint):
    response = api_call.send_request('post', base_url=base_endpoint[0], payload=data_for_post)

    with allure.step('Check response status code == 200'):
        assert response.status_code == 201
    with allure.step('Check response data'):
        assert response.json()["name"] == data_for_post["name"]
        assert response.json()["job"] == data_for_post["job"]
    with allure.step('Validate JSON schema'):
        validate_schema(response.json(), 'create_user.json')


@allure.tag('API')
@allure.feature('API')
@allure.story('Update user')
@allure.title('Update existing user')
@allure.link('https://reqres.in/')
def test_update_user(base_endpoint):
    response = api_call.send_request('put', base_url=f"{base_endpoint[0]}/2", payload=data_for_update)

    with allure.step('Check response status code == 200'):
        assert response.status_code == 200
    with allure.step('Check response data'):
        assert response.json()["name"] == data_for_update["name"]
        assert response.json()["job"] == data_for_update["job"]
    with allure.step('Validate JSON schema'):
        validate_schema(response.json(), 'update_user.json')


@allure.tag('API')
@allure.feature('API')
@allure.story('Delete user')
@allure.title('Delete existing user')
@allure.link('https://reqres.in/')
def test_delete_user(base_endpoint):
    response = api_call.send_request('delete', base_url=f"{base_endpoint[0]}/2")

    with allure.step('Check response status code == 204'):
        assert response.status_code == 204
    with allure.step('Check response data'):
        assert response.text == ''
