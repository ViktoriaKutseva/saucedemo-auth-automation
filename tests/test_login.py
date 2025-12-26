"Login tests for the Saucedemo"

import pytest
from playwright.sync_api import Page
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage  

@pytest.mark.smoke
@pytest.mark.login

class TestLogin:
    """Test suite for login functionality."""

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
        login_page.open()
        assert login_page.is_on_login_page()
        
        login_page.login("standard_user", "secret_sauce")
        inventory_page.wait_for_page_load() 

        assert inventory_page.is_on_inventory_page()
        assert "inventory.html" in inventory_page.get_url()
        assert inventory_page.is_container_displayed()

        product_count = inventory_page.get_product_count()
        assert product_count == 6, f"Expected 6 products, found {product_count}"

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
        login_page.open()
        assert login_page.is_on_login_page()
        
        login_page.login("standard_user", "wrong_password")
        
        assert login_page.is_error_message_displayed()
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        actual_error = login_page.get_error_message_text()
        assert actual_error == expected_error, f"Expected error message: '{expected_error}', but got: '{actual_error}'"
        assert login_page.is_on_login_page()

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
        login_page.open()
        assert login_page.is_on_login_page()
        
        login_page.login("locked_out_user", "secret_sauce")
        
        assert login_page.is_error_message_displayed()
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        actual_error = login_page.get_error_message_text()
        assert actual_error == expected_error, f"Expected error message: '{expected_error}', but got: '{actual_error}'"
        assert login_page.is_on_login_page()

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
        login_page.open()
        assert login_page.is_on_login_page()
        
        login_page.login("", "")
        
        assert login_page.is_error_message_displayed()
        expected_error = "Epic sadface: Username is required"
        actual_error = login_page.get_error_message_text()
        assert actual_error == expected_error, f"Expected error message: '{expected_error}', but got: '{actual_error}'"
        assert login_page.is_on_login_page()

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
        login_page.open()
        assert login_page.is_on_login_page()
        
        login_page.login("performance_glitch_user", "secret_sauce")
        inventory_page.wait_for_page_load() 

        assert inventory_page.is_on_inventory_page()
        assert "inventory.html" in inventory_page.get_url()
        assert inventory_page.is_container_displayed()

        product_count = inventory_page.get_product_count()
        assert product_count == 6, f"Expected 6 products, found {product_count}"