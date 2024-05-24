from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
import allure
from selenium.common import NoSuchElementException


class MainPage:

    def __init__(self):
        self.registration_form = s('a[test-id="nav_sign"]')
        self.registration_option = s(f'[test-id="sign_"]')
        self.search_button = s('[test-id="nav_search"]')
        self.search_input_field = s('[test-id="nav_search_input"]')
        self.sections = ss('[test-id="rail_tab_item"]')
        self.page_title = s('[test-id="collection_page_title"]')
        self.collection_of_elements = ss('[test-id="search_collection_element"]')
        self.category = s('[test-id="search_collection_element"]')
        self.film_genre = s('[test-id="meta_genre"]')
        self.registration_options = ['sber', 'vk', 'google', 'yandex', 'ok']
        self.registration_elements = [s(f'[test-id="sign_{option}"]') for option in self.registration_options]

    @allure.step('Open browser')
    def open(self):
        browser.open('/')

    @allure.step('Open registration form')
    def open_registration_form(self):
        self.registration_form.click()

    @allure.step('Check all registration options are available')
    def check_registration_options_available(self):
        for element in self.registration_elements:
            element.should(be.visible.and_(be.clickable))

    @allure.step('Search film by title')
    def search_film_by_title(self, film_title):
        self.search_button.click()
        self.search_input_field.should(be.blank).type(film_title).press_enter()

    @allure.step('Check search result')
    def check_result(self, film_title):
        try:
            self.collection_of_elements.element_by(have.text(film_title)).should(
                be.visible.and_(be.clickable))
        except NoSuchElementException:
            print(f'Search for the request:{film_title} did not find anything')

    @allure.step('Go to selected section')
    def go_to_selected_section(self, section_name):
        self.sections.element_by(have.exact_text(section_name)).click()

    @allure.step('Verify section name')
    def check_section_name(self, section_name):
        self.page_title.should(have.exact_text(section_name))

    @allure.step('Go to selected films genre section')
    def go_to_selected_films_genre(self, genre):
        self.collection_of_elements.element_by(have.exact_text(genre)).click()
        self.page_title.should(have.exact_text(genre))

    @allure.step('Check film in section has selected genre')
    def check_first_film_has_selected_genre(self, genre):
        self.collection_of_elements.first.click()
        self.film_genre.should(have.exact_text(genre))

    @allure.step('Go to selected category of films')
    def go_to_selected_category(self, category):
        self.category.s(f'//span[text()="{category}"]').click()

    @allure.step('Check category title')
    def check_category_title(self, category):
        self.page_title.should(have.exact_text(category))


main_page = MainPage()
