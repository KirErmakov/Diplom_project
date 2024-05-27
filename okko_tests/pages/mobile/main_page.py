import allure
from selene.support.shared.jquery_style import s, ss
from appium.webdriver.common.appiumby import AppiumBy


class MainPage:

    def __init__(self):
        self.login_form_button = s((AppiumBy.ID, 'ru.more.play:id/avatarImageView'))
        self.catalogue = ss(
            (AppiumBy.XPATH,
             '//android.widget.ImageView[@resource-id="ru.more.play:id/itemBottomMenuImageView"]')).element(1)
        self.shop = ss(
            (AppiumBy.XPATH,
             '//android.widget.ImageView[@resource-id="ru.more.play:id/itemBottomMenuImageView"]')).element(2)

    @allure.step('Go to login form')
    def open_login_form(self):
        self.login_form_button.click()

    @allure.step('Go to Catalogue section')
    def go_to_catalogue(self):
        self.catalogue.click()

    @allure.step('Go to Shop section')
    def go_to_shop(self):
        self.shop.click()


main_page = MainPage()
