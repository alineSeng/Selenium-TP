from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Base_Page:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.date_picker_submenu = (By.CSS_SELECTOR, ".show #item-2 > .text")
        self.progress_bar_submenu = (By.CSS_SELECTOR, ".show #item-4 > .text")
        self.alerts_submenu = (By.CSS_SELECTOR, ".show #item-1 > .text")
       
    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs

    def click_on_date_picker_submenu(self):
        self.wait.until(EC.element_to_be_clickable(self.date_picker_submenu)).click()
    
    def click_on_date_progressbar_submenu(self):
        self.wait.until(EC.element_to_be_clickable(self.progress_bar_submenu)).click()
        
    def click_on_alert_submenu(self):
        self.wait.until(EC.element_to_be_clickable(self.alerts_submenu)).click()