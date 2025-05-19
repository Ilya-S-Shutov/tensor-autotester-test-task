from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from base_page import BasePage


class CompanyCardPage(BasePage):
    XPATH_INN_LOCATOR = (By.XPATH, '//div[@data-qa="ContractorCard-About-ИНН"]/div.contractor-Dialog_INNKPP-pointer')
    TAG_COMPANY_NAME_LOCATOR = (By.TAG_NAME, 'h1')

    def open(self, inn: str, cpp: str) -> None:
        self.URL = f'{self.BASE_URL}/profile/{inn}-{cpp}'
        super().open()

    def get_company_inn(self) -> str:
        return self.find_element(self.XPATH_INN_LOCATOR).text

    def get_company_name(self) -> str:
        return self.find_element(self.TAG_COMPANY_NAME_LOCATOR).text


