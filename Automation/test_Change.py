import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.add_Questions import Add_Questions
from PageObjects.change_test import Change_Test
from PageObjects.dashboard import Dashboard
from Utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestChange(BaseClass):
    def test_change(self,setup):
        self.wait = WebDriverWait(self.driver, 10)
        TestName = "Change Test Dummy"
        ChangeTest = Change_Test(self.driver)
        DashBoard = Dashboard(self.driver)
        ChangeTest.click_change_test_button()
        ChangeTest.change_active_test(TestName)
        DashBoard.click_logo()
        