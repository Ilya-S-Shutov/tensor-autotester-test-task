from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    BASE_URL = 'https://saby.ru/'
    URL = BASE_URL
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        self.driver.get(self.URL)

    def find_element(self, locator: tuple[str, str]) -> WebElement | str:
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Can't find element by locator {locator}.")

    def find_elements(self, locator: tuple[str, str]) -> list[WebElement] | str:
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Can't find elements by locator {locator}.")

    def click(self, locator: tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator),
                        message=f"Can't find element by locator {locator}.")