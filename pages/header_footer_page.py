import allure

from data import Urls
from locators.header_footer_locators import HeaderFooterLocators
from pages.base_page import BasePage


class HeaderFooterPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open(Urls.MAIN_PAGE)

    @allure.step('Кликаем по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_element(HeaderFooterLocators.SAMOKAT_LOGO)
        return self.current_url

    @allure.step('Переходим по логотипу Яндекса')
    def go_to_yandex_from_logo(self):
        self.click_element(HeaderFooterLocators.YANDEX_LOGO)
        self.switch_to_tab(1)

    @allure.step('Проверяем отображение логотипа Дзена')
    def is_dzen_logo_displayed(self):
        return self.wait_for_visibility(
            HeaderFooterLocators.DZEN_LOGO
        ).is_displayed()