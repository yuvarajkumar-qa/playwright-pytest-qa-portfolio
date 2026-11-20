from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_btn = page.locator("[data-test='checkout']")
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")
        self.finish_btn = page.locator("[data-test='finish']")
        self.error_msg = page.locator("[data-test='error']")
        self.complete_header = page.locator("[data-test='complete-header']")

    def start_checkout(self):
        self.checkout_btn.click()

    def fill_customer_info(self, first: str, last: str, zip_code: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        self.continue_btn.click()

    def finish_order(self):
        self.finish_btn.click()

    def assert_order_complete(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")

    def assert_error_contains(self, text: str):
        expect(self.error_msg).to_contain_text(text)
