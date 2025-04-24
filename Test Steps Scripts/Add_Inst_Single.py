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

action = ActionChains(driver)
driver.find_element(By.XPATH,"//a[@id='id_edit_menu']").click()
driver.find_elements(By.XPATH,"//i[@class='fa fa-users']")[1].click()
driver.find_elements(By.XPATH,"//i[@class='fa fa-user']")[1].click()

wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h2[@class='panel-title']")))

#Add Instructor
driver.find_element(By.XPATH,"//input[@name='first_name']").send_keys("Nishant")
driver.find_element(By.XPATH,"//input[@name='last_name']").send_keys("N")
driver.find_element(By.XPATH,"//input[@name='instructor_email']").send_keys("jv@jv.com")
driver.find_element(By.XPATH,"//input[@value='Add']").click()

message = driver.find_element(By.XPATH,"//div[@class='message-text']").text
assert "success" in message
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='message-text']")))
#Remove
driver.find_elements(By.XPATH,"//button[@class='btn btn-danger']")[1].click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(4)