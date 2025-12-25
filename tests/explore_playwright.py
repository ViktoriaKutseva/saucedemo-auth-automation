"Overview of the playwright abilities"

from playwright.sync_api import sync_playwright
import time


def explore_saucedemo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        print("Navigating to saucedemo.com")
        page.goto("https://www.saucedemo.com/")  

        time.sleep(2)

        print("Filling in login credentials")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        print("Clicking login button")
        page.locator("#login-button").click()
        page.wait_for_url("**/inventory.html")
        print("Current URL after login:", page.url)
        assert "inventory.html" in page.url

        products = page.locator(".inventory_item")
        product_count = products.count()
        product_names = page.locator(".inventory_item_name").all_text_contents()
        print("Products found:")
        for name in product_names:
            print(f"  - {name}")
        print(f"Number of products displayed: {product_count}")

        time.sleep(2)

        browser.close()
        print("Browser closed")

# def test_invalid_login():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=500)
#         page = browser.new_page()
#         page.goto("https://www.saucedemo.com/")  

#         page.get_by_role("textbox", name="Username").fill("invalid_user")
#         page.get_by_role("textbox", name="Password").fill("wrong_password")
#         page.locator("#login-button").click()

#         error_message = page.locator("[data-test='error']").inner_text()
#         print("Error message displayed:", error_message)
#         print("Taking screenshot of the error message")
#         page.screenshot(path="docs/login_error.png")
#         browser.close()
if __name__ == "__main__":
    explore_saucedemo()