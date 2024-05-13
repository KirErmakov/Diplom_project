from selene import be
from selene.support.shared.jquery_style import s
from appium.webdriver.common.appiumby import AppiumBy
import allure
from selenium.common import NoSuchElementException


class CataloguePage:

    @allure.step('Search film by title')
    def search_film(self, film_title):
        s((AppiumBy.ID, 'ru.more.play:id/searchEditText')).type(film_title)

    @allure.step('Check search result')
    def check_result(self, film_title):
        try:
            s((AppiumBy.ACCESSIBILITY_ID, f'{film_title}')).should(be.visible.and_(be.clickable))

        except NoSuchElementException:
            print(f'Search for the request:{film_title} did not find anything')


catalogue = CataloguePage()
