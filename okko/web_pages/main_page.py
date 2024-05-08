from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
import allure
from selenium.common import NoSuchElementException


class MainPage:
    @allure.step('Open browser')
    def open(self):
        browser.open('/')

    @allure.step('Open registration form')
    def open_registration_form(self):
        s('a[test-id="nav_sign"]').click()

    @allure.step('Check all registration options are available')
    def check_registration_options_available(self):
        registration_options = ['sber', 'vk', 'google', 'yandex', 'ok']

        for option in registration_options:
            s(f'[test-id="sign_{option}"]').should(be.visible.and_(be.clickable))

    @allure.step('Search film by title')
    def search_film_by_title(self, film_title):
        s('[test-id="nav_search"]').click()
        s('[test-id="nav_search_input"]').should(be.blank).type(film_title).press_enter()

        try:
            browser.all('[test-id="search_collection_element"]').element_by(have.text(film_title)).should(
                be.visible.and_(be.clickable))
        except NoSuchElementException:
            print(f'Search for the request:{film_title} did not find anything')

    @allure.step('Go to selected section')
    def go_to_selected_section(self, section_name):
        ss('[test-id="rail_tab_item"]').element_by(have.exact_text(section_name)).click()
        s('[test-id="collection_page_title"]').should(have.exact_text(section_name))

    @allure.step('Go to selected films genre section')
    def go_to_selected_films_genre(self, genre):
        ss('[test-id="search_collection_element"]').element_by(have.exact_text(genre)).click()
        s('[test-id="collection_page_title"]').should(have.exact_text(genre))

    @allure.step('Check film in section has selected genre')
    def check_film_has_selected_genre(self, genre):
        ss('[test-id="search_collection_element"]').first.click()
        s('[test-id="meta_genre"]').should(have.exact_text(genre))

    @allure.step('Go to selected category of films')
    def go_to_selected_category(self, category):
        ss('[test-id="search_collection_element"]').element_by(have.exact_text(category)).click()
        s('[test-id="collection_page_title"]').should(have.exact_text(category))
        ss('[test-id=card_rail_header]').element_by(have.exact_text(category))


main_page = MainPage()
