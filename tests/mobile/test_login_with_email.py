from allure_commons.types import Severity
from okko.mobile_pages.main_page import main_page
from okko.mobile_pages.login_form import login_form
import allure


@allure.tag('UI Mobile')
@allure.feature('Login with email')
@allure.title('Register with valid email')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_login_with_email(generate_email):
    main_page.open_login_form()

    login_form.enter_email(generate_email)
    login_form.register_with_email()
