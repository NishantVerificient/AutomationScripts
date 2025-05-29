import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.add_Questions import Add_Questions
from PageObjects.add_student import Add_student
from PageObjects.change_test import Change_Test
from PageObjects.dashboard import Dashboard
from Utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestAddStudent(BaseClass):
    def test_add_student(self,setup):
        AddStudent = Add_student(self.driver)
        Inst_Dashboard = Dashboard(self.driver)
        self.wait = WebDriverWait(self.driver, 10)


        f_name = "Bruce"
        l_name = "Wayne"
        email = "brucewayne@xyz12345678901.com"

        Inst_Dashboard.click_edit_menu()
        Inst_Dashboard.click_edit_students()
        Inst_Dashboard.click_add_students()

        AddStudent.click_submit()
        assert "fill out this field" not in AddStudent.get_error_message()

        AddStudent.fill_registration(f_name,l_name,email)
        AddStudent.click_submit()
        AddStudent.get_title()
        AddStudent.refresh()
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h1[@style='font-size:36px; font-weight: normal;']")))