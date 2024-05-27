import allure
from selene import be
from selene.support.shared.jquery_style import s
from appium.webdriver.common.appiumby import AppiumBy


class LoginForm:

    def __init__(self):
        self.login_button = s((AppiumBy.ID, 'ru.more.play:id/profileLoginButton'))
        self.email_input_field = s((AppiumBy.ID, 'ru.more.play:id/singleAuthorizationEditText'))
        self.register_button = s((AppiumBy.ID, 'ru.more.play:id/singleAuthorizationEnterButton'))
        self.code_message = s((AppiumBy.XPATH, '//android.widget.TextView[@text="Введите код из письма"]'))

    @allure.step('Enter email into input field')
    def enter_email(self, email):
        self.login_button.click()
        self.email_input_field.type(email)

    @allure.step('Register with entered email')
    def register_with_email(self):
        self.register_button.click()

    @allure.step('Check the code message is displayed')
    def check_code_message(self):
        self.code_message.should(be.visible)


login_form = LoginForm()
