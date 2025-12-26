"Inventory Page class for Sauce Demo"

from allure import step
from playwright.sync_api import Page

from src.pages.base_page import BasePage


class InventoryPage(BasePage):

    URL_PATTERN = "**/inventory.html"
    INVENTORY_CONTAINER = ".inventory_container"
    PRODUCT_ITEMS = ".inventory_item"
    PRODUCT_NAMES = ".inventory_item_name"
    SHOPPING_CART_LINK = ".shopping_cart_link"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def __init__(self, page: Page):
        """Initialize the InventoryPage.
        Args:
            page (Page): The Playwright Page object.
        """
        super().__init__(page)

    @step("Wait for the inventory page to load completely.")
    def wait_for_page_load(self) -> None:
        """Wait for the inventory page to load completely."""
        self.page.wait_for_url(self.URL_PATTERN)

    @step("Check if the current page is the inventory page")
    def is_on_inventory_page(self) -> bool:
        """Check if the current page is the inventory page.
        Returns:
            bool: True if on inventory page, False otherwise.
        """
        return "inventory.html" in self.get_url()
    
    @step("Check if the inventory container is displayed")
    def is_container_displayed(self) -> bool:
        """Check if the inventory container is displayed.
        Returns:
            bool: True if inventory container is visible, False otherwise.
        """
        return self.page.locator(self.INVENTORY_CONTAINER).is_visible()
    
    @step("Get the count of products displayed on the inventory page")
    def get_product_count(self) -> int:
        """Get the count of products displayed on the inventory page.
        Returns:
            int: Number of products.
        """
        return self.page.locator(self.PRODUCT_ITEMS).count()
    
    @step("Get the names of all products displayed on the inventory page")
    def get_product_names(self) -> list[str]:
        """Get the names of all products displayed on the inventory page.
        Returns:
            list[str]: List of product names.
        """
        return self.page.locator(self.PRODUCT_NAMES).all_text_contents()
    
    @step("Check if a specific product is displayed on the inventory page")
    def is_product_displayed(self, product_name: str) -> bool:
        """Check if a specific product is displayed on the inventory page.
        Args:
            product_name (str): The name of the product to check.
        Returns:
            bool: True if the product is displayed, False otherwise.
        """
        return self.page.locator(self.PRODUCT_NAMES, has_text=product_name).is_visible()