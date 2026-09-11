import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.header_footer_locators import HeaderFooterLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url

    @staticmethod
    def format_locator(locator_template, value):
        by, locator = locator_template
        return by, locator.format(value)

    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Находим элемент: {locator}')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Находим элементы: {locator}')
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step('Ждём видимость элемента: {locator}')
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ждём, пока элемент станет кликабельным: {locator}')
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Ждём скрытие элемента: {locator}')
    def wait_for_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Ждём видимость элементов: {locator}')
    def find_visible_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step('Кликаем по элементу: {locator}')
    def click_element(self, locator, timeout=10):
        element = self.wait_for_clickable(locator, timeout)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Заполняем поле значением: {value}')
    def send_keys(self, locator, value, timeout=10):
        element = self.wait_for_visibility(locator, timeout)
        element.clear()
        element.send_keys(value)

    @allure.step('Получаем текст элемента: {locator}')
    def get_text(self, locator, timeout=10):
        element = self.wait_for_visibility(locator, timeout)
        return element.text

    @allure.step('Скроллим до элемента: {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    @allure.step('Скроллим страницу вниз')
    def scroll_page_down(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    @allure.step('Принимаем cookies')
    def accept_cookies(self):
        self.click_element(HeaderFooterLocators.COOKIE_BUTTON)

    @allure.step('Переключаемся на вкладку с индексом {tab_index}')
    def switch_to_tab(self, tab_index):
        self.driver.switch_to.window(self.driver.window_handles[tab_index])