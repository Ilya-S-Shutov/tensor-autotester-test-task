from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.logs import log_selenium_actions


class BasePage:
    BASE_URL = 'https://saby.ru/'
    URL = BASE_URL

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @log_selenium_actions
    def open(self) -> None:
        self.driver.get(self.URL)

    @log_selenium_actions
    def find_element(self, locator: tuple[str, str]) -> WebElement | str:
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Can't find element by locator {locator}.")

    @log_selenium_actions
    def find_elements(self, locator: tuple[str, str]) -> list[WebElement] | str:
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Can't find elements by locator {locator}.")

    @log_selenium_actions
    def click(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator),
                               message=f"Can't find element by locator {locator}.").click()

    @log_selenium_actions
    def add_cookie(self, name: str, value: str, **cookie_options) -> None:
        cookie_options['name'] = name
        cookie_options['value'] = value
        self.driver.add_cookie(cookie_options)
        self.refresh()

    @log_selenium_actions
    def refresh(self) -> None:
        self.driver.refresh()

    @log_selenium_actions
    def get_current_url(self) -> str:
        return self.driver.current_url
