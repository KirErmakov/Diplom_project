import allure
from selene import be
from selene.support.shared.jquery_style import s
from appium.webdriver.common.appiumby import AppiumBy


class LoginForm:

    @allure.step('Enter email into input field')
    def enter_email(self, email):
        s((AppiumBy.ID, 'ru.more.play:id/profileLoginButton')).click()
        s((AppiumBy.ID, 'ru.more.play:id/singleAuthorizationEditText')).type(email)

    @allure.step('Register with entered email')
    def register_with_email(self):
        s((AppiumBy.ID, 'ru.more.play:id/singleAuthorizationEnterButton')).click()
        s((AppiumBy.XPATH, '//android.widget.TextView[@text="Введите код из письма"]')).should(be.visible)


login_form = LoginForm()
