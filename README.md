# SauceDemo UI Test Suite (Playwright + Pytest)

UI tests covering sign-in, shopping cart updates, and checkout on SauceDemo, built with Python, Playwright, and Pytest and run automatically on GitHub Actions with an HTML report artifact.

## What's Tested
* **Sign-in (`tests/test_login.py`):** Normal login (`@pytest.mark.smoke`) and blocked login for locked-out accounts (`@pytest.mark.regression`).
* **Cart & Checkout (`tests/test_checkout.py`):** Adding an item, checking the cart badge count, finishing an order (`@pytest.mark.smoke`), and making sure checkout stops when the postal code is left blank (`@pytest.mark.regression`).
* **QA Strategy & Bug Notes (`docs/test_strategy.md`, `docs/bug_reports.md`):** Risk priorities, smoke vs. regression scope, edge cases, and defect write-ups.


## Folder Structure
```text
├── .github/workflows/playwright.yml
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   └── test_checkout.py
├── pytest.ini
└── requirements.txt
