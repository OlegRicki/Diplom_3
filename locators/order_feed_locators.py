from selenium.webdriver.common.by import By


class OrderFeedLocators:
    FIRST_ORDER = (By.XPATH, '(//a[contains(@class, "OrderHistory_")])[1]')
    MODAL_WINDOW = (By.XPATH, '//div[contains(@class, " Modal_modal__contentBox__")]')
    FIRST_ORDER_NAME = (By.XPATH, '(//h2[contains(@class, "text text_type_main-medium mb-2")])[1]')
    FIRST_ORDER_NUMBER = (By.XPATH, '(//p[contains(@class, "text text_type_digits-default")])[1]')
    COUNTER_ALL_TIME = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')
    COUNTER_FOR_TODAY = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')
    IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li[contains(@class, "text")][1]')


