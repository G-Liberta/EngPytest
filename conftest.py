# A common file in the root directory where all test files can access the same fixture
# without repeating of having the driver() fixture in every test file.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# variables
CHROME_DRIVER_PATH = 'C:\\Users\\CRS\\Downloads\\chromedriver-win64\\chromedriver.exe'


# Pytest fixture to set up and tear down the WebDriver
@pytest.fixture
def driver():
    # Set up and tear down the Chrome Driver
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver  # Return the driver instance
    driver.quit()  # Ensure the driver quits after the test
