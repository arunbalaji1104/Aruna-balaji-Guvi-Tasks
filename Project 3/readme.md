SauceDemo Automation Framework
This project contains automated UI tests for the SauceDemo web application, implemented using Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern.

Project Structure
pages/: Page Object Model classes representing various web pages.

tests/: Test cases for login, cart, checkout, etc.

conftest.py: Pytest fixtures including WebDriver setup.

requirements.txt: Python dependencies.

pytest.ini: Pytest configuration.

reports/: Directory for generated test reports.
├── pages/                 # Page Object Model classes for each page
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── (others as needed)
│
├── tests/                 # Test classes and functions
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│
│
├── conftest.py            # Pytest fixtures and WebDriver setup
├── requirements.txt       # Dependencies file
├── pytest.ini             # Pytest configuration
├── reports/               # Test reports
└── README.md              # This file
