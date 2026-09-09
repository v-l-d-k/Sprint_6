import allure
from selenium.webdriver.common.by import By

from data import Urls
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    DATEPICKER = (By.CLASS_NAME, 'react-datepicker')

    @allure.step('Открываем страницу заказа')
    def open_order_page(self):
        self.open(Urls.ORDER_PAGE)

    @allure.step('Нажимаем верхнюю кнопку "Заказать" на главной странице')
    def click_order_from_header(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Нажимаем нижнюю кнопку "Заказать" на главной странице')
    def click_order_from_bottom(self):
        for _ in range(10):
            elements = self.find_elements(
                *MainPageLocators.ORDER_BUTTON_BOTTOM
            )
            if elements and elements[0].is_displayed():
                button = elements[0]
                self.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    button
                )
                self.execute_script("arguments[0].click();", button)
                return

            self.execute_script("window.scrollBy(0, 700);")

        raise Exception('Не удалось найти нижнюю кнопку "Заказать" после прокрутки страницы')

    @allure.step('Заполняем имя')
    def fill_name(self, name):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Заполняем фамилию')
    def fill_surname(self, surname):
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step('Заполняем адрес')
    def fill_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбираем станцию метро: {station_name}')
    def fill_metro_station(self, station_name):
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.select_visible_station(
            OrderPageLocators.METRO_STATION_VISIBLE,
            station_name
        )

    @allure.step('Заполняем телефон')
    def fill_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Нажимаем кнопку "Далее"')
    def click_next_button(self):
        self.scroll_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем дату доставки')
    def fill_date(self, date_string):
        date_input = self.wait_for_visibility(OrderPageLocators.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date_string)
        self.find_element(By.TAG_NAME, 'body').click()

    @allure.step('Выбираем срок аренды')
    def select_rental_duration(self, duration):
        self.scroll_to_element(OrderPageLocators.RENTAL_DURATION_DROPDOWN)
        self.click_element(OrderPageLocators.RENTAL_DURATION_DROPDOWN)

        duration_option_locator = (
            By.XPATH,
            OrderPageLocators.RENTAL_DURATION_OPTION[1].format(duration)
        )
        self.scroll_to_element(duration_option_locator)
        self.click_element(duration_option_locator)

    @allure.step('Выбираем цвет самоката')
    def select_scooter_color(self, color):
        if color == 'black':
            self.click_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        elif color == 'grey':
            self.click_element(OrderPageLocators.COLOR_GREY_CHECKBOX)

    @allure.step('Заполняем комментарий для курьера')
    def fill_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_first_form(self, order_data):
        self.fill_name(order_data['name'])
        self.fill_surname(order_data['surname'])
        self.fill_address(order_data['address'])
        self.fill_metro_station(order_data['metro'])
        self.fill_phone(order_data['phone'])

    @allure.step('Заполняем форму "Про аренду"')
    def fill_second_form(self, order_data):
        self.fill_date(order_data['date'])
        self.select_rental_duration(order_data['duration'])
        self.select_scooter_color(order_data['color'])
        self.fill_comment(order_data['comment'])

    @allure.step('Нажимаем кнопку "Заказать" в форме аренды')
    def click_order_button(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтверждаем заказ')
    def click_confirm_button(self):
        self.wait_for_visibility(OrderPageLocators.CONFIRM_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Подтверждение оформления заказа')
    def submit_order(self):
        self.click_order_button()
        self.click_confirm_button()

    @allure.step('Создание заказа через верхнюю кнопку "Заказать"')
    def create_order_from_header(self, order_data):
        self.accept_cookies()
        self.click_order_from_header()
        self.fill_first_form(order_data)
        self.click_next_button()
        self.fill_second_form(order_data)
        self.submit_order()

    @allure.step('Создание заказа через нижнюю кнопку "Заказать"')
    def create_order_from_bottom(self, order_data):
        self.accept_cookies()
        self.click_order_from_bottom()
        self.fill_first_form(order_data)
        self.click_next_button()
        self.fill_second_form(order_data)
        self.submit_order()

    @allure.step('Проверяем отображение окна "Заказ оформлен"')
    def check_order_status_window(self):
        return self.wait_for_visibility(OrderPageLocators.STATUS_WINDOW) is not None

    @allure.step('Выбираем станцию метро')
    def select_visible_station(self, locator, station_name):
        stations = self.find_visible_elements(locator)

        for station in stations:
            if station.text.strip() == station_name:
                station.click()
                break