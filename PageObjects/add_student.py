import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Add_student:
    submit = (By.XPATH,"//input[@id='submit_reg_data']")
    error_message = (By.XPATH, "//ul[@class='list-unstyled']")
    first_name = (By.XPATH, "//input[@name='student_first_name']")
    last_name = (By.XPATH, "//input[@name='student_last_name']")
    student_id = (By.XPATH, "//input[@name='student_id']")
    student_email = (By.XPATH, "//input[@name='student_email']")
    title = (By.XPATH, "//h2[@class='title-tag']")
    logo = (By.XPATH, "//a[@aria-label='logo']")
    header_text = (By.XPATH, "//h1[@style='font-size:36px; font-weight: normal;']")
    bulk_import = (By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[3]/ul[1]/li[3]/a[1]")
    file_input = (By.XPATH, "//input[@type='file']")
    upload_button = (By.XPATH, "//input[@value='Upload Invitations']")
    alert_box = (By.XPATH, "div[@style='margin-top:15px;']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def click_submit(self):
        return self.driver.find_element(*Add_student.submit).click()

    def get_error_message(self):
        return self.driver.find_element(*Add_student.error_message).text

    def fill_registration(self, f_name, l_name, email):
        self.driver.find_element(*Add_student.first_name).send_keys(f_name)
        self.driver.find_element(*Add_student.last_name).send_keys(l_name)
        return self.driver.find_element(*Add_student.student_email).send_keys(email)

    def get_title(self):
        self.driver.find_element(*Add_student.title)
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//h2[@class='title-tag']")))
        print(*Add_student.title)

    def refresh(self):
        self.driver.find_element(*Add_student.logo).click()
        return self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h1[@style='font-size:36px; font-weight: normal;']")))

    def click_bulk_import(self):
        return self.driver.find_element(*Add_student.bulk_import).click()

    def fill_file_input(self, file):
        return self.driver.find_element(*Add_student.file_input).send_keys(file)

    def click_upload_button(self):
        self.driver.find_element(*Add_student.upload_button).click()

    def verify(self):
        return self.driver.find_element(*Add_student.alert_box).text