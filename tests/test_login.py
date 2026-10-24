import logging

import pytest

from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    ("username", "password", "expected_message"),
    [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
        ("wrong-user", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "wrong-password", "Your password is invalid!"),
    ],
    ids=["valid-user", "invalid-username", "invalid-password"],
)
def test_login_variants(driver, username, password, expected_message):
    logger.info("Executing login scenario: %s", expected_message)
    page = LoginPage(driver)
    page.open()

    page.login(username, password)

    message = page.get_flash_message()
    assert expected_message in message


def test_logout_successfully(driver):
    logger.info("Starting logout scenario")
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_as_valid_user()

    secure_page = SecureAreaPage(driver)
    secure_page.logout()

    assert "You logged out of the secure area!" in login_page.get_flash_message()
