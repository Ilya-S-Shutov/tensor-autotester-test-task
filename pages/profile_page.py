from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from base_page import BasePage


class ProfilePage(BasePage):
    SEARCH_FIELD_LOCATOR = ''

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.URL = f'{self.BASE_URL}/profile'

    def update_cookie(self):
        pass

    def use_search(self, query: str) -> None:
        pass
