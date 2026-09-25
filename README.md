# AI_TestForge_Automation

A practice QA automation project covering **UI automation with Playwright** and
**API testing with Python `requests`**, organised with Pytest and the Page Object Model.

It was built as a hands-on learning project. It tests public practice sites, not a
production application:

- UI: [automationexercise.com](https://automationexercise.com)
- API: the [AutomationExercise practice API](https://automationexercise.com/api_list) and
  [JSONPlaceholder](https://jsonplaceholder.typicode.com)

## Technologies

- Python 3.14
- Playwright for Python 1.60 (browser automation)
- Pytest 9.1 (test runner, fixtures, markers, parametrize)
- requests 2.34 (API testing)
- pytest-html (HTML reports)
- GitHub Actions (workflow file included, see [CI](#ci))

## Project structure

```
api/            API client classes (BaseAPI, AuthAPI, ProductsAPI, UsersAPI, PostsAPI)
config/         Base URL, browser, headless and timeout settings
fixtures/       Pytest fixtures for test users and logged-in pages
pages/          Page Object Model classes (BasePage, HomePage, LoginPage, ...)
testdata/       JSON test data
tests/          UI tests: smoke/, e2e/, negative/
tests_api/      API tests
utilities/      JSON reader, random data, API assertions, loggers
conftest.py     Browser/page fixture, ad blocking, screenshot on failure
pytest.ini      Test paths and markers
```

## UI automation (Playwright)

- **Page Object Model:** locators and actions live in page classes under `pages/`;
  tests only call page methods.
- **Assertions:** Playwright `expect()` web-first assertions, which wait and retry until
  the condition is true (e.g. `to_have_text`, `to_be_visible`, `to_have_url`).
- **Locators:** the site's `data-qa` attributes and IDs.
- **Browser fixture:** `conftest.py` starts Chromium, Firefox or WebKit (set by the
  `BROWSER` variable), headed or headless (`HEADLESS`), and closes it after each test.
  Third-party ad requests are blocked so pop-up ads cannot cover the page.
- **Screenshot on failure:** a Pytest hook saves a screenshot to `screenshots/`.

UI tests (11):

| Area | Tests |
|---|---|
| Smoke | register a new user, valid login, logout, delete account |
| End-to-end | register, logout, log in again, delete account |
| Negative | login with wrong password / unregistered email (error shown); login form with empty email / invalid email format / empty password (browser validation blocks submit); signup with an already registered email (error shown) |

## API testing (Python `requests`)

API tests (20):

| Area | Tests |
|---|---|
| Products (AutomationExercise) | get all products, get all brands, search returns matching products, search with no match returns empty list, search without the required parameter (400), unsupported HTTP methods (405, three endpoints) |
| Login (AutomationExercise) | valid credentials (200), wrong password and unregistered email (404), missing email or password (400) |
| Account (AutomationExercise) | create, read back, delete and confirm the account is gone; create with an existing email (400) |
| Users CRUD (JSONPlaceholder) | GET list, GET single user, POST, PUT, DELETE with status code and response body checks |

Note: the AutomationExercise API always returns HTTP 200 and puts the real result code
(200, 201, 400, 404, 405) in a `responseCode` field in the JSON body, with a `text/html`
content type. `utilities/api_assertions.py` checks both.

## Test data and fixtures

- `testdata/register.json`: demo user details (no real personal data).
- `testdata/negative_login.json`: negative login cases, used with `@pytest.mark.parametrize`.
- `testdata/api_data.json`: payloads for the JSONPlaceholder tests.
- Every test that needs an account gets a **new user with a unique `@example.com` email**
  from the `test_user` fixture. `registered_user` creates it through the API before the
  test, and the account is deleted through the API afterwards. Tests do not depend on
  each other or on run order.
- Files ending in `.local.json` are git-ignored and never committed.

## How to run

```bash
python -m venv venv
venv\Scripts\activate            # Windows  (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
python -m playwright install chromium

pytest                    # all tests
pytest -m api             # API tests only
pytest -m ui              # UI tests only
pytest -m smoke           # smoke UI tests
pytest -m negative        # negative UI tests

# headless run with an HTML report (Windows PowerShell)
$env:HEADLESS="true"; pytest --html=reports/report.html --self-contained-html
```

## Results

Latest local runs on Windows 10, Python 3.14.6, Chromium, headless (25 Sep 2026),
repeated in a fresh virtual environment installed from `requirements.txt`:

- API tests: **20 passed**
- UI tests: **11 passed**

These are live public practice sites, so a test can fail if a site is down or changes.

## CI

`.github/workflows/tests.yml` runs the API and UI tests on GitHub Actions (Ubuntu,
headless Chromium) on every push to `main` and on pull requests, and uploads the HTML
reports as an artifact. It has not run on GitHub yet; its result will show in the
Actions tab after the first push.
