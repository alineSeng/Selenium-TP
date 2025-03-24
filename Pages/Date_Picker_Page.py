from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Date_Picker_Page:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.select_date_field = (By.ID, "datePickerMonthYearInput")
        self.date_and_time_field = (By.ID, "dateAndTimePickerInput")
        self.select_month = (By.CSS_SELECTOR, ".react-datepicker__month-read-view--down-arrow")
        #self.november = (By.CSS_SELECTOR, ".react-datepicker__month-option:nth-child(11)")
        self.november = (By.XPATH, "//div[normalize-space()='November']")
        self.select_year = (By.CSS_SELECTOR, ".react-datepicker__year-read-view")
        self.year_2035 = (By.CSS_SELECTOR, ".react-datepicker__year-option:nth-child(4)")
        self.select_day_05 = (By.CSS_SELECTOR, ".react-datepicker__day--005")
        self.select_time_23_45 = (By.CSS_SELECTOR, ".react-datepicker__time-list-item:nth-child(96)")

    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs

    def input_select_date(self, date):
        element = self.wait.until(EC.element_to_be_clickable(self.select_date_field))
        element.clear()
        print(f"Date : {date}")
        element.send_keys(date)
      
    
    def check_input_date(self, date):
        element = self.wait.until(EC.visibility_of_element_located(self.select_date_field))
        assert element.get_attribute("value") == date, f"Expected date : {date} but got {element.get_attribute('value')}"

    def select_date_and_time(self):
        self.wait.until(EC.element_to_be_clickable(self.date_and_time_field)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_month)).click()
        self.wait.until(EC.element_to_be_clickable(self.november)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_year)).click()
        self.wait.until(EC.element_to_be_clickable(self.year_2035)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_day_05)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_time_23_45)).click()
    
    