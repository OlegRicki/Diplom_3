from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, '//p[text()="Конструктор"]')
    ORDER_FEED_TAB = (By.XPATH, '//p[text()="Лента Заказов"]')
    MODAL_WINDOW = (By.XPATH, '(//div[contains(@class, "Modal_modal__container")])[1]')
    BUTTON_CLOSE_MODAL = (By.XPATH, '(//button[@type="button"])[1]')
    DRAG__INGREDIENT = (By.XPATH, '//span[text()="Перетяните булочку сюда (верх)"]')
    BUN_IMG = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    ONE_COUNTER = (By.XPATH, '(//p[contains(@class, "counter_counter__num__3nue1")])[1]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    TEXT_ORDER_FEED = (By.XPATH, '//h1[text()="Лента заказов"]')

