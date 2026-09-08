from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_TEMPLATE = (By.XPATH, "//div[@id='accordion__heading-{0}']")
    ANSWER_TEMPLATE = (By.XPATH, "//div[@id='accordion__panel-{0}']")

    ORDER_BUTTON_HEADER = (
        By.XPATH,
        '//div[contains(@class, "Header_Nav")]'
        '//button[normalize-space()="Заказать"]'
    )

    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        '//div[contains(@class, "Home_FinishButton__")]'
        '/button[normalize-space()="Заказать"]'
    )