import allure
from allure_commons.types import Severity
from models.pages.mobile.main_page import main_page
from models.pages.mobile.shop_page import shop_page


@allure.tag('Mobile')
@allure.feature('Mobile')
@allure.story('Purchase film from shop')
@allure.title('Purchase film')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_buy_film():
    main_page.go_to_shop()

    shop_page.open_paid_film_card()

    shop_page.check_purchase_option()
