# Selenium Test Automation Suite

This project demonstrates a maintainable Selenium test suite using the Page Object Model (POM), pytest, and HTML reporting.

## Features

- Selenium WebDriver automation against the The Internet login page
- Page object classes for reusability and readability
- Parameterized login scenarios
- Logout validation
- HTML test report generation via pytest-html
- CI workflow for GitHub Actions

## Project structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
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
└── confest.py
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```

This generates an HTML report in `reports/report.html`.

## CI

The GitHub Actions workflow installs dependencies, runs the suite, and uploads the HTML report as an artifact.
