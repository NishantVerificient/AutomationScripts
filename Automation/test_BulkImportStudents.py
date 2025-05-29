import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.add_Instructor import Add_instructor
from PageObjects.add_Questions import Add_Questions
from PageObjects.add_student import Add_student
from PageObjects.change_test import Change_Test
from PageObjects.dashboard import Dashboard
from Utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestAddStudent(BaseClass):
    def test_add_student(self,setup):
        BulkStudents = Add_student(self.driver)
        Inst_Dashboard = Dashboard(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

        file = "//Users//nishant//Downloads//add_students.csv"

        Inst_Dashboard.click_edit_menu()
        Inst_Dashboard.click_edit_students()
        BulkStudents.click_bulk_import()
        BulkStudents.fill_file_input(file)
        BulkStudents.click_upload_button()
        #assert "uploaded" in BulkStudents.verify()
        #print(BulkStudents.verify())
