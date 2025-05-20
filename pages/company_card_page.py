from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.logs import log_selenium_actions
from .base_page import BasePage


class CompanyCardPage(BasePage):
    INN_LOCATOR = (By.XPATH, '//div[@data-qa="ContractorCard-About-ИНН"]/div.contractor-Dialog_INNKPP-pointer')
    COMPANY_NAME_LOCATOR = (By.TAG_NAME, 'h1')

    @log_selenium_actions
    def open(self, inn: str, cpp: str) -> None:
        self.URL = f'{self.BASE_URL}/profile/{inn}-{cpp}'
        super().open()

    @log_selenium_actions
    def get_company_inn(self) -> str:
        return self.find_element(self.INN_LOCATOR).text

    @log_selenium_actions
    def get_company_name(self) -> str:
        return self.find_element(self.COMPANY_NAME_LOCATOR).text


