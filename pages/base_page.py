from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(self.driver)

    def open_page(self, page: str):
        self.driver.get(page)

    def click_to_element(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def wait_displayed_element(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))

    def check_displayed_element(self, locator) -> bool:
        return self.wait.until(ec.visibility_of_element_located(locator)).is_displayed()

    def get_current_url(self):
        url = self.driver.current_url
        return str(url)

    def send_keys(self, locator, data: str):
        self.wait.until(ec.element_to_be_clickable(locator)).send_keys(data)

    def check_not_displayed_element(self, locator):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def get_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def drag_and_drop_element(self, source_element, target_element):
        self.actions.click_and_hold(source_element)
        self.actions.move_to_element(target_element)
        self.actions.release(target_element)
        self.actions.perform()

    def get_text_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text
