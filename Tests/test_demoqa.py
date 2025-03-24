from Pages.Home_Page import Home_Page
from Pages.Base_Page import Base_Page
from Pages.Date_Picker_Page import Date_Picker_Page
from Pages.Progressbar_Page import Progressbar_Page
from Pages.Alerts_Page import Alerts_Page

date = "05/11/2035"


def test_date_picker(driver, wait):
    home_page = Home_Page(driver, wait)
    home_page.go_to_widgets_menu()
    
    base_page = Base_Page(driver, wait)
    base_page.click_on_date_picker_submenu()
    
    date_picker_page = Date_Picker_Page(driver, wait)
    # date_picker_page.input_select_date(date)
    # date_picker_page.check_input_date(date)
    date_picker_page.select_date_and_time()
    
def test_progress_bar(driver, wait):
    home_page = Home_Page(driver, wait)
    home_page.go_to_widgets_menu()
    
    base_page = Base_Page(driver, wait)
    base_page.click_on_date_progressbar_submenu()
    
    progressbar_page = Progressbar_Page(driver, wait)
    progressbar_page.start_progress_bar()


def test_alerts(driver, wait):
    home_page = Home_Page(driver, wait)
    home_page.go_to_alerts_frame_windows_menu()
    
    base_page = Base_Page(driver, wait)
    base_page.click_on_alert_submenu()
    
    alerts_page = Alerts_Page(driver, wait)
    # alerts_page.check_alerts_button()
    alerts_page.check_timer_alert_button()
    
