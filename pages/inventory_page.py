from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def assert_on_inventory(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(self.title).to_have_text("Products")

    def add_item_by_slug(self, item_slug: str):
        # SauceDemo uses predictable data-test slugs like 'sauce-labs-backpack'
        self.page.locator(f"[data-test='add-to-cart-{item_slug}']").click()

    def remove_item_by_slug(self, item_slug: str):
        self.page.locator(f"[data-test='remove-{item_slug}']").click()

    def assert_cart_count(self, expected_count: str):
        expect(self.cart_badge).to_have_text(expected_count)

    def open_cart(self):
        self.cart_link.click()
