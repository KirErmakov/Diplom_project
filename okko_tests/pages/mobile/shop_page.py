from selene import be
from selene.support.shared.jquery_style import ss, s
from appium.webdriver.common.appiumby import AppiumBy
import allure


class ShopPage:

    def __init__(self):
        self.film_card = ss((AppiumBy.XPATH, '//android.widget.ImageView')).element(2)
        self.purchase_button = s((AppiumBy.ID, 'ru.more.play:id/contentCardPrimaryButton'))

    @allure.step('Go to paid film card')
    def open_paid_film_card(self):
        self.film_card.click()

    @allure.step('Verify the purchase option')
    def check_purchase_option(self):
        self.purchase_button.should(be.visible.and_(be.clickable))


shop_page = ShopPage()
