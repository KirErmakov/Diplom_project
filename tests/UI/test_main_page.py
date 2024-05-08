from okko.web_pages.main_page import main_page
import allure
from allure_commons.types import Severity


class TestMainPage:
    @allure.tag('UI')
    @allure.feature('Registration options')
    @allure.title('Check registration options')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
    def test_registration_options_available(self):
        main_page.open()

        main_page.open_registration_form()
        main_page.check_registration_options_available()

    @allure.tag('UI')
    @allure.feature('Film search')
    @allure.title('Search film by title')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
    def test_search_film_by_title(self):
        film_title_for_search = 'Дивергент'
        main_page.open()

        main_page.search_film_by_title(film_title_for_search)

    @allure.tag('UI')
    @allure.feature('Web-app sections')
    @allure.title('Check selected section availability')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
    def test_selected_section_available(self):
        section_name = 'Фильмы'
        main_page.open()

        main_page.go_to_selected_section(section_name)

    @allure.tag('UI')
    @allure.feature('Film genre')
    @allure.title('Select film by genre')
    @allure.severity(Severity.NORMAL)
    @allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
    def test_select_film_by_genre(self):
        film_genre = 'Комедии'
        main_page.open()

        main_page.go_to_selected_films_genre(film_genre)
        main_page.check_film_has_selected_genre(film_genre)

    @allure.tag('UI')
    @allure.feature('Film category')
    @allure.title('Select films by category')
    @allure.severity(Severity.NORMAL)
    @allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
    def test_select_category_of_films(self):
        film_category = 'Фильмы'
        main_page.open()

        main_page.go_to_selected_category(film_category)
