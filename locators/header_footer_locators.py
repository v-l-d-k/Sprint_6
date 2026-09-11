from selenium.webdriver.common.by import By


class HeaderFooterLocators:
    # Кнопка принятия cookies
    COOKIE_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )

    # Логотип Яндекса
    YANDEX_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoYandex')]"
    )

    # Логотип Самоката
    SAMOKAT_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoScooter')]"
    )

    # Логотип Дзена
    DZEN_LOGO = (
        By.XPATH,
        '//a[@aria-label="Логотип Бренда"]'
    )