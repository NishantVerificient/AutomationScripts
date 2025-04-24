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

#Change Test
driver.find_element(By.XPATH,"//i[@class='fa fa-share-square-o']").click()
#driver.find_element(By.XPATH,"//div[@class='chosen-search']").send_keys("Test Auto")
ActiveTest = driver.find_element(By.XPATH,"//a[@class='chosen-single']")
SaveTest = driver.find_element(By.XPATH,"//button[@id='update_test']")
Name = "Test Automation Dummy"
TestTitle = driver.find_element(By.XPATH,"//h1[@class='title-tag no-margin']").text
ActiveTest.click()
items = driver.find_elements(By.XPATH,"//li[@class='active-result']")
for item in items:
    if item.text == Name:
        item.click()
SaveTest.click()

#alert = driver.find_element(By.XPATH,"//div[@class='alert alert-warning alert-dismissible fade in']").text
#assert "success" in alert, "NOT Changed!"
#print(alert)
#driver.find_element(By.XPATH,"//li[@data-option-array-index='3']").click()
#driver.find_element(By.XPATH,"//input[@autocomplete='off']").send_keys("Test Auto")
#drop = Select(driver.find_element(By.XPATH,"//ul[@class='chosen-results']"))
#drop.select_by_index(3)
#action = ActionChains(driver)
#time.sleep(1)
#driver.find_element(By.XPATH,"//input[@autocomplete='off']").send_keys("Test Automation Dummy 01")
#driver.find_element(By.XPATH,"//button[@id='update_test']").click()
time.sleep(1)



