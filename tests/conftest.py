"Pytest configuration and fixtures"

import os

import allure
import pytest
from playwright.sync_api import BrowserContext, Page

from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def trace_on_failure(context: BrowserContext, request):
    """Fixture to record trace on test failure and attach to Allure."""
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    # Check if the test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        trace_path = f"trace_{request.node.name}.zip"
        context.tracing.stop(path=trace_path)
        allure.attach.file(
            trace_path, 
            name="Playwright Trace: View at https://trace.playwright.dev/", 
            attachment_type="application/zip",
            
        )
        # Clean up the file after attaching
        if os.path.exists(trace_path):
            os.remove(trace_path)
    else:
        context.tracing.stop()


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