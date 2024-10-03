import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.home_page import BasicPage

# variables
CHROME_DRIVER_PATH = 'C:\\Users\\CRS\\Downloads\\chromedriver-win64\\chromedriver.exe'
url = "https://www.eng.it/"

# Pytest fixture to set up and tear down the WebDriver
@pytest.fixture
def driver():
    # Set up and tear down the Chrome Driver
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver  # Return the driver instance
    driver.quit()  # Ensure the driver quits after the test


def test_open_cookies(driver):
    """Test case for opening the cookie customization, validating if the correct window is opened
    and then saving and closing the window"""
    basic_page = BasicPage(driver)
    basic_page.open_page(url)
    basic_page.open_cookies()  # Validate opening the cookie preferences


def test_accept_cookies(driver):
    """Test case for accepting cookies."""
    basic_page = BasicPage(driver)
    basic_page.open_page(url)
    basic_page.accept_cookies()  # Validate accepting cookies


def test_refuse_cookies(driver):
    """Test case for refusing cookies."""
    basic_page = BasicPage(driver)
    basic_page.open_page(url)
    basic_page.refuse_cookies()  # Validate refusing cookies


def test_verify_logo(driver):
    """Test case for verifying presence of logo and taking a screenshot."""
    basic_page = BasicPage(driver)
    basic_page.open_page(url)
    basic_page.accept_cookies()  # Validate accepting cookies
    basic_page.eng_logo()
