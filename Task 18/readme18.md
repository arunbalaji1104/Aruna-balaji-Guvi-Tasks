# Zen Portal Automation (BDD + Behave + Allure)

This project automates the login/logout functionality of the Zen Portal (`https://www.zenclass.in/`)  
using **Python, Behave (BDD), Selenium, Page Object Model (POM), and Allure Reports**.

---

## Project Structure
project/
│── features/
│ ├── login.feature # BDD scenarios
│ └── steps/
│ └── test_login_steps.py # Step definitions
│
│── pages/
│ ├── login_page.py # Page Object for login
│ └── dashboard_page.py # Page Object for dashboard
│
│── requirements.txt # Python dependencies
│── README.md # Instructions
│── .gitignore 
