import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open(Urls.MAIN_PAGE)

    @allure.step('Открываем вопрос FAQ с индексом {index} и получаем текст ответа')
    def get_answer_text(self, index):
        question_locator = self.format_locator(
            MainPageLocators.QUESTION_TEMPLATE, index
        )
        answer_locator = self.format_locator(
            MainPageLocators.ANSWER_TEMPLATE, index
        )

        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

        return self.get_text(answer_locator)

    @allure.step('Нажимаем верхнюю кнопку "Заказать" на главной странице')
    def click_order_from_header(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Нажимаем нижнюю кнопку "Заказать" на главной странице')
    def click_order_from_bottom(self):
        self.scroll_page_down()
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)