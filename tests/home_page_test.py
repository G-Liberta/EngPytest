from pages.home_page import HomePage
from config import BASE_URL


def test_open_cookies(driver):
    """Test case for opening the cookie customization, validating if the correct window is opened
    and then saving and closing the window"""
    basic_page = HomePage(driver)
    basic_page.open_page(BASE_URL)
    basic_page.open_cookies()  # Validate opening the cookie preferences


def test_accept_cookies(driver):
    """Test case for accepting cookies."""
    basic_page = HomePage(driver)
    basic_page.open_page(BASE_URL)
    basic_page.accept_cookies()  # Validate accepting cookies


def test_refuse_cookies(driver):
    """Test case for refusing cookies."""
    basic_page = HomePage(driver)
    basic_page.open_page(BASE_URL)
    basic_page.refuse_cookies()  # Validate refusing cookies


def test_verify_logo(driver):
    """Test case for verifying presence of logo and taking a screenshot."""
    basic_page = HomePage(driver)
    basic_page.open_page(BASE_URL)
    basic_page.accept_cookies()  # Validate accepting cookies
    basic_page.eng_logo()


def test_change_language(driver):
    """Test case for changing the language from Italian to English"""
    home_page = HomePage(driver)
    home_page.open_page(BASE_URL)
    home_page.accept_cookies()  # Accept cookies before proceeding
    home_page.switch_language()
