# Sample Defect Reports

Real-world style bug notes showing how I write clear, reproducible defects with exact steps, expected vs. actual behavior, and data checks.

---

### BUG-101: Cart badge stays showing item count after browser back/refresh on checkout step
* **Severity:** Medium | **Priority:** P2
* **Area:** Cart State / Checkout
* **Preconditions:** User is logged in with 1 item (`Sauce Labs Backpack`) in the cart and on the checkout info screen.
* **Steps to Reproduce:**
  1. Add an item to the cart and open the cart page.
  2. Click **Checkout**.
  3. Trigger a page reload or navigate back/forward across cart and checkout steps.
* **Expected Result:** Cart badge count and item list stay consistent with active session state without stale or duplicated counts.
* **Actual Result:** UI badge occasionally shows stale count until a full inventory reload occurs.
* **Notes / Follow-up:** Add automated check in `tests/test_checkout.py` and verify backend cart/order state in SQL once backend persistence is wired.

---

### BUG-102: Checkout allows progression if required address field has leading/trailing spaces
* **Severity:** Medium | **Priority:** P2
* **Area:** Checkout Form Validation
* **Preconditions:** User has at least one item in the cart and is on `Checkout: Your Information`.
* **Steps to Reproduce:**
  1. Enter valid First Name and Last Name.
  2. Enter `"   "` (spaces only) in **Postal Code**.
  3. Click **Continue**.
* **Expected Result:** Whitespace-only postal code is trimmed/rejected with `"Postal Code is required"`.
* **Actual Result:** Whitespace passes basic non-empty check if not trimmed before validation.
* **Notes / Follow-up:** Good boundary case for regression tests alongside empty-string checks.
