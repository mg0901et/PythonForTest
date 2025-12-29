import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DemoExecution:

    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def AutoSelectWithEnter(self):
        self.driver.get("https://www.yatra.com/react-home/flights")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//p[@title='New Delhi']").click()
        textBox = self.driver.find_element(By.XPATH,"(//input[@id='input-with-icon-adornment'])[1]")
        time.sleep(2)
        textBox.send_keys("New Y")
        time.sleep(2)
        # textBox.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH,"//span[normalize-space()='New York']").click()
        time.sleep(2)
    
    def FindLenofSuggestion(self):
        self.driver.get("https://www.yatra.com/react-home/flights")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//p[@title='New Delhi']").click()
        textBox = self.driver.find_element(By.XPATH,"(//input[@id='input-with-icon-adornment'])[1]")
        textBox.send_keys("New")
        time.sleep(2)
        listSuggestion = self.driver.find_elements(By.XPATH,"//div[@class='MuiBox-root css-134xwrj']//ul//div")
        print(len(listSuggestion))
        count = 0
        for result in listSuggestion:
            print(f"{count} - {result.text}")
            count = count+1
            if "NYC" in result.text:
                result.click()
                break
        time.sleep(4)

    def WorkWithCalender(self):
        self.driver.get("https://www.yatra.com/react-home/flights")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,"//p[@title='New Delhi']").click()
        textBox = self.driver.find_element(By.XPATH,"(//input[@id='input-with-icon-adornment'])[1]")
        textBox.send_keys("New")
        time.sleep(2)
        listSuggestion = self.driver.find_elements(By.XPATH,"//div[@class='MuiBox-root css-134xwrj']//ul//div")
        print(len(listSuggestion))
        count = 0
        for result in listSuggestion:
            # print(f"{count} - {result.text}")
            count = count+1
            if "NYC" in result.text:
                result.click()
                break
        self.driver.find_element(By.XPATH,"//p[@title='Mumbai']").click()
        textBox = self.driver.find_element(By.XPATH,"//input[@id='input-with-icon-adornment']")
        textBox.send_keys("Pun")
        time.sleep(2)
        listSuggestion = self.driver.find_elements(By.XPATH,"(//ul)[2]//div")
        print(len(listSuggestion))
        count = 0
        for result in listSuggestion:
            # print(f"{count} - {result.text}")
            count = count+1
            if "PNQ" in result.text:
                result.click()
                break
        self.driver.find_element(By.XPATH,"//div[@aria-label='Departure Date inputbox']").click()
        time.sleep(2)
        textBox = self.driver.find_elements(By.XPATH,"//div[contains(@aria-label,'2026-01')]//div//div[@aria-label]")
        print(f"List Of DATE:- {len(textBox)}")  
        count = 0
        for result in range(len(textBox)):
            date_elements = self.driver.find_elements(By.XPATH,"//div[contains(@aria-label,'2026-01')]//div//div[@aria-label]")
            if count < len(date_elements):
                result = date_elements[count]
                aria_label = result.get_attribute("aria-label")
                print(f"{count} - {aria_label}")
                if "January 4th, 2026" in aria_label:
                    result.click()
                    break
            count = count+1
        time.sleep(4)



    

    
        


testobj = DemoExecution()
testobj.WorkWithCalender()