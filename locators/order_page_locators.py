from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    SURNAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_VISIBLE = (
        By.XPATH,
        '//*[@role="menuitem" and contains(@class, "select-search__row")]'
    )
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = (By.XPATH, '//button[contains(., "Далее")]')

    # Форма "Про аренду"
    DATE_INPUT = (
        By.XPATH,
        '//input[@placeholder="* Когда привезти самокат"]'
    )
    RENTAL_DURATION_DROPDOWN = (
        By.XPATH,
        '//div[contains(@class, "Dropdown-control")]'
    )
    RENTAL_DURATION_OPTION = (
        By.XPATH,
        '//div[contains(@class, "Dropdown-menu")]//div[normalize-space()="{}"]'
    )

    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder, 'Комментарий')]"
    )

    ORDER_BUTTON = (
        By.XPATH,
        '//button[contains(., "Заказать") and contains(@class, "Button_Middle")]'
    )

    # Подтверждение заказа
    CONFIRM_BUTTON = (
        By.XPATH,
        '//button[contains(., "Да") and contains(@class, "Button_Button")]'
    )

    # Окно успешного заказа
    STATUS_WINDOW = (
        By.XPATH,
        '//div[contains(@class, "Order_ModalHeader")]'
    )