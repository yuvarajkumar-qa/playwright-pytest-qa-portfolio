# Test Strategy & QA Notes

## Why These Flows Are Automated First
For an e-commerce app, the highest business risk sits around account access, cart accuracy, and checkout completion. If sign-in fails, cart counts drift, or checkout lets bad input slip through, revenue and user trust take an immediate hit.

## Smoke vs. Regression (`@pytest.mark`)
* **Smoke (`pytest -m smoke`):** Fast checks for core paths that must work before deeper testing or deployment—valid login and completing an end-to-end checkout.
* **Regression (`pytest -m regression`):** Targeted checks for guardrails and failure modes—locked-out user handling and missing required checkout fields like postal code.

## Edge Cases & Real-World Bugs to Watch
From manual testing experience, UI happy paths rarely catch everything. Useful areas to expand next:
* **Cart state drift:** Adding, removing, and refreshing or navigating back to make sure the item count stays accurate.
* **Form & price boundaries:** Blank or whitespace-only fields, special characters in names/ZIP codes, and total calculation checks.
* **Account & session states:** Locked-out users, slow/problem accounts, and behavior after logout or browser back/forward.
* **API & database alignment:** Confirming UI actions match backend responses and database records rather than relying only on screen state.
