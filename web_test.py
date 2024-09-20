
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.google_home_page import GoogleHomePage


def test_google_search():
    # Set up the Chrome WebDriver with the Service class
    service = Service('C:\\Users\\CRS\\Downloads\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # Initialize the GoogleHomePage object
    google_home_page = GoogleHomePage(driver)

    # Load the Google homepage
    google_home_page.load()

    # Enter the search term and submit
    google_home_page.enter_search_term("Selenium Python")
    google_home_page.submit_search()

    # Wait for the title to contain "Selenium Python"
    WebDriverWait(driver, 10).until(EC.title_contains("Selenium Python"))

    # Assert that the title contains "Selenium Python"
    assert "Selenium Python" in driver.title

    # Close the browser
    driver.quit()