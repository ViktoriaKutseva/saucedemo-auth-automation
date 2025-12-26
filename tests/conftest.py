"Pytest configuration and fixtures"

import pytest
from playwright.sync_api import Page
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture to provide a LoginPage object.
    Args:
        page (Page): The Playwright Page object.
    Returns:
        LoginPage: An instance of the LoginPage.
    """
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    """Fixture to provide an InventoryPage object.
    Args:
        page (Page): The Playwright Page object.
    Returns:
        InventoryPage: An instance of the InventoryPage.
    """
    return InventoryPage(page)

@pytest.fixture
def authenticated_page(page: Page, login_page: LoginPage) -> Page:
    """Fixture to provide an authenticated page after login.
    Args:
        page (Page): The Playwright Page object.
        login_page (LoginPage): The LoginPage object.
    Returns:
        Page: The authenticated Playwright Page object.
    """
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return page