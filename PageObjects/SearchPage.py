from operator import truediv

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, search_driver):
        self.driver = search_driver

        #Locators for Search
        self.SearchField = (By.XPATH, "//input[@placeholder='Search for games']")
        self.GameTitleForSnowbirdSolitaire= (By.XPATH, "//a[text()='Snowbird Solitaire']")
        self.PlayNowButton =(By.XPATH, "//button[contains(normalize-space(), 'Play Now')]")


    def enter_any_game_in_searchbar(self, game):
        search_element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.SearchField)
        )
        search_element.send_keys(game)
        search_element.send_keys(Keys.ENTER)
        print(f"'{game}' is entered in the search bar")

    def is_snowbird_solitaire_present(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.GameTitleForSnowbirdSolitaire)
            )
            print("Snowbird Solitaire is present in search results.")
            return True
        except TimeoutException:
            return False

    def click_on_snow_solitaire_game(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.GameTitleForSnowbirdSolitaire)
        ).click()
        print("Click on snow solitaire game")

    def is_playnow_buton_present(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.visibility_of_element_located((self.PlayNowButton))
            )
            print("play now button is present")
            return True
        except TimeoutException:
            return False



