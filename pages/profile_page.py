from selenium.webdriver.remote.webdriver import WebDriver

from utils.logs import log_selenium_actions
from .base_page import BasePage


class ProfilePage(BasePage):
    # SEARCH_FIELD_LOCATOR = (By.CLASS_NAME, '')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.URL = f'{self.BASE_URL}/profile'
    #
    # def add_cookie_abtest_a(self) -> None:
    #     self.add_cookie('abtest-profile', 'A')
    #     self.refresh()

    @log_selenium_actions
    def skip_stage(self) -> None:
        self.driver.get('https://saby.ru/profile/page/company-list')


    # def use_search(self, query: str) -> None:
    #     pass
