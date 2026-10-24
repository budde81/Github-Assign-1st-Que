import logging
import sys
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


@pytest.fixture(scope="function")
def driver():
    """Provide a clean Chrome instance for every test."""
    logging.info("Starting browser session for test")
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(service=Service(), options=chrome_options)
    try:
        yield browser
    finally:
        logging.info("Closing browser session")
        browser.quit()
