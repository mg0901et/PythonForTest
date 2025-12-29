import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class BaseElement:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.yatra.com/")
        self.driver.find_element(By.XPATH,"(//img[@alt='cross'])[1]").click()
        self.driver.maximize_window()
        time.sleep(2)

    def find_the_text(self):
        """ Help to Find a text from the ELEMENTS -->> .text """

        text = self.driver.find_element(By.XPATH,"//h2[normalize-space()='Flights to Popular Domestic Destinations from']").text
        print(text)

    def find_attribute_value(self):
        """ Help to Find the values of the Attribute -->> .get_attribute("Attribue_we_want_to_search") """

        attr_title = self.driver.find_element(By.XPATH,"//p[@title='Mumbai']").get_attribute("title")
        print(attr_title)

    def check_element_state(self):
        # self.driver.quit()
        self.driver.get("https://training.openspan.com/login")
        element_state = self.driver.find_element(By.ID,"login_button").is_enabled()
        print("Current Element State is :", element_state)
        self.driver.find_element(By.ID,"user_name").send_keys("Mayank")
        self.driver.find_element(By.ID,"user_pass").send_keys("Mayank")
        element_state = self.driver.find_element(By.ID,"login_button").is_enabled()
        print("Current Element State is :", element_state)
    
    def check_element_isDisplayed(self):
        #CASE-1 When ELEMNT IS THERE IN THE SITE BUT IT'S HIDDEN
        self.driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        element_status = self.driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print("Status of Element : ",element_status)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        element_status = self.driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print("Status of Element : ",element_status)

        #CASE-2 WHEN ELEMENT IS REMOVED BASED ON SELECTION
        """
        This will throw an ERROR which 
        we need to manage bcz this will only work with those Element which is visible

        """
    def checkbox_selected(self):
        self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        time.sleep(2)
        checkStatus = self.driver.find_element(By.XPATH,"//input[@type='checkbox']").is_selected()
        print('Status of checkBox is : ',checkStatus)

        self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        time.sleep(2)
        checkStatus = self.driver.find_element(By.XPATH,"//input[@type='checkbox']").is_selected()
        print('Status of checkBox is : ',checkStatus)

    def RadioButton_selected(self):
        self.driver.find_element(By.XPATH,"//input[@value='2']").click()
        time.sleep(2)
        checkStatus = self.driver.find_element(By.XPATH,"//input[@value='2']").is_selected()
        print('Status of RadioButton is : ',checkStatus)

        time.sleep(2)
        checkStatus = self.driver.find_element(By.XPATH,"//input[@value='3']").is_selected()
        print('Status of RadioButton is : ',checkStatus)
    
    def Select_Drop_Drown(self):
        self.driver.get("https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select")
        self.driver.maximize_window()
        dropDown = self.driver.find_element(By.NAME,"pets")
        checkBox = Select(dropDown)
        checkBox.select_by_index(1)
        time.sleep(2)
        checkBox.select_by_value("hamster")
        time.sleep(2)
        checkBox.select_by_visible_text("Spider")
        time.sleep(2)

browserObj = BaseElement()
browserObj.Select_Drop_Drown()


