import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://preproduction.verificient.com/")
driver.maximize_window()

#Login
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("nishantnargide+inst1@verificient.com")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Nishant@password1")
driver.find_element(By.XPATH,"//button[@data-callback='onSubmit']").click()

#Instructor Dashboard
driver.implicitly_wait(10)
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='col-sm-12']")))

driver.find_element(By.XPATH,"//a[@id='id_edit_menu']").click()
driver.find_element(By.XPATH,"//i[@class='fa fa-users']").click()
driver.find_element(By.XPATH,"//i[@class='fa fa-user-plus']").click()

#Add Student
Submit = driver.find_element(By.XPATH,"//input[@id='submit_reg_data']")
Submit.click()
message = driver.find_element(By.XPATH,"//ul[@class='list-unstyled']").text
assert "fill out this field" in message
driver.find_element(By.XPATH,"//input[@name='student_first_name']").send_keys("Nishant")
driver.find_element(By.XPATH,"//input[@name='student_last_name']").send_keys("N")
driver.find_element(By.XPATH,"//input[@name='student_id']").send_keys("1234")
driver.find_element(By.XPATH,"//input[@name='student_email']").send_keys("nishantnargide+student03@verificient.com")
Submit.click()

Added = driver.find_element(By.XPATH,"//h2[@class='title-tag']")
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h2[@class='title-tag']")))
print(Added.text)
driver.find_element(By.XPATH,"//a[@aria-label='logo']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h1[@style='font-size:36px; font-weight: normal;']")))
time.sleep(5)