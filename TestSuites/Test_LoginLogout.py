import time
from ..PageObjects.LoginLogoutPage import LoginLogoutPage
from ..Fixtures.driver_fixture import driver

# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()

def test_verify_login_logout(driver):
    loginlogout_page = LoginLogoutPage(driver)

    loginlogout_page.navigate_to_pogo_page("https://www.pogo.com")
    loginlogout_page.click_sign_in_button()
    loginlogout_page.enter_username("neproks@gmail.com")
    loginlogout_page.click_next_button()
    loginlogout_page.enter_password("Pogotest@38")
    loginlogout_page.click_login_button()
    loginlogout_page.click_avatar_icon_present_user_dashboard()

#assertion for successful login
    actual_username = loginlogout_page.get_logged_in_username()
    expected_username = "Pogotest38"
    assert actual_username == expected_username, (
        f"Expected Username: '{expected_username}', but got '{actual_username}'"
    )
    print(f"Actual Username:'{actual_username}' matched successfully with Expected Username:'{expected_username}'. Test Passed!")

#assertion for successful Logout
    loginlogout_page.click_on_signout_button()

    actual_signout_result = loginlogout_page.get_signout_message()
    expected_signout_result = "You've been signed out! Press the CONTINUE button to return to the home page."
    assert actual_signout_result == expected_signout_result, (
        f"Expected Result : '{expected_signout_result}', but got '{actual_signout_result}'"
    )
    print("logout successful message is displayed")

    assert loginlogout_page.is_signin_button_present(), "Sign In button is not visible after sign out!"
    print("Sign in button is displayed after successful logout")
    time.sleep(8)
