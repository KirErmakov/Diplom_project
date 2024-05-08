import pytest
import allure
from allure_commons.types import Severity
from okko.web_pages.main_page import main_page
from okko.web_pages.registration_form import registration_from


class TestRegistrationForm:
    @pytest.mark.positive
    @allure.tag('UI')
    @allure.feature('Registration with email')
    @allure.title('Register with valid email')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
    def test_registration_with_valid_email(self):
        main_page.open()
        main_page.open_registration_form()
        valid_email = 'test@gmail.com'

        registration_from.register_with_email(valid_email)

    @pytest.mark.negative
    @allure.tag('UI')
    @allure.feature('Registration with email')
    @allure.title('Register with invalid email')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
    def test_registration_with_invalid_email(self):
        main_page.open()
        main_page.open_registration_form()
        invalid_email = 'test@gmailcom'

        registration_from.register_with_email(invalid_email, email_valid=False)
