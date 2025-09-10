*** Settings ***
Resource    ../resources/common_vars.robot
Resource    ../resources/keywords.robot
Library     SeleniumLibrary

*** Test Cases ***
Login With Valid Credentials
    Open Sauce Demo
    Login With Credentials    ${VALID_USER}    ${VALID_PASS}
    Verify User On Products Page
    Close Browser

Login With Invalid Credentials
    Open Sauce Demo
    Login With Credentials    ${INVALID_USER}    ${INVALID_PASS}
    Verify Error Message
    Close Browser
