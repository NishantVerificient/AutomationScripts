import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Change_Test:
    change_test_button = (By.XPATH, "//i[@class='fa fa-share-square-o']")
    active_test_dropdown = (By.XPATH, "//a[@class='chosen-single']")
    dropdown = (By.XPATH, "//li[@class='active-result']")
    save_button = (By.XPATH, "//button[@id='update_test']")
    test_title = (By.XPATH, "//h1[@class='title-tag no-margin']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def click_change_test_button(self):
        self.driver.find_element(*Change_Test.change_test_button).click()
        return self.driver.find_element(*Change_Test.test_title).text


    def change_active_test(self, TestName):
        self.driver.find_element(*Change_Test.active_test_dropdown).click()
        items = self.driver.find_elements(*Change_Test.dropdown)
        for item in items:
            if item.text == TestName:
                item.click()
                break

    def click_save_test(self):
        self.driver.find_element(*Change_Test.save_button).click()
        return time.sleep(2)
