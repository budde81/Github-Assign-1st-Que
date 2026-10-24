from __future__ import annotations

import logging
from typing import Tuple

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = Tuple[str, str]
logger = logging.getLogger(__name__)


class BasePage:
    """Reusable browser actions and element-access helpers."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url: str) -> None:
        logger.info("Opening URL: %s", url)
        self.driver.get(url)

    def wait_for_element(self, locator: Locator) -> WebElement:
        logger.debug("Waiting for element: %s", locator)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: Locator) -> None:
        element = self.wait_for_element(locator)
        logger.info("Clicking element: %s", locator)
        element.click()

    def type(self, locator: Locator, value: str) -> None:
        element = self.wait_for_element(locator)
        logger.info("Typing into %s with value: %s", locator, value)
        element.clear()
        element.send_keys(value)

    def read_text(self, locator: Locator) -> str:
        text = self.wait_for_element(locator).text
        logger.debug("Read text from %s: %s", locator, text)
        return text

    def is_element_displayed(self, locator: Locator) -> bool:
        try:
            element = self.wait_for_element(locator)
            is_displayed = element.is_displayed()
            logger.debug("Element %s displayed: %s", locator, is_displayed)
            return is_displayed
        except Exception:
            logger.warning("Element not displayed: %s", locator)
            return False

    def find(self, locator: Locator) -> WebElement:
        logger.debug("Finding element: %s", locator)
        return self.driver.find_element(*locator)

    def assert_text_contains(self, locator: Locator, expected_text: str) -> bool:
        message = self.read_text(locator)
        logger.info("Checking text %s in %s", expected_text, locator)
        return expected_text in message
