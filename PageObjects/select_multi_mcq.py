from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Select_MultiMCQ:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    choice_one = (By.XPATH, "//textarea[substring(@id, string-length(@id) - string-length('-choice1') + 1) = '-choice1']")
    choice_two = (By.XPATH, "//textarea[substring(@id, string-length(@id) - string-length('-choice2') + 1) = '-choice2']")
    choice_three = (By.XPATH, "//textarea[substring(@id, string-length(@id) - string-length('-choice3') + 1) = '-choice3']")
    choice_four = (By.XPATH, "//textarea[substring(@id, string-length(@id) - string-length('-choice4') + 1) = '-choice4']")
    choice_answer1 = (By.XPATH,"//label[substring(@for, string-length(@for) - string-length('-choice3') + 1) = '-choice3']")
    choice_answer2 = (By.XPATH,"//label[substring(@for, string-length(@for) - string-length('-choice1') + 1) = '-choice1']")
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


    def fill_question_name_2(self, question3):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@role='toolbar']")))
        self.driver.switch_to.frame(0)
        return self.driver.find_element(*Select_MultiMCQ.question_text).send_keys(question3)

    def fill_choice_two(self,choice1,choice2,choice3,choice4):
        self.driver.switch_to.default_content()
        self.driver.find_element(*Select_MultiMCQ.choice_one).send_keys(choice1)
        self.driver.find_element(*Select_MultiMCQ.choice_two).send_keys(choice2)
        self.driver.find_element(*Select_MultiMCQ.choice_three).send_keys(choice3)
        self.driver.find_element(*Select_MultiMCQ.choice_four).send_keys(choice4)
        self.driver.find_element(*Select_MultiMCQ.choice_answer1).click()
        self.driver.find_element(*Select_MultiMCQ.choice_answer2).click()
        self.driver.find_element(*Select_MultiMCQ.add_weight).clear()
        self.driver.find_element(*Select_MultiMCQ.add_weight).send_keys(15)
        self.driver.find_element(*Select_MultiMCQ.learning_obj).send_keys("By the end of period_of_time everything will be automated")
        self.driver.find_element(*Select_MultiMCQ.rationale).send_keys("Connecting Learning goals")
        self.driver.find_element(*Select_MultiMCQ.difficulty_level).click()
        self.driver.find_element(*Select_MultiMCQ.difficulty_value_high).click()
        self.driver.find_element(*Select_MultiMCQ.question_visibility).click()
        self.driver.find_element(*Select_MultiMCQ.question_option_institution).click()
        return self.driver.find_element(*Select_MultiMCQ.save_question_button).click()