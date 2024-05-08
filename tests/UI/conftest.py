import pytest
import allure
from utils import attach
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Select browser: Chrome or Firefox')


@pytest.fixture(scope='function', autouse=True)
def manage_browser(request):
    browser_name = request.config.getoption('--browser_name')
    options = ChromeOptions() if browser_name.lower() == 'chrome' else FirefoxOptions()

    '''common_options = [
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--disable-extensions',
        '--disable-popup-blocking',
        '--disable-infobars'
    ]
    for option in common_options:
        options.add_argument(option)'''

    driver_class = webdriver.Chrome if browser_name.lower() == 'chrome' else webdriver.Firefox
    browser.config.driver = driver_class(options=options)
    browser.config.base_url = "https://okko.tv"
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    with allure.step('Add screenshot'):
        attach.add_screenshot(browser)

    with allure.step('Add browser logs'):
        attach.add_logs(browser)

    with allure.step('Add HTML'):
        attach.add_html(browser)

    browser.quit()
