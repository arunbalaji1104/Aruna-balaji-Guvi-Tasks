*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://robotsparebinindustries.com/
${BROWSER}   chrome
${USERNAME}  maria
${PASSWORD}  thomas

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login
    Input Text    id:username    ${USERNAME}
    Input Text    id:password    ${PASSWORD}
    Click Button    id:login

Verify Login Successful
    Page Should Contain Element    id:logout

Logout
    Click Button    id:logout
    Close Browser
