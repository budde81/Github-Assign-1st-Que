# Formal Assignment Prompt: Selenium Test Automation Refactoring

## Objective
Refactor the provided procedural Selenium Python script into a robust, maintainable, and professional test automation suite using industry-standard enterprise testing practices. The solution must demonstrate sound software engineering principles and improve code quality, maintainability, and test readability.

## Required Deliverables
The final project must include the following components:

1. POM (Page Object Model)
   - Files:
     - `pages/base_page.py`
     - `pages/login_page.py`
     - `pages/secure_area_page.py`
   - Requirements:
     - Separate page classes for each page under test.
     - Encapsulation of page-specific behavior and locators.
     - No direct Selenium actions embedded inside test methods.

2. Locator in one place
   - Files:
     - `pages/login_page.py`
     - `pages/secure_area_page.py`
     - `pages/base_page.py`
   - Requirements:
     - All UI locators must be declared in one location within each page object class.
     - Test classes must not contain raw locators or direct page element definitions.

3. Reusable login method
   - Files:
     - `pages/login_page.py`
     - `tests/test_login.py`
   - Requirements:
     - A reusable login method must be implemented to accept credentials.
     - A dedicated valid-login helper may also be included where appropriate.

4. Code smell reduction
   - Files:
     - `pages/base_page.py`
     - `tests/conftest.py`
     - `tests/test_login.py`
     - `pages/login_page.py`
     - `pages/secure_area_page.py`
   - Requirements:
     - Remove procedural duplication and unnecessary code complexity.
     - Eliminate code smells such as repeated Selenium calls and hardcoded UI logic in tests.
     - Follow clean code practices that support scalability and future extension.

5. Readability
   - Files:
     - `tests/test_login.py`
     - `pages/login_page.py`
     - `pages/base_page.py`
     - `README.md`
     - `PROMPT_FORMAL.md`
   - Requirements:
     - Write clear, descriptive method and test names.
     - Organize the project into logical modules and directories.
     - Keep the tests concise and easy to understand.

6. Logging
   - Files:
     - `pages/base_page.py`
     - `pages/login_page.py`
     - `pages/secure_area_page.py`
     - `tests/conftest.py`
     - `tests/test_login.py`
   - Requirements:
     - Add logging for critical automation steps such as browser setup, navigation, login attempts, invalid login handling, and logout flow.
     - Use standardized log messages and a consistent logging format.

## Mandatory Functional Coverage
The final suite must include at least the following tests:

- Successful login scenario
- Invalid login scenario
- Parameterized login data validation
- Logout scenario

## Technical Standards
The implementation must follow these standards:

- Use pytest as the test framework.
- Use Selenium WebDriver for browser automation.
- Use WebDriverWait for explicit waits instead of fixed sleeps.
- Use fixtures for browser lifecycle management.
- Keep page objects separate from test logic.
- Ensure tests are maintainable and suitable for CI execution.

## Expected Project structure

```text
.
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── secure_area_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_login.py
├── .gitignore
├── pytest.ini
├── README.md
├── requirements.txt
├── reports/
├── PROMPT_FORMAL.md
└── CI configuration files
```

## Reporting Requirements
The project should generate a test report in HTML format for result visibility and easier review.

## Expected Outcome
The final code should represent a professional test automation project that is clean, reusable, scalable, and aligned with enterprise software engineering standards.

## Evaluation Criteria
Your solution will be assessed on the following:

- Correctness of Selenium automation
- Proper use of the Page Object Model
- Organization of locators and test logic
- Reusability of login workflows
- Clarity and maintainability of code
- Logging implementation
- Test readability and structure
- Execution reliability with pytest
