# Automated Testing of GUVI Web Application

## Project Title
Automated Testing of the Web Application [https://www.guvi.in](https://www.guvi.in)

---

## Project Objective
The objective of this project is to automate the testing of the GUVI web application by simulating user actions and validating key UI functionalities. The automation covers:  

- Verifying page behavior  
- Accessibility of critical elements  
- Navigation flows  
- Login and logout functionalities  

---

## Scope
- Cross-browser validation (Chrome, Firefox, Edge)  
- Both positive and negative test scenarios  
- Comprehensive reporting using Pytest HTML reports  

GUVI_Project/
│
├─ pages/                  # Page Object Model classes
│   ├─ base_page.py        # BasePage class with common methods
│   ├─ home_page.py        # Homepage elements and actions (menu, Login button, Dobby)
│   ├─ login_page.py       # Login page elements and actions
│   └─ signup_page.py      # Sign-Up page elements and actions
│
├─ tests/                  # Test scripts
│   ├─ test_login.py       # TC3, TC6, TC7: Login button & login functionality
│   ├─ test_home.py        # TC1, TC2, TC8, TC9: Homepage validations
│   └─ test_signup.py      # TC4, TC5: Sign-Up button and navigation
│
├─ drivers/                # WebDriver executables
│   └─ chromedriver.exe
├─ reports/                # Optional: HTML test reports
│   └─ report.html
├─ config.py               # URLs, credentials, settings
├─ requirements.txt        # Python dependencies
└─ README.md               # Project documentation


## Test Cases Covered
1. Verify whether the URL `https://www.guvi.in` is valid  
2. Verify the webpage title is `"GUVI | Learn to code in your native language"`  
3. Verify visibility and clickability of the Login button  
4. Verify visibility and clickability of the Sign-Up button  
5. Verify navigation to the Sign-Up page  
6. Verify login functionality with valid credentials  
7. Verify login functionality with invalid credentials  
8. Verify menu items like “Courses”, “LIVE Classes”, and “Practice” are visible  
9. Verify the presence of Dobby Guvi Assistant (chatbot)  
10. Verify logout functionality  

---

## Project Setup

### Prerequisites
- Python 3.x installed  
- WebDriver for your browser (e.g., `chromedriver.exe`)  
- Required Python packages: Selenium and Pytest  

