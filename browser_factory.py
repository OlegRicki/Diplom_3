from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver


class BrowserFactory:
    @staticmethod
    def get_browser(browser_name):

        if browser_name == 'chrome':
            browser_options = ChromeOptions()
            browser_options.add_argument("start-maximized")
            driver = webdriver.Chrome(options=browser_options)
        elif browser_name == 'firefox':
            browser_options = FirefoxOptions()
            browser_options.add_argument("maximize_window()")
            driver = webdriver.Firefox(options=browser_options)
        else:
            raise ValueError(f'Unknown browser type: {browser_name}')

        if browser_name == 'firefox':
            driver.maximize_window()
        return driver
