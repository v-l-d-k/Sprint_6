import pytest
from selenium import webdriver

from data import Urls


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.MAIN_PAGE)

    yield driver

    driver.quit()