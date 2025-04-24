import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://preproduction.verificient.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("nishantnargide+inst07@verificient.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Password@12345")
    driver.find_element(By.XPATH, "//button[@data-callback='onSubmit']").click()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()