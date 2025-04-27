from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class RegisterPage:

    def __init__(self, SignUp_driver):
        self.driver = SignUp_driver

        #Locators for Signup pages
        self.RegisterButton = (By.XPATH, "//button[.//div[text()='Register free']]")
        self.country_dropdown = (By.ID, 'clientreg_country-selctrl')
        self.month_dropdown = (By.ID, 'clientreg_dobmonth-selctrl')
        self.day_dropdown = (By.ID, 'clientreg_dobday-selctrl')
        self.year_dropdown = (By.ID, 'clientreg_dobyear-selctrl')
        self.NextBtn = (By.XPATH,"//a[text()='Next']")
        self.SignupEmailAddress = (By.XPATH, "//input[@id='email']")
        self.EA_ID = (By.ID, 'originId')
        self.SignupPassword = (By.ID,'password')

    def click_register_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.RegisterButton)
        ).click()
        print("[INFO] Clicked on Register Free button.")

    def select_country(self, country):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.country_dropdown)
        )
        Select(element).select_by_visible_text(country)
        print(f"[INFO] Country selected: {country}")

    def select_month(self, month):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.month_dropdown)
        )
        Select(element).select_by_visible_text(month)
        print(f"[INFO] DOB Month selected: {month}")

    def select_day(self, day):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.day_dropdown)
        )
        Select(element).select_by_visible_text(day)
        print(f"[INFO] DOB Day selected: {day}")

    def select_year(self, year):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.year_dropdown)
        )
        Select(element).select_by_visible_text(year)
        print(f"[INFO] DOB Year selected: {year}")

    def click_next(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NextBtn)
        ).click()
        print("[INFO] Clicked Next button.")

    def enter_signup_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SignupEmailAddress)
        ).send_keys(email)
        print(f"[INFO] Email entered: {email}")

    def enter_ea_id(self, ea_id):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EA_ID)
        ).send_keys(ea_id)
        print(f"[INFO] EA ID entered: {ea_id}")

    def enter_signup_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SignupPassword)
        ).send_keys(password)
        print(f"[INFO] Password entered: [hidden]")



    #function to close iframe element
    def close_arkose_popup(self):
        try:
            # Wait for iframe to appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src,'arkoselabs')]"))
            )
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@src,'arkoselabs')]")
            self.driver.switch_to.frame(iframe)
            print("[INFO] Switched to iframe.")

            # Wait and click the close (X) button inside iframe
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@aria-label='Close Arkose Labs Enforcement Challenge.']"))
            ).click()
            print("[INFO] Closed the Arkose puzzle popup.")

            # Switch back to main page
            self.driver.switch_to.default_content()
            print("[INFO] Switched back to main page.")

        except Exception as e:
            print(f"[ERROR] Cross button not found or could not click it: {e}")
