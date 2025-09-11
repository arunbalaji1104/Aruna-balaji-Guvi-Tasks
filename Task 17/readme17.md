# Zen Class Automation Project

## Overview
This project automates the login and logout functionality of the [Zen Class](https://www.zenclass.in/) portal using **Python**, **Playwright**, and **Pytest**.  
It follows the **Page Object Model (POM)** design pattern, uses **explicit waits**, and generates **HTML test reports**.

---

## Features

- **Automated Login**
- **Automated Logout**
- **Validation of Input Fields (Username, Password)**
- **Validation of Submit Button**
- **HTML Test Reports**
- **Page Object Model (POM) Implementation**
- **Python OOP and Exception Handling**

---

## Project Structure

│
├── pages/
│ └── login_page.py # POM class for login/logout
│
├── tests/
│ └── test_login.py # Pytest test cases
│
├── utils/
│ └── config.py # URL and credentials
│
├── pytest.ini # Pytest HTML report configuration
├── requirements.txt # Python dependencies
└── README.md # Project overview and instructions
