*** Settings ***
Resource    ../resources/keywords.robot

*** Test Cases ***
Verify Login Functionality
    Open Browser To Login Page
    Login
    Verify Login Successful
    Logout
