from ..PageObjects.LoginLogoutPage import LoginLogoutPage
from ..Fixtures.driver_fixture import driver
from ..PageObjects.SearchPage import SearchPage
import time

def test_verify_search_game(driver):
    search_game = SearchPage(driver)
    loginlogout_page = LoginLogoutPage(driver)

    loginlogout_page.navigate_to_pogo_page("https://www.pogo.com")
    loginlogout_page.login_to_pogo("neproks@gmail.com","Pogotest@38")
    search_game.enter_any_game_in_searchbar("Snowbird Solitaire")

# assetion for Snowbird Solitaire is present or not
    assert search_game.is_snowbird_solitaire_present(),("Snowbird Solitaire is not present in search")
    print("Snowbird Solitaire is displayed after successful search")

#assetion for playnow button
    search_game.click_on_snow_solitaire_game()
    assert  search_game.is_playnow_buton_present(), ("Play now button is not present after user was navigated to the game page")
    print("Play now button is present")
    time.sleep(10)


