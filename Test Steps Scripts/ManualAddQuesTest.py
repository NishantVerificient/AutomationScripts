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
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("nishantnargide+inst1@verificient.com")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Nishant@password1")
driver.find_element(By.XPATH,"//button[@data-callback='onSubmit']").click()

#Instructor Dashboard
driver.implicitly_wait(10)
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='col-sm-12']")))

#Create Test
driver.find_element(By.XPATH,"//a[@id='id_edit_menu']").click()
driver.find_element(By.XPATH,"//a[@id='id_edit_test_details_menu']").click()
driver.find_element(By.XPATH,"//a[@id='func-add-test']").click()

#Test details
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h2[@style='font-size: 18px;']")))

driver.find_element(By.XPATH,"//textarea[@class='form-control']").send_keys("Test Automation Dummy 01")
driver.find_element(By.XPATH,"//textarea[@name='description']").send_keys("Description for Test Automation Dummy")
driver.find_element(By.XPATH,"//input[@id='id_start_at_0']").send_keys('12-02-2025')
driver.find_element(By.XPATH,"//input[@id='id_start_at_1']").send_keys('1030AM')
driver.find_element(By.XPATH,"//input[@id='id_end_at_0']").send_keys('12-02-2030')
driver.find_element(By.XPATH,"//input[@id='id_end_at_1']").send_keys('1030PM')
driver.find_element(By.XPATH,"//input[@name='duration']").send_keys('120')

#Details for students
driver.find_element(By.XPATH,"//input[@name='use_all_available_questions']").click()
#driver.find_element(By.XPATH,"//input[@name='question_count']").clear()
driver.find_element(By.XPATH,"//input[@name='question_count']").send_keys('1')
driver.find_element(By.XPATH,"//input[@name='serve_random_questions']").click()
#driver.find_element(By.XPATH,"//input[@class='form-control input-sm']").send_keys('100')
driver.find_element(By.XPATH,"//input[@name='attempts_allowed']").send_keys('9999')

dropdown = driver.find_element(By.XPATH,"//select[@class='form-control']")
select = Select(dropdown)
select.select_by_visible_text("Verified Certificate")

driver.find_element(By.XPATH,"//input[@name='show_learning_obj_to_student']").click()
driver.find_element(By.XPATH,"//input[@name='show_answer_sheet_to_student']").click()

#Test Features
onboarding = driver.find_element(By.XPATH,"//input[@name='is_onboarding']")
onboarding.click()
assert onboarding.is_selected(), "Not an OB Test"
onboarding.click()

external = driver.find_element(By.XPATH,"//input[@name='is_hosted_externally']")
assert not external.is_selected(), "Not Externally Hosted"

skipProctor = driver.find_element(By.XPATH,"//input[@name='is_proctoring_skip_allowed']")
skipProctor.click()
driver.find_element(By.XPATH,"//input[@id='id_test_access_code']").send_keys('1234')
skipProctor.click()
assert not skipProctor.is_selected(), "Proctored Exam"

driver.find_element(By.XPATH,"//input[@id='id_is_identity_question_required']").click()

#submit
driver.find_element(By.XPATH,"//input[@class='btn btn-custom btn-lg']").click()
#actions = ActionChains(driver)
#actions.move_to_element(edit).perform()

#Add Questions
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='col-sm-12']")))

driver.find_element(By.XPATH,"//button[@data-target='#qtypemodal']").click()
#dropdown2 = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select Question Type']"))
#dropdown2.select_by_visible_text("Essay")
driver.find_element(By.XPATH,"//select[@aria-label='Select Question Type']").click()
driver.find_element(By.XPATH,"//option[@value='long-text']").click()
driver.find_element(By.XPATH,"//button[@id='func-confirm-question-type']").click()

#Enter Question
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//iframe[@class='cke_wysiwyg_frame cke_reset']")))
driver.switch_to.frame(0)
QuestionText = driver.find_element(By.XPATH,"//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
#QuestionText.click()
QuestionText.send_keys("Question One")
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//input[@value='Save Question']").click()

#Question Two
driver.find_element(By.XPATH,"//button[@data-target='#qtypemodal']").click()
driver.find_element(By.XPATH,"//select[@aria-label='Select Question Type']").click()
driver.find_element(By.XPATH,"//option[@value='long-text']").click()
driver.find_element(By.XPATH,"//button[@id='func-confirm-question-type']").click()
#Add
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//iframe[@class='cke_wysiwyg_frame cke_reset']")))
driver.switch_to.frame(0)
Question2Text = driver.find_element(By.XPATH,"//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
Question2Text.send_keys("Question Two")
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//input[@value='Save Question']").click()

#Question Three
driver.find_element(By.XPATH,"//button[@data-target='#qtypemodal']").click()
driver.find_element(By.XPATH,"//select[@aria-label='Select Question Type']").click()
driver.find_element(By.XPATH,"//option[@value='long-text']").click()
driver.find_element(By.XPATH,"//button[@id='func-confirm-question-type']").click()
#Add
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//iframe[@class='cke_wysiwyg_frame cke_reset']")))
driver.switch_to.frame(0)
Question3Text = driver.find_element(By.XPATH,"//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
Question3Text.send_keys("Question Two")
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//input[@value='Save Question']").click()

#Save Changes
driver.find_element(By.XPATH,"//a[@id='func-save-test']").click()

#Success Message assertion
#SuccessText = driver.find_element(By.XPATH,"//div[@class='alert alert-warning alert-dismissible fade in']").text
#assert "success" in SuccessText, "Failed!"
#print(SuccessText)
time.sleep(5)
