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


def test_navigation_solutions_modal(driver):
    """Test case for verifying that the 'Solutions' modal is displayed when clicked."""
    home_page = HomePage(driver)
    home_page.open_page(BASE_URL)
    home_page.accept_cookies()
    home_page.switch_language()
    home_page.accept_cookies()
    home_page.click_navigation_link("//span[contains(text(), 'Insights')]")
    home_page.verify_modal_displayed("//div[@id='megamenu-0']")
    # Verify that the sub-options are displayed in the 'Solutions' modal
    home_page.verify_sub_options(
        modal_xpath="//div[@id='megamenu-0']//ul[@class='navbar-h menu-mega__column']",
        sub_option_texts=["Papers", "Stories", "Podcasts", "Events"]
    )

    # Click on 'Markets' sub-option and verify the expected content is loaded/displayed
    home_page.click_sub_option_and_verify_content(
        sub_option_text="Papers",
        expected_content_xpath="//span[@class='heading1']"
    )
