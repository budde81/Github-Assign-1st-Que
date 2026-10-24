from __future__ import annotations

import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class SecureAreaPage(BasePage):
    """Page object for the secure area visible after successful login."""

    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")
    FLASH_MESSAGE = (By.ID, "flash")

    def logout(self) -> None:
        logger.info("Logging out from secure area")
        self.click(self.LOGOUT_LINK)

    def get_flash_message(self) -> str:
        return self.read_text(self.FLASH_MESSAGE)

    def is_logged_in(self) -> bool:
        return self.is_element_displayed(self.LOGOUT_LINK)
