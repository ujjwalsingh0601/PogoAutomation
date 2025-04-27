from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TooltipPage:
    def __init__(self, tooltip_driver):
        self.driver = tooltip_driver


        #Locators for tooltip
        self.PogiMeter_MenuIncon = (By.XPATH,"//img[@alt='Pogis Icon']")
        self.GemBalance_MenuIcon = (By.XPATH, "//img[@alt='Gem Count']")
        self.Inbox_Icon = (By.XPATH, "//img[@alt= 'Inbox Header Navigation Icon']")

        self.Pogimeter_Tooltip =(By.XPATH, "//*[@id='pageContent']/div[1]/header/div[2]/div/div[1]/div/div[2]/div/div[2]")
        self.GemBalance_Tooltip =(By.XPATH, "//div[@id='pageContent']/div[1]/header/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]")
        self.Inbox_Tooltip = (By.XPATH, "//div[@id='pageContent']/div[1]/header/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]")

    def hover_on_pogimeter_and_capture_tooltip(self):
        try:
            wait = WebDriverWait(self.driver, 5)

            # Step 1: Wait for the PogiMeter icon and hover
            pogi_icon = wait.until(EC.presence_of_element_located(self.PogiMeter))
            actions = ActionChains(self.driver)
            actions.move_to_element(pogi_icon).perform()

            # Step 2: Wait for the tooltip to become visible
            tooltip = wait.until(EC.visibility_of_element_located(self.Pogimetertooltip))

            # Step 3: Capture and return tooltip text
            print("fetching tooltip message")
            return tooltip.text.strip()

        except Exception as e:
            print(f"Error while capturing tooltip: {e}")
            return None

    def hover_on_menuicon_and_capture_tooltip(self, MenuIconLogo, Tooltip):
        try:
            wait = WebDriverWait(self.driver, 5)

            # Step 1: Wait for the Menu Icon and hover
            menu_icon = wait.until(EC.presence_of_element_located(MenuIconLogo))
            actions = ActionChains(self.driver)
            actions.move_to_element(menu_icon).perform()

            # Step 2: Wait for the Tooltip to become visible
            tooltip_element = wait.until(EC.visibility_of_element_located(Tooltip))

            # Step 3: Capture and return tooltip text
            print("Fetching tooltip message...")
            return tooltip_element.text.strip()

        except Exception as e:
            print(f"Error while capturing tooltip: {e}")
            return None