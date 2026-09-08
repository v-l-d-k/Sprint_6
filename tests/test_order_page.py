import allure

from data import OrderData
from pages.order_page import OrderPage


@allure.suite('Тестирование оформления заказа')
class TestOrderPage:

    @allure.title('Создание заказа через верхнюю кнопку "Заказать"')
    @allure.description(
        'Позитивный сценарий создания заказа через верхнюю кнопку на главной странице.'
    )
    def test_create_order_from_header(self, driver):
        order_page = OrderPage(driver)

        order_page.create_order_from_header(OrderData.ORDER_FROM_HEADER)

        assert order_page.check_order_status_window(), (
            'Окно с информацией о заказе не появилось '
            'после оформления заказа через верхнюю кнопку.'
        )

    @allure.title('Создание заказа через нижнюю кнопку "Заказать"')
    @allure.description(
        'Позитивный сценарий создания заказа через нижнюю кнопку на главной странице.'
    )
    def test_create_order_from_bottom(self, driver):
        order_page = OrderPage(driver)

        order_page.create_order_from_bottom(OrderData.ORDER_FROM_BOTTOM)

        assert order_page.check_order_status_window(), (
            'Окно с информацией о заказе не появилось '
            'после оформления заказа через нижнюю кнопку.'
        )