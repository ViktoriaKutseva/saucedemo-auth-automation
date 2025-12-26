"Base Page class with common functions for all pages."

from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        """Initialize the BasePage.
        Args:
            page (Page): The Playwright Page object.
        """
        self.page = page

    def navigate_to(self, url: str):
        """Navigate to a specified URL.
        Args:
            url (str): The URL to navigate to.
        """
        self.page.goto(url)
    
    def get_url(self) -> str:
        """Get the current URL of the page.
        Returns:
            str: The current URL.
        """
        return self.page.url
    
    def get_title(self) -> str:
        """Get the title of the current page.
        Returns:
            str: The page title.
        """
        return self.page.title()
    
    def take_screenshot(self, path: str):
        """Take a screenshot of the current page.
        Args:
            path (str): The file path to save the screenshot.
        """
        self.page.screenshot(path=path)

    