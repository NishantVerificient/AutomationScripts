import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Set_Level:
    proctoring_tab = (By.XPATH, "//li[@index='0']")
    L1 = (By.XPATH, "//*[@id='according_identity_conf']/div[5]/div/div[2]/div[1]/div/div[2]/div")
    L2 = (By.XPATH, "//*[@id='according_identity_conf']/div[4]/div/div[2]/div[1]/div/div[2]/div")
    L3 = (By.XPATH, "//*[@id='according_identity_conf']/div[3]/div/div[2]/div[1]/div/div[2]/div")
    L4 = (By.XPATH, "//*[@id='according_identity_conf']/div[2]/div/div[2]/div[1]/div/div[2]/div")
    L5 = (By.XPATH, "//*[@id='according_identity_conf']/div[1]/div/div[2]/div[1]/div/div[2]/div")
    active = (By.XPATH,"//*[@id='according_identity_conf']div[4]/div[1]/div[1]/div[1]/div[1]/a[1]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def click_proctoring_tab(self):
        self.driver.find_element(*Set_Level.proctoring_tab).click()
        return self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='according_identity_conf']")))

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1)

    def set_test_to_l5(self):
        # Check if the switch is enabled (i.e., if it's in the 'active' state)
        switch_element = self.driver.find_element(*Set_Level.L5)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", switch_element)
        time.sleep(1)
        if "active" in switch_element.get_attribute("class"):  # Check if it's enabled
            print("L5 Switch is already enabled.")
            time.sleep(2)
        else:
            print("Switch is not enabled, performing click on L5.")
            switch_element.click()  # Perform click to enable it
            time.sleep(2)
            #self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='according_identity_conf']div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")))


    def set_test_to_l4(self):
        # Check if the switch is enabled (i.e., if it's in the 'active' state)
        switch_element = self.driver.find_element(*Set_Level.L4)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", switch_element)
        time.sleep(1)
        if "active" in switch_element.get_attribute("class"):  # Check if it's enabled
            print("L4 Switch is already enabled.")
            time.sleep(2)
        else:
            print("Switch is not enabled, performing click on L4.")
            switch_element.click()  # Perform click to enable it
            time.sleep(2)
            #self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='according_identity_conf']div[2]/div[1]/div[1]/div[1]/div[1]/a[1]")))

    def set_test_to_l3(self):
        # Check if the switch is enabled (i.e., if it's in the 'active' state)
        switch_element = self.driver.find_element(*Set_Level.L3)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", switch_element)
        time.sleep(1)
        if "active" in switch_element.get_attribute("class"):  # Check if it's enabled
            print("L3 Switch is already enabled.")
            time.sleep(2)
        else:
            print("Switch is not enabled, performing click on L3.")
            switch_element.click()  # Perform click to enable it
            time.sleep(2)
            #return self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='according_identity_conf']div[3]/div[1]/div[1]/div[1]/div[1]/a[1]")))

    def set_test_to_l2(self):
        # Check if the switch is enabled (i.e., if it's in the 'active' state)
        switch_element = self.driver.find_element(*Set_Level.L2)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", switch_element)
        time.sleep(1)
        if "active" in switch_element.get_attribute("class"):  # Check if it's enabled
            print("L2 Switch is already enabled.")
            time.sleep(2)
        else:
            print("Switch is not enabled, performing click on L2.")
            switch_element.click()  # Perform click to enable it
            time.sleep(2)
            #self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='according_identity_conf']div[4]/div[1]/div[1]/div[1]/div[1]/a[1]")))

    def set_test_to_l1(self):
        # Check if the switch is enabled (i.e., if it's in the 'active' state)
        switch_element = self.driver.find_element(*Set_Level.L1)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", switch_element)
        time.sleep(1)
        if "active" in switch_element.get_attribute("class"):  # Check if it's enabled
            print("L1 Switch is already enabled.")
            time.sleep(2)
        else:
            print("Switch is not enabled, performing click on L1.")
            switch_element.click()  # Perform click to enable it
            time.sleep(2)
            #self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='according_identity_conf']div[5]/div[1]/div[1]/div[1]/div[1]/a[1]")))

