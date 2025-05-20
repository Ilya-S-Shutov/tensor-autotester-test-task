from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.logs import log_selenium_actions
from .base_page import BasePage
from .company_card_page import CompanyCardPage


class CompanyListPage(BasePage):
    SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[class*="Search"]')
    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'div[data-qa="Search__searchButton"]')
    SEARCH_RESULT_ITEMS_ROW_LOCATOR = (By.XPATH, '//div[@data-qa="row"]//div[@data-qa="contractorMain-listBrowser__cellMain"]')
    INN_LOCATOR = (By.CSS_SELECTOR, 'div[data-qa="row"] div[class*="Inn"] span')
    COMPANY_NAME_LOCATOR = (By.CSS_SELECTOR, 'div[class="contractor-common-Templates__mainCell_Name"]')
    REGION_CITY_LOCATOR = (By.CSS_SELECTOR, 'div[class="contractor-common-Templates__mainCell_RegionCity"]')
    FILTERS_LOCATOR = (By.NAME, 'detailPanelTarget')
    FILTER_FIELDS_LOCATOR = (By.CSS_SELECTOR, 'div[data-qa="FilterPanel__PropertyGrid__item"]')
    FILTER_FIELD_LOCATOR = (By.TAG_NAME, 'input')
    FILTER_SEARCH_LOCATOR = (By.XPATH, '//div[text()="Найти"]')
    BUTTON_EXPAND_LOCATOR = (By.ID, 'iconExpanded')
    CHECKBOX_REGION_LOCATOR = (By.CSS_SELECTOR, 'span[text()="{region}"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.URL = f'{self.BASE_URL}/profile/page/company-list'

    @log_selenium_actions
    def use_search(self, query: str) -> None:
        self.find_element(self.SEARCH_FIELD_LOCATOR).send_keys(query)
        self.click(self.SEARCH_BUTTON_LOCATOR)

    @log_selenium_actions
    def get_items_info(self, amount_items: int = 0) -> list[str]:
        result = []
        items = self.find_elements(self.SEARCH_RESULT_ITEMS_ROW_LOCATOR)
        if amount_items > 0:
            items = items[:amount_items]
        for item in items:
            result.append(item.text)
        return result

    @log_selenium_actions
    def find_company_item_by_name_and_city(self, target_company_name: str, target_city: str) -> WebElement:
        items = self.find_elements(self.SEARCH_RESULT_ITEMS_ROW_LOCATOR)
        for item in items:
            company_name = item.find_element(*self.COMPANY_NAME_LOCATOR).text
            company_city = item.find_element(*self.REGION_CITY_LOCATOR).text
            if target_company_name == company_name and target_city == company_city:
                return item

    @log_selenium_actions
    def find_company_item_by_position(self, position: int) -> WebElement:
        items = self.find_elements(self.SEARCH_RESULT_ITEMS_ROW_LOCATOR)
        return items[position]

    @log_selenium_actions
    def get_inn_of_item(self, target_company_name: str, target_city: str) -> str:
        item = self.find_company_item_by_name_and_city(target_company_name, target_city)
        return item.find_element(*self.INN_LOCATOR).text

    @log_selenium_actions
    def click_on_company_item(self, company_name: str, city: str, index: int | None = None) -> CompanyCardPage:
        if index:
            self.find_company_item_by_position(index).click()
        else:
            self.find_company_item_by_name_and_city(company_name, city).click()
        return CompanyCardPage(self.driver)

    @log_selenium_actions
    def use_region_filter(self, region: str) -> None:
        self.find_element(self.BUTTON_EXPAND_LOCATOR)
        locator = (self.CHECKBOX_REGION_LOCATOR[0], self.CHECKBOX_REGION_LOCATOR[1].format(region=region))
        self.click(locator)

        # self.click(self.NAME_FILTERS_LOCATOR)
        # items = self.find_elements(self.CSS_FILTER_FIELDS_LOCATOR)
        # for item in items:
        #     if 'Регион' in item.text:
        #         item.find_element(*self.TAG_FILTER_FIELD_LOCATOR).send_keys(query)
        #         self.click(self.XPATH_FILTER_SEARCH_LOCATOR)
        #         break








