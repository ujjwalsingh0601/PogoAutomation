from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginLogoutPage:
    def __init__(self, loginlogout_driver):
        self.driver = loginlogout_driver
        # Locators for Login
        self.SignInButton = (By.XPATH, "//button[.//div[text()='Sign In']]")
        self.UsernameTextbox = (By.ID, 'email')
        self.NextButton = (By.XPATH, "//a[text()='NEXT']")
        self.PasswordTextbox = (By.ID, 'password')
        self.LoginButton = (By.XPATH, "//a[@id='logInBtn']")
        self.AvatarIcon = (By.XPATH, "//img[@alt='Avatar Image']")
        self.UsernameText = (By.XPATH, "//div[contains(text(),'Pogotest38')]")

        #Locator for Loginout
        self.SignOutButton = (By.XPATH, "//button[.//div[text()='Sign Out']]")   #  //div[text()='Sign Out']
        self.SignInButtonHeader = (By.XPATH, "//div[@class='header__1RWOM']/header/div[2]/div[1]/div[3]/button")
        self.SignoutMessage = (By.XPATH, "//div[contains(@class, 'signout')]/section/div[1]")




    def navigate_to_pogo_page(self, url):
        self.driver.get(url)
        print (f"Open the browser and enter url : '{url}'")

    def click_sign_in_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SignInButton)
        ).click()
        print("Click on sign in button")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.UsernameTextbox)
        ).send_keys(username)
        print(f"Enter username: '{username}' ")

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NextButton)
        ).click()
        print("Click on next button ")


    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PasswordTextbox)
        ).send_keys(password)
        print(f"Enter password: '{password}' ")

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LoginButton)
        ).click()
        print("Click on login button")

    def click_avatar_icon_present_user_dashboard(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.AvatarIcon)
        ).click()
        print("Click on avatar icon from the user's dashboard")

    def get_logged_in_username(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.UsernameText)
            )
            print ("Capturing.... Logged in username")
            return element.text.strip()
        except Exception as e:
            print(f"Error finding username element: {e}")
            return None


    def click_on_signout_button(self):
        signout_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SignOutButton)  # Wait until clickable, not just visible
        )
        signout_element.click()
        print("Click on signout button")
        # # Optionally move the mouse to the element before clicking
        # ActionChains(self.driver).move_to_element(signout_element).perform()
        # # Scroll into view just in case
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", signout_element)
        # # Click
        # signout_element.click()

    def is_signin_button_present(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.SignInButtonHeader)
            )
            print("Search for sign in button present or not........")
            return True
        except TimeoutException:
            return False

    def is_signout_button_present(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.SignOutButton)
            )
            print("Search for sign out button present or not........")
            return True
        except TimeoutException:
            return False

    def get_signout_message(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.SignoutMessage)
            )
            print("Capturing.... Signout message")
            return element.text.strip()
        except Exception as e:
            print(f"Error finding signout message: {e}")
            return None

    def login_to_pogo(self, username, password):
        self.click_sign_in_button()
        self.enter_username(username)
        self.click_next_button()
        self.enter_password(password)
        self.click_login_button()
        #print("Login with valid credential")
