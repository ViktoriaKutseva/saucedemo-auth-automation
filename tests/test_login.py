"Login tests for the Saucedemo"
import allure
import pytest
from playwright.sync_api import Page

from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage
from tests.conftest import login_page


@allure.epic("SauceDemo Web Application")
@allure.feature("Authentication")
@pytest.mark.smoke
@pytest.mark.login
class TestLogin:
    """Test suite for login functionality."""
    
    @allure.story("Successful Login")
    @allure.title("Test successful login with standard user")
    @allure.description("Test the login functionality with valid credentials for a standard user.")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("critical")
    def test_successful_login_standard_user(self, login_page: LoginPage, inventory_page: InventoryPage):
        """
        Test successful login with standard user.

        Steps:
        1. Open login page
        2. Login with standard_user / secret_sauce
        3. Click login button
        4. Verify redirect to inventory page
        5. Verify inventory container is visible
        6. Verify products are displayed
        """
        with allure.step("Open login page"):
            login_page.open()
            assert login_page.is_on_login_page()
    
        with allure.step("Enter valid credentials and submit"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Verify redirect to inventory page and contents"):
            inventory_page.wait_for_page_load() 
            assert inventory_page.is_on_inventory_page()
        
        with allure.step("Check inventory page contents"):
            assert inventory_page.is_container_displayed()
            product_count = inventory_page.get_product_count()
            assert product_count == 6, f"Expected 6 products, found {product_count}"

    @allure.story("Invalid Login")
    @allure.title("Test login attempt with invalid password")
    @allure.description("Test the login functionality with an invalid password for a standard user.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("validation")
    def test_login_with_invalid_password(self, login_page: LoginPage):
        """
        Test login attempt with invalid password.
        Steps:
        1. Open login page
        2. Enter valid username but wrong password
        3. Click login button
        4. Verify error message is displayed
        5. Verify error message text
        6. Verify still on login page
        """
        with allure.step("Open login page"):
            login_page.open()
            assert login_page.is_on_login_page()

        with allure.step("Enter valid username but invalid password"):
            login_page.login("standard_user", "wrong_password")

        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed()
            expected_error = "Epic sadface: Username and password do not match any user in this service"
            actual_error = login_page.get_error_message_text()
            assert actual_error == expected_error, f"Expected error message: '{expected_error}', but got: '{actual_error}'"
    
        with allure.step("Verify still on login page"):
            assert login_page.is_on_login_page()

    @allure.story("Locked Out User Login")
    @allure.title("Test login attempt with locked out user")
    @allure.description("Test the login functionality with a locked out user.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("validation", "security")
    def test_login_locked_out_user(self, login_page: LoginPage):
        """
        Test login attempt with locked out user.
        Steps:
        1. Open login page
        2. Enter locked out username and valid password
        3. Click login button
        4. Verify error message is displayed
        5. Verify error message text
        6. Verify still on login page
        """
        with allure.step("Open login page"):
            login_page.open()
            assert login_page.is_on_login_page()

        with allure.step("Enter locked out user credentials"):        
            login_page.login("locked_out_user", "secret_sauce")

        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed()
            expected_error = "Epic sadface: Sorry, this user has been locked out."
            actual_error = login_page.get_error_message_text()
            assert actual_error == expected_error, f"Expected error message: '{expected_error}', but got: '{actual_error}'"

        with allure.step("Verify still on login page"):
            assert login_page.is_on_login_page()

    @allure.story("Empty Fields Login")
    @allure.title("Test login attempt with empty username and password fields")
    @allure.description("Test the login functionality when both username and password fields are left empty.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("validation")
    def test_login_with_empty_fields(self, login_page: LoginPage):
        """
        Test login attempt with empty username and password fields.
        Steps:
        1. Open login page
        2. Leave username and password fields empty
        3. Click login button
        4. Verify error message is displayed
        5. Verify error message text
        6. Verify still on login page
        """
        
        with allure.step("Open login page"):
            login_page.open()
            assert login_page.is_on_login_page()
        
        with allure.step("Enter empty username and password credentials"):        
            login_page.login("", "")

        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed()
            expected_error = "Epic sadface: Username is required"
            actual_error = login_page.get_error_message_text()
            assert actual_error == expected_error, f"Expected error message: '{expected_error}', but got: '{actual_error}'"

        with allure.step("Verify still on login page"):
            assert login_page.is_on_login_page() 

    @allure.story("Performance Testing")
    @allure.title("Test login with performance glitch user")
    @allure.description(
        """
        Verify that the application handles slow-loading scenarios gracefully.
        The performance_glitch_user experiences intentional delays.
        """
    )
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("performance", "positive")
    @pytest.mark.slow
    def test_login_with_performance_glitch_user(self, login_page: LoginPage, inventory_page: InventoryPage):
        """
        Test successful login with performance glitch user.
        Steps:
        1. Open login page
        2. Login with performance_glitch_user / secret_sauce
        3. Click login button
        4. Verify redirect to inventory page
        5. Verify inventory container is visible
        6. Verify products are displayed
        """
        with allure.step("Open login page"):
            login_page.open()
            assert login_page.is_on_login_page()

        with allure.step("Enter performance glitch user and password credentials"):
            login_page.login("performance_glitch_user", "secret_sauce")
            inventory_page.wait_for_page_load() 

        with allure.step("Verify redirect to inventory page and contents"):
            assert inventory_page.is_on_inventory_page()
            assert "inventory.html" in inventory_page.get_url()

        with allure.step("Check inventory page contents"):
            assert inventory_page.is_container_displayed()
            product_count = inventory_page.get_product_count()
            assert product_count == 6, f"Expected 6 products, found {product_count}"
