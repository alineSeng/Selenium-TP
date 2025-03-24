from Pages.Home_Page import Home_Page
from Pages.Base_Page import Base_Page
from Pages.Date_Picker_Page import Date_Picker_Page

date = "05/11/2035"


def test_demoqa_1(driver, wait):
    home_page = Home_Page(driver, wait)
    home_page.go_to_widgets_menu()
    
    base_page = Base_Page(driver, wait)
    base_page.click_on_date_picker_submenu()
    
    date_picker_page = Date_Picker_Page(driver, wait)
    # date_picker_page.input_select_date(date)
    # date_picker_page.check_input_date(date)
    date_picker_page.select_date_and_time()
    
  