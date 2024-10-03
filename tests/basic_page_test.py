import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.basic_page import BasicPage


# Pytest fixture to set up and tear down the WebDriver
@pytest.fixture
def driver():
    # Set up the Chrome WebDriver with the Service class
    service = Service('C:\\Users\\CRS\\Downloads\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver  # Return the driver instance
    driver.quit()  # Ensure the driver quits after the test


def test_basic_page(driver):
    basic_page = BasicPage(driver)
    basic_page.open_page("https://www.eng.it/")
