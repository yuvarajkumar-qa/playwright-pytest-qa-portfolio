import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_user_can_complete_checkout(page: Page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")
    inventory.assert_on_inventory()

    inventory.add_item_by_slug("sauce-labs-backpack")
    inventory.assert_cart_count("1")
    inventory.open_cart()

    checkout.start_checkout()
    checkout.fill_customer_info("Yuvaraj", "Kumar", "600001")
    checkout.finish_order()
    checkout.assert_order_complete()


@pytest.mark.regression
def test_checkout_requires_postal_code(page: Page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")
    inventory.add_item_by_slug("sauce-labs-bike-light")
    inventory.open_cart()

    checkout.start_checkout()
    # Leaving postal code blank should block step two and show validation error
    checkout.fill_customer_info("Yuvaraj", "Kumar", "")
    checkout.assert_error_contains("Postal Code is required")
