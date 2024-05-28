*** Settings ***
Library    Test_seatbelt.py
Library    Seatbelt_GUI.py
Documentation    Test the selected component

*** Test Cases ***
Test Seatbelt Alerts
    [Documentation]    Check that light and sound alerts function correctly when the seatbelt is unfastened and fastened.

    Unfasten Seatbelt
    ${light_red}=    Is Light Indicator Red
    ${sound_on}=    Is Sound Alarm On
    Should Be True    ${light_red}    The warning light should flash red when the belt is unfastened.
    Should Be True    ${sound_on}     The audible alarm must be activated when the belt is unfastened.

    Fasten Seatbelt
    ${light_green}=    Is Light Indicator Green
    ${sound_on}=    Is Sound Alarm On
    ${light_off}=  Set Variable    ${light_green} == True
    ${sound_off}=  Set Variable    ${sound_on} == False
    Should Be True    ${light_off}    The warning light should be green when the belt is fastened.
    Should Be True    ${sound_off}    The audible alarm must be deactivated when the belt is fastened.