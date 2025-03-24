from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait

class Alerts_Page:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.alert_button = (By.ID, "alertButton")
        self.timer_alert_button = (By.XPATH, "//button[@id='timerAlertButton']")
        self.confirm_button = (By.ID, "confirmButton")
        self.promt_button = (By.ID, "promtButton")
        

    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs

    def check_alerts_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.alert_button))
        element.click()
        #assert element.is_displayed(), "Alert button is not displayed"
       
    def check_timer_alert_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.timer_alert_button)) 
        element.click() 
        self.time.sleep(6)
        # Vérifier si l'alerte est présente
        try:
            alert = self.wait.until(EC.alert_is_present())  # Attendre que l'alerte soit présente
            print("Alert is present!")
            
            # Accepter l'alerte (cliquer sur Ok)
            alert.accept()
            print("Clicked on OK in the alert.")
            
        except Exception as e:
            print("Alert not found within the given time.")
            print(f"Error: {e}")
            
        
    
    