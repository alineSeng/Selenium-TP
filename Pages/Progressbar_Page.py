from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait

class Progressbar_Page:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.star_button = (By.XPATH, "//button[@id='startStopButton']")
        self.bar_result = (By.CSS_SELECTOR, ".progress-bar")
        

    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs

    def start_progress_bar(self):
        element = self.wait.until(EC.visibility_of_element_located(self.star_button))
        element.click()
        
        # Attendre que la barre de progression atteigne 100%
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.find_element(*self.bar_result).get_attribute("aria-valuenow") == "100"  # Vérifie que la barre atteint 100%
        )

        # Vérifier la valeur finale de la barre de progression
        bar_value = self.driver.find_element(*self.bar_result).get_attribute("aria-valuenow")
        assert bar_value == "100", f"Expected progress bar value to be 100, but got {bar_value}"

    
    