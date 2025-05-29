from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Select_TrueFalse:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    choice_true = (By.XPATH,"//label[substring(@for, string-length(@for) - string-length('-choice1') + 1) = '-choice1']")
    choice_false = (By.XPATH,"//label[substring(@for, string-length(@for) - string-length('-choice2') + 1) = '-choice2']")
    question_text = (By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
    save_question_button = (By.XPATH, "//input[@value='Save Question']")

    #Question Details
    add_weight = (By.XPATH, "//input[contains(@name, '-weight')]")
    learning_obj = (By.XPATH, "//input[contains(@name, '-learning_objectives')]")
    rationale = (By.XPATH, "//textarea[contains(@name, '-rationale')]")

    question_visibility = (By.XPATH, "//label[contains(@for, '-visiblity')]")
    question_option_institution = (By.XPATH, "//option[@value='institution']")
    question_option_self = (By.XPATH, "//option[@value='self']")
    question_option_global = (By.XPATH, "//option[@value='global']")

    difficulty_level = (By.XPATH, "//select[contains(@name, '-difficulty_level')]")
    difficulty_value_high = (By.XPATH, "//option[@value='high']")
    difficulty_value_easy = (By.XPATH, "//option[@value='easy']")
    difficulty_value_medium = (By.XPATH, "//option[@value='medium']")


    def fill_question_name_3(self, question4):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@role='toolbar']")))
        self.driver.switch_to.frame(0)
        return self.driver.find_element(*Select_TrueFalse.question_text).send_keys(question4)

    def fill_truefalse(self):
        self.driver.switch_to.default_content()
        self.driver.find_element(*Select_TrueFalse.choice_true).click()
        self.driver.find_element(*Select_TrueFalse.choice_false).click()
        self.driver.find_element(*Select_TrueFalse.add_weight).clear()
        self.driver.find_element(*Select_TrueFalse.add_weight).send_keys(15)
        self.driver.find_element(*Select_TrueFalse.learning_obj).send_keys("By the end of period_of_time everything will be automated")
        self.driver.find_element(*Select_TrueFalse.rationale).send_keys("Connecting Learning goals")
        self.driver.find_element(*Select_TrueFalse.difficulty_level).click()
        self.driver.find_element(*Select_TrueFalse.difficulty_value_high).click()
        self.driver.find_element(*Select_TrueFalse.question_visibility).click()
        self.driver.find_element(*Select_TrueFalse.question_option_institution).click()
        return self.driver.find_element(*Select_TrueFalse.save_question_button).click()