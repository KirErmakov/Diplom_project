from selene import be
from selene.support.shared.jquery_style import ss, s
from appium.webdriver.common.appiumby import AppiumBy
import allure


class ShopPage:

    @allure.step('Purchase film')
    def buy_film(self):
        ss((AppiumBy.XPATH, '//android.widget.ImageView')).element(2).click()
        s((AppiumBy.ID, 'ru.more.play:id/contentCardPrimaryButton')).should(be.visible.and_(be.clickable))


shop_page = ShopPage()
