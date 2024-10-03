from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        # Opens the specified URL in the browser.
        self.driver.get(url)

    def accept_cookies(self, timeout=10):
        # Clicks the 'Accept Cookies' button if it is available.
        try:
            accept_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='iubenda-cs-accept-btn iubenda-cs-btn-primary']"))
            )
            accept_button.click()
            print("Cookies accepted.")
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Accept cookies failed: {e}")

    def refuse_cookies(self, timeout=10):
        # Clicks the 'Refuse Cookies' button if it is available.
        try:
            refuse_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='iubenda-cs-reject-btn iubenda-cs-btn-primary']"))
            )
            refuse_button.click()
            print("Cookies refused.")
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Refuse cookies failed: {e}")

    def open_cookies(self, timeout=10):
        # Opens the cookie settings menu and verifies the header text.
        try:
            # Wait for the cookie settings button to be clickable
            open_cookies_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='iubenda-cs-customize-btn']"))
            )
            open_cookies_button.click()
            print("Cookies customization opened.")

            # Verify that the cookie customization modal is open
            view_more_header = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='purposes-header']/h2"))
            )

            # Assert that the header text matches the expected value
            assert view_more_header.text == 'Le tue preferenze relative alla privacy', \
                f"Expected 'Le tue preferenze relative alla privacy' but got '{view_more_header.text}'"
            print("Correct header displayed in the cookie preferences.")

            save_and_continue_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='iubFooterBtn']"))
            )
            save_and_continue_button.click()
            print("Cookies customization saved.")

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Open cookies failed: {e}")

    def switch_language(self, timeout=10):
        # Change language from Italian to English.
        try:
            language_option = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='nav-item d-flex justify-content-between "
                                                      "align-items-center']")
                                           ))
            language_option.click(),
            print("Language changed.")
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Refuse cookies failed: {e}")

    def eng_logo(self, timeout=10):
        # Verify the logo is present
        try:
            logo = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@class='logo']"))
            )
            assert logo.is_displayed(), "Logo is not displayed"
            print("Logo verification passed.")
            # Capture the screenshot of the element
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = os.path.join('screenshots', f'logo_screenshot_{timestamp}.png')
            logo.screenshot(screenshot_path)
        except AssertionError as e:
            print(e)

    """Functions to test the links at the navigation bar"""


