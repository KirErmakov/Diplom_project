from allure_commons.types import Severity
from okko_tests.pages.mobile.main_page import main_page
from okko_tests.pages.mobile.login_form import login_form
import allure


@allure.tag('UI Mobile')
@allure.feature('Mobile')
@allure.story('Register with email')
@allure.title('Register with valid email')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_login_with_email(generate_email):
    main_page.open_login_form()

    login_form.enter_email(generate_email)
    login_form.register_with_email()

    login_form.check_code_message()
