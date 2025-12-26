"Login Page class for Sauce Demo"

from allure import step
from playwright.sync_api import Page

from src.pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    ERROR_CLOSE_BUTTON = ".error-button"

    def __init__(self, page: Page):
        """Initialize the LoginPage.
        Args:
            page (Page): The Playwright Page object.
        """
        super().__init__(page)

    @step("Open the login page")
    def open(self) -> "LoginPage":
        """Navigate to the login page."""
        self.navigate_to(self.URL)
        return self
    
    @step("Fill in the username input field")
    def fill_username(self, username: str) -> "LoginPage":
        """Fill in the username input field.
        Args:
            username (str): The username to enter.
        """
        self.page.locator(self.USERNAME_INPUT).fill(username)
        return self
    
    @step("Fill in the password input field")
    def fill_password(self, password: str) -> "LoginPage":
        """Fill in the password input field.
        Args:
            password (str): The password to enter.
        """
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        return self
    
    @step("Click the login button")
    def click_login(self) -> None:
        """Click the login button."""
        self.page.locator(self.LOGIN_BUTTON).click()
    
    @step("Perform the login action with given credentials")
    def login(self, username: str, password: str) -> None:
        """Perform the login action with given credentials.
        Args:
            username (str): The username to enter.
            password (str): The password to enter.
        """
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
    
    @step("Check if error message is visible")
    def is_error_message_displayed(self) -> bool:
        """
        Check if error message is visible.
        
        Returns:
            True if error message is displayed
        """
        return self.page.locator(self.ERROR_MESSAGE).is_visible()

    @step("Get the text of the error message")
    def get_error_message_text(self) -> str:
        """Get the text of the error message.
        Returns:
            str: The error message text.
        """
        return self.page.locator(self.ERROR_MESSAGE).inner_text()
    
    @step("Close the error message if it is displayed")
    def close_error_message(self) -> "LoginPage":
        """Close the error message if it is displayed.
        Returns:
            LoginPage: The current LoginPage instance.
        """
        if self.is_error_message_displayed():
            self.page.locator(self.ERROR_CLOSE_BUTTON).click()
        return self
    
    @step("Check if the current page is the login page")
    def is_on_login_page(self) -> bool:
        """Check if the current page is the login page.
        Returns:
            bool: True if on the login page, False otherwise.
        """
        return self.get_url() == self.URL