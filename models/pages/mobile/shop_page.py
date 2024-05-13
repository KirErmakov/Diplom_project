from selene import be
from selene.support.shared.jquery_style import ss, s
from appium.webdriver.common.appiumby import AppiumBy
import allure


class ShopPage:

    @allure.step('Go to paid film card')
    def open_paid_film_card(self):
        ss((AppiumBy.XPATH, '//android.widget.ImageView')).element(2).click()

    @allure.step('Verify the purchase option')
    def check_purchase_option(self):
        s((AppiumBy.ID, 'ru.more.play:id/contentCardPrimaryButton')).should(be.visible.and_(be.clickable))


shop_page = ShopPage()
