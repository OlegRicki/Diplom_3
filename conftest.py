import pytest
from browser_factory import BrowserFactory
from pages.login_page import LoginPage
from api.api_base import ApiBase
from generations import generate_user_name
from constants import Constants

constants = Constants()
test_user_name = generate_user_name()
test_email = 'oleqrezni4enko@yandex.ru'
test_password = 'olegoleg'


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def driver(request):
    driver = BrowserFactory.get_browser(request.param)

    driver.get(constants.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def create_user_and_authorization(driver):
    api_base = ApiBase()
    email, password, access_token = api_base.create_new_user(username=test_user_name, password=test_password,
                                                             email=test_email)
    login_page = LoginPage(driver)
    login_page.authorization(email=email, password=password)

    yield email, password, access_token

    api_base.delete_user(access_token=access_token)


@pytest.fixture
def create_order(driver, create_user_and_authorization):
    email, password, access_token = create_user_and_authorization
    api_base = ApiBase()
    order_number = api_base.create_order_authorization_user(access_token=access_token)
    return order_number
