import datetime
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
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("nishantnargide+inst07@verificient.com")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Password@12345")
driver.find_element(By.XPATH,"//button[@data-callback='onSubmit']").click()

#Instructor Dashboard
driver.implicitly_wait(10)
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='col-sm-12']")))

#Change Config
driver.find_element(By.XPATH,"//i[@class='fa fa-share-square-o']").click()
#DataInput = driver.find_element(By.XPATH,"//a[@class='chosen-single']")
#DataInput.click()

#driver.find_element(By.XPATH,"//input[@autocomplete='off']").send_keys("Test Auto")
#drop = Select(driver.find_element(By.XPATH,"//div[@class='chosen-container chosen-container-single']"))
#drop.select_by_visible_text("Test Auto")
#action = ActionChains(driver)
#driver.find_element(By.XPATH,"//div[@class='chosen-search']").send_keys("Test Automation Dummy 01")
#driver.find_element(By.XPATH,"//button[@id='update_test']").click()

driver.find_element(By.XPATH,"//a[@id='id_edit_menu']").click()
driver.find_element(By.XPATH,"//a[@id='id_edit_test_details_menu']").click()
driver.find_element(By.LINK_TEXT,"Configurations").click()

#Set Configurations
LevelText = "Level 1 | ProctorLock"
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h1[@class='panel-title ng-binding']")))
driver.find_element(By.XPATH,"//li[@ng-if='show_proctoring_level_change_tab']").click()
#driver.find_element(By.XPATH,"//div/div/div/input[@aria-label='PROCTOR TA For in class exams | Proctor TA LITE']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='ng-scope']")))
driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='according_identity_conf']/div[6]/div/div[2]/div[1]/div/div[2]/div").click()
time.sleep(2)

#Verification Settings
driver.find_element(By.XPATH,"//li[@index='1']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h1[@class='panel-title ng-binding']")))
driver.find_element(By.XPATH,"//*[@id='accordion_identity_conf']/div/div/div[3]").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='modal-body ng-scope']")))
driver.find_element(By.XPATH,"//button[@ng-click='continueToConfigChange()']").click()
face_scan = driver.find_element(By.XPATH,"//*[@id='accordion_identity_conf']/div[1]/div/div[3]")
if face_scan.is_selected():
    print("Face scan mandatory")
else:
    print("*o*")
time.sleep(5)
#wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='according_identity_conf']/div[6]/div/div[2]/div[1]/div/div[2]/input[@class='ng-pristine ng-untouched ng-valid ng-not-empty']")))

#//input[@class='ng-pristine ng-untouched ng-valid ng-not-empty']
#wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='according_identity_conf']/div[6]/div/div[2]/div[1]/div/div/class='ng-pristine ng-untouched ng-valid ng-not-empty'")))



#/html[1]/body[1]/div[2]/div[8]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[3]
#//div[6]//div[1]//div[2]//div[1]//div[1]//div[2]//div[1]//div[1]//span[3]
#for config in configurations:
#    if config.text == LevelText:
#        switch = config.find_element(By.XPATH,"//span[@class='ng-false-value']")
#        switch.click()
#switch = driver.find_element(By.XPATH,"//span[@class='bootstrap-switch-container']")
#isON = switch.get_attribute("class")

time.sleep(10)
