import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v133.dom import set_file_input_files
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Add_instructor:
    add = (By.XPATH,"//input[@value='Add']")
    error_message = (By.XPATH, "//div[@class='message-text']")
    first_name = (By.XPATH, "//input[@name='first_name']")
    last_name = (By.XPATH, "//input[@name='last_name']")
    instructor_email = (By.XPATH, "//input[@name='instructor_email']")
    remove = (By.XPATH, "//button[@class='btn btn-danger']")
    bulk_import = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[4]/ul[1]/li[2]/a[1]")
    choose_file = (By.XPATH,"//input[@type='file']")
    upload_button = (By.XPATH,"//input[@value='Upload Invitations']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def click_add(self):
        return self.driver.find_element(*Add_instructor.add).click()

    def get_error_message(self):
        return self.driver.find_element(*Add_instructor.error_message).text

    def fill_registration(self, f_name, l_name, email):
        self.driver.find_element(*Add_instructor.first_name).send_keys(f_name)
        self.driver.find_element(*Add_instructor.last_name).send_keys(l_name)
        return self.driver.find_element(*Add_instructor.instructor_email).send_keys(email)

    def click_remove(self):
        self.driver.find_elements(*Add_instructor.remove)[1].click()
        self.wait.until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

    def assertion(self):
        return self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='message-text']")))

    def click_bulk_import_inst(self):
        return self.driver.find_element(*Add_instructor.bulk_import).click()

    def fill_file_input(self, file):
        return self.driver.find_element(*Add_instructor.choose_file).send_keys(file)

    def click_upload_button(self):
        return self.driver.find_element(*Add_instructor.upload_button).click()