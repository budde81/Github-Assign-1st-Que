from __future__ import annotations

import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """Page object for the login form."""

    URL = "https://the-internet.herokuapp.com/login"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    VALID_CREDENTIALS = ("tomsmith", "SuperSecretPassword!")

    def open(self) -> None:
        logger.info("Opening login page")
        super().open(self.URL)

    def login(self, username: str, password: str) -> None:
        logger.info("Attempting login for user: %s", username)
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def login_as_valid_user(self) -> None:
        username, password = self.VALID_CREDENTIALS
        self.login(username, password)

    def get_flash_message(self) -> str:
        return self.read_text(self.FLASH_MESSAGE)

    def is_success_message_present(self) -> bool:
        return self.assert_text_contains(self.FLASH_MESSAGE, "You logged into a secure area!")

    def is_invalid_credentials_message_present(self) -> bool:
        message = self.get_flash_message().lower()
        logger.info("Validating invalid credential message: %s", message)
        return "invalid" in message and ("password" in message or "username" in message)
