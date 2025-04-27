
import time
from ..PageObjects.LoginLogoutPage import LoginLogoutPage
from ..Fixtures.driver_fixture import driver
from ..PageObjects.RegisterPages import RegisterPage

def test_verify_user_registration(driver):
    loginlogout_page = LoginLogoutPage(driver)
    register_page = RegisterPage(driver)

    loginlogout_page.navigate_to_pogo_page("https://www.pogo.com")
    register_page.click_register_button()
    register_page.select_country("India")
    register_page.select_month("January")
    register_page.select_day("1")
    register_page.select_year("2000")
    register_page.click_next()
    register_page.enter_signup_email("dewedwe@gmail.com")
    register_page.enter_ea_id("USTfsf5799")
    register_page.enter_signup_password("TesfdfdfdferetAccount@5799")
    register_page.click_next()
    register_page.close_arkose_popup()


