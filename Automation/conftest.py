import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://preproduction.verificient.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("nishantnargide+inst07@verificient.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Password@12345")
    driver.find_element(By.XPATH, "//button[@data-callback='onSubmit']").click()
    driver.implicitly_wait(10)
    #Instructor Dashboard
    wait = WebDriverWait(driver, 15)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='col-sm-12']")))
    time.sleep(3)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()