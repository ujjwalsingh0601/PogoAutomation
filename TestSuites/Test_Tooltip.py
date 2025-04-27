from ..PageObjects.LoginLogoutPage import LoginLogoutPage
from ..Fixtures.driver_fixture import driver
from ..PageObjects.TooltipPage import TooltipPage
import time

def test_verify_tooltip_message(driver):
    loginlogout_page = LoginLogoutPage(driver)
    tooltip_page = TooltipPage(driver)

    loginlogout_page.navigate_to_pogo_page("https://www.pogo.com")
    loginlogout_page.login_to_pogo("neproks@gmail.com", "Pogotest@38")

    # # static function to verify tooltip message on single menu icon which is for pogimeter tool tip message
    # actual_pogimeter_tooltip_message = tooltip_page.hover_on_pogimeter_and_capture_tooltip()
    # expected_pogimeter_tooltip_message = "Track how many you need to earn to unlock the next reward. Click the meter to see the rewards."
    # assert actual_pogimeter_tooltip_message == expected_pogimeter_tooltip_message, (
    #     f"Expected tooltip message: '{expected_pogimeter_tooltip_message}', but got :'{actual_pogimeter_tooltip_message}'")
    # print("actual_pogimeter_tooltip_message matched with expected_pogimeter_tooltip_message ")


    #reusable function to verify tooltip messages of each menu icon
    #1. verify tool tip message of pogimeter menu icon
    actual_pogimeter_tooltip_message = tooltip_page.hover_on_menuicon_and_capture_tooltip(
        tooltip_page.PogiMeter_MenuIncon, tooltip_page.Pogimeter_Tooltip)
    expected_pogimeter_tooltip_message = "Track how many you need to earn to unlock the next reward. Click the meter to see the rewards."
    assert actual_pogimeter_tooltip_message == expected_pogimeter_tooltip_message, (
        f"Expected tooltip message: '{expected_pogimeter_tooltip_message}', but got :'{actual_pogimeter_tooltip_message}'")
    print("actual_pogimeter_tooltip_message matched with expected_pogimeter_tooltip_message ")

    #2. verify tool tip message of Gem Balance menu icon
    actual_gembalance_tooltip_message = tooltip_page.hover_on_menuicon_and_capture_tooltip(
        tooltip_page.GemBalance_MenuIcon, tooltip_page.GemBalance_Tooltip)
    expected_gembalance_tooltip_message = "Use gems to buy power-ups, boosters, and hidden object episodes."
    assert actual_gembalance_tooltip_message == expected_gembalance_tooltip_message, (
        f"Expected tooltip message: '{actual_gembalance_tooltip_message}', but got :'{expected_gembalance_tooltip_message}'")
    print("actual_gembalance_tooltip_message matched with expected_gembalance_tooltip_message ")

    #3. verify tool tip message of inbox icon
    actual_inbox_icon_tooltip_message = tooltip_page.hover_on_menuicon_and_capture_tooltip(
        tooltip_page.Inbox_Icon, tooltip_page.Inbox_Tooltip)
    expected_inbox_icon_tooltip_message = "Here you'll receive news from Pogo. Club members can also access player messaging and gifting."
    assert expected_inbox_icon_tooltip_message in actual_inbox_icon_tooltip_message, (
        f"Expected tooltip message: '{actual_inbox_icon_tooltip_message}', but got :'{expected_inbox_icon_tooltip_message}'")
    print("expected_inbox_icon_tooltip_message contains in actual_inbox_icon_tooltip_message")


