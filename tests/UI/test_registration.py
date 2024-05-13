import pytest
import allure
from allure_commons.types import Severity
from okko_tests.pages.web.main_page import main_page
from okko_tests.pages.web.registration_form import registration_form


class TestRegistrationForm:
    @pytest.mark.positive
    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('User Registration')
    @allure.title('Register with valid email')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
    def test_registration_with_valid_email(self, generate_email):
        main_page.open()
        main_page.open_registration_form()

        registration_form.enter_email(generate_email)

        registration_form.check_registration_result()

    @pytest.mark.negative
    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('User Registration')
    @allure.title('Register with invalid email')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
    def test_registration_with_invalid_email(self):
        main_page.open()
        main_page.open_registration_form()
        invalid_email = 'test@gmailcom'

        registration_form.enter_email(invalid_email)

        registration_form.check_registration_result(email_valid=False)
