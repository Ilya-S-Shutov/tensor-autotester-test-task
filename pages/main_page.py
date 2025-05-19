from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from base_page import BasePage


class MainPage(BasePage):
    TEXT_LINK_ALL_ABOUT_COMPANY_LOCATOR = (By.LINK_TEXT, 'Все о компаниях')

    def click_link_all_about_company(self):
        return self.click(self.TEXT_LINK_ALL_ABOUT_COMPANY_LOCATOR)
