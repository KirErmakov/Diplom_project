import allure
from selene.support.shared.jquery_style import s, ss
from appium.webdriver.common.appiumby import AppiumBy


class MainPage:
    @allure.step('Open login form')
    def open_login_form(self):
        s((AppiumBy.ID, 'ru.more.play:id/avatarImageView')).click()

    @allure.step('Go to Catalogue section')
    def go_to_catalogue(self):
        (ss(
            (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="ru.more.play:id/itemBottomMenuImageView"]')).
         element(1).click())

    @allure.step('Go to Shop section')
    def go_to_shop(self):
        (ss(
            (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="ru.more.play:id/itemBottomMenuImageView"]')).
         element(2).click())


main_page = MainPage()
