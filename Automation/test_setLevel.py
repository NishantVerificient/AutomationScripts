import pytest

from PageObjects.dashboard import Dashboard
from PageObjects.set_level import Set_Level
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Test_SetConfigurations(BaseClass):
    def test_configurations(self,setup):
        Inst_Dashboard = Dashboard(self.driver)
        SetLevel = Set_Level(self.driver)

        Inst_Dashboard.click_edit_menu()
        Inst_Dashboard.click_edit_test_details_menu()
        Inst_Dashboard.click_configurations()
        SetLevel.click_proctoring_tab()
        #SetLevel.scroll_to_bottom()
        #SetLevel.set_test_to_l4()
        SetLevel.set_test_to_l5()

