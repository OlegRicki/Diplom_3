import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from constants import Constants

constants = Constants()


@pytest.fixture(scope='session')
def driver():
    browser_options = Options()
    browser_options.add_argument("start-maximized")

    driver = webdriver.Chrome(options=browser_options)
    driver.get(constants.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def authorization(driver):
    login_page = LoginPage(driver)
    login_page.authorization(email=constants.EMAIL, password=constants.PASSWORD)
