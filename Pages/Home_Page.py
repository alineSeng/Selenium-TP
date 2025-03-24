from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Home_Page:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.elements_menu = (By.CSS_SELECTOR, ".card:nth-child(1) h5")
        self.forms_menu = (By.CSS_SELECTOR, ".card:nth-child(2) svg")
        self.alerts_frame_windows_menu = (By.XPATH, "//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div[@class='category-cards']/div[3]/div[1]")
        self.widgets_menu = (By.CSS_SELECTOR, ".card:nth-child(4) h5")
        self.interactions_menu = (By.CSS_SELECTOR, ".card:nth-child(5) h5")
        self.book_store_application_menu = (By.CSS_SELECTOR, ".card:nth-child(6) svg")


    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs

    def go_to_elements_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.elements_menu)).click()
    
    def go_to_forms_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.forms_menu)).click()

    def go_to_alerts_frame_windows_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.alerts_frame_windows_menu)).click()
    
    def go_to_widgets_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.widgets_menu)).click()
    
    def go_to_interactions_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.interactions_menu)).click()
    
    def go_to_book_store_application_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.book_store_application_menu)).click()
