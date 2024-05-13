import allure
from allure_commons.types import Severity
from models.pages.mobile.main_page import main_page
from models.pages.mobile.catalogue_page import catalogue


@allure.tag('UI Mobile')
@allure.feature('Mobile')
@allure.story('Search film from catalogue')
@allure.title('Search film by title')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_search_film_by_title():
    film_tile = 'Дивергент'
    main_page.go_to_catalogue()

    catalogue.search_film(film_tile)

    catalogue.check_result(film_tile)
