from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.logs import log_selenium_actions
from .base_page import BasePage


class MainPage(BasePage):
    ALL_ABOUT_COMPANY_LOCATOR = (By.CSS_SELECTOR, "a.sbisru-Menu-items__header[href='/profile']")

    @log_selenium_actions
    def click_link_all_about_company(self):
        return self.click(self.ALL_ABOUT_COMPANY_LOCATOR)
