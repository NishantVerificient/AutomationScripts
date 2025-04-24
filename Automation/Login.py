import pytest
import selenium

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self,setup):
        pass