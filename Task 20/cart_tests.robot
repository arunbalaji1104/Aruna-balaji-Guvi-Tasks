*** Settings ***
Resource    ../resources/common_vars.robot
Resource    ../resources/keywords.robot
Library     SeleniumLibrary

*** Test Cases ***
Add Product To Cart
    Open Sauce Demo
    Login With Credentials    ${VALID_USER}    ${VALID_PASS}
    Add Product To Cart    Sauce Labs Backpack
    Close Browser

Add Multiple Products And Checkout
    Open Sauce Demo
    Login With Credentials    ${VALID_USER}    ${VALID_PASS}
    Add Multiple Products And Checkout    Sauce Labs Backpack    Sauce Labs Bike Light    Sauce Labs Bolt T-Shirt
    Close Browser
