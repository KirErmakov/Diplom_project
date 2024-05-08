import allure
from allure_commons.types import Severity
from okko.mobile_pages.main_page import main_page
from okko.mobile_pages.shop_page import shop_page


@allure.tag('Mobile')
@allure.feature('Mobile')
@allure.story('Purchase film from shop')
@allure.title('Purchase film')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_buy_film():
    main_page.go_to_shop()

    shop_page.buy_film()
