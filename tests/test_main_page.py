import allure
import pytest

from data import FaqData
from pages.main_page import MainPage


@allure.suite('Проверка блока FAQ')
class TestMainPageFaq:

    @allure.title('Проверка текста ответов на все вопросы FAQ')
    @allure.description(
        'Принимаем cookies, поочерёдно открываем каждый вопрос в блоке FAQ '
        'и сравниваем текст ответа с ожидаемым значением из данных.'
    )
    @pytest.mark.parametrize(
        'index, expected_question, expected_answer',
        [
            (i, item[0], item[1])
            for i, item in enumerate(FaqData.FAQ_ITEMS)
        ]
    )
    def test_questions_and_answers(self, driver, index, expected_question, expected_answer):
        main_page = MainPage(driver)

        with allure.step('Принимаем cookies'):
            main_page.accept_cookies()

        with allure.step(f'Открываем вопрос "{expected_question}" и получаем ответ'):
            actual_answer_text = main_page.get_answer_text(index)

        with allure.step('Проверяем, что текст ответа совпадает с ожидаемым'):
            assert actual_answer_text == expected_answer, (
                f'Ожидали ответ: "{expected_answer}", '
                f'получили: "{actual_answer_text}"'
            )