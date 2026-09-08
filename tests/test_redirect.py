import allure

from data import Urls
from pages.header_footer_page import HeaderFooterPage


@allure.suite('Проверка переходов по логотипам')
class TestRedirects:

    @allure.title('Переход на главную страницу по логотипу Самоката')
    @allure.description(
        'Проверяем, что при клике на логотип Самоката '
        'происходит переход на главную страницу.'
    )
    def test_redirect_scooter_logo(self, driver):
        header_footer_page = HeaderFooterPage(driver)

        current_url = header_footer_page.click_scooter_logo()

        assert current_url.rstrip('/') == Urls.MAIN_PAGE.rstrip('/'), (
            f'Переход на главную страницу Самоката не выполнен. '
            f'Ожидали: {Urls.MAIN_PAGE}, получили: {current_url}'
        )

    @allure.title('Переход на страницу Дзена по логотипу Яндекса')
    @allure.description(
        'Проверяем, что при клике на логотип Яндекса '
        'открывается страница Дзена в новой вкладке.'
    )
    def test_redirect_yandex_logo(self, driver):
        header_footer_page = HeaderFooterPage(driver)

        header_footer_page.go_to_yandex_from_logo()
        current_url = header_footer_page.current_url

        assert Urls.DZEN_PAGE in current_url, (
            f'Переход на страницу Дзена не выполнен. '
            f'Ожидали URL, содержащий: {Urls.DZEN_PAGE}, получили: {current_url}'
        )

        assert header_footer_page.is_dzen_logo_displayed(), (
            'Логотип Дзена не найден на открывшейся странице'
        )