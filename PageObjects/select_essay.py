from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Select_Essay:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    question_text = (By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
    save_question_button = (By.XPATH, "//input[@value='Save Question']")

    #Question Details
    add_weight = (By.XPATH, "//input[contains(@name, '-weight')]")
    learning_obj = (By.XPATH, "//input[contains(@name, '-learning_objectives')]")
    rationale = (By.XPATH, "//textarea[contains(@name, '-rationale')]")

    question_visibility = (By.XPATH, "//label[contains(@for, '-visiblity')]")
    question_option_institution = (By.XPATH,"//option[@value='institution']")
    question_option_self = (By.XPATH,"//option[@value='self']")
    question_option_global = (By.XPATH,"//option[@value='global']")

    difficulty_level = (By.XPATH,"//select[contains(@name, '-difficulty_level')]")
    difficulty_value_high = (By.XPATH,"//option[@value='high']")
    difficulty_value_easy = (By.XPATH,"//option[@value='easy']")
    difficulty_value_medium = (By.XPATH,"//option[@value='medium']")


    def fill_question_name_0(self, question1):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@role='toolbar']")))
        self.driver.switch_to.frame(0)
        self.driver.find_element(*Select_Essay.question_text).send_keys(question1)
        self.driver.switch_to.default_content()
        self.driver.find_element(*Select_Essay.add_weight).clear()
        self.driver.find_element(*Select_Essay.add_weight).send_keys(15)
        self.driver.find_element(*Select_Essay.learning_obj).send_keys("By the end of period_of_time everything will be automated")
        self.driver.find_element(*Select_Essay.rationale).send_keys("Connecting Learning goals")
        self.driver.find_element(*Select_Essay.difficulty_level).click()
        self.driver.find_element(*Select_Essay.difficulty_value_high).click()
        self.driver.find_element(*Select_Essay.question_visibility).click()
        self.driver.find_element(*Select_Essay.question_option_institution).click()
        return self.driver.find_element(*Select_Essay.save_question_button).click()
