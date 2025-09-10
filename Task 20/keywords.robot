*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Sauce Demo
    [Documentation]    Launch browser and open Sauce Demo site
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login With Credentials
    [Arguments]    ${username}    ${password}
    Input Text    id=user-name    ${username}
    Input Text    id=password     ${password}
    Click Button  id=login-button

Verify User On Products Page
    Page Should Contain Element    xpath=//span[text()="Products"]

Verify Error Message
    Page Should Contain Element    css=.error-message-container

Add Product To Cart
    [Arguments]    ${product_name}
    Click Button    xpath=//div[text()="${product_name}"]/ancestor::div[@class="inventory_item"]//button
    Click Element   id=shopping_cart_container
    Page Should Contain    ${product_name}

Add Multiple Products And Checkout
    [Arguments]    @{products}
    FOR    ${item}    IN    @{products}
        Click Button    xpath=//div[text()="${item}"]/ancestor::div[@class="inventory_item"]//button
    END
    Click Element   id=shopping_cart_container
    Click Button    id=checkout
    Page Should Contain    Checkout: Your Information
