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
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("nishantnargide+inst1@verificient.com")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Nishant@password1")
driver.find_element(By.XPATH, "//button[@data-callback='onSubmit']").click()

#Instructor Dashboard
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='col-sm-12']")))

#File Path
file_path = "C:/Users/nishantnargide_verif/Downloads/DataOne.csv"
#Bulk Import
driver.find_element(By.XPATH, "//a[@id='id_edit_menu']").click()
driver.find_element(By.XPATH, "//i[@class='fa fa-users']").click()
driver.find_element(By.XPATH,"//a[@href='/614e76646a472c210d255003/tests/registrations/test/afc2970fcb1f4e4c9aa8abccb631cfea/upload/']").click()

file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys(file_path)
driver.find_element(By.XPATH, "//input[@value='Upload Invitations']").click()

alert = driver.find_element(By.XPATH,"div[@style='margin-top:15px;']").text
assert "success" in alert
print(alert)
time.sleep(5)
