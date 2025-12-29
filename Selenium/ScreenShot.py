import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class workingwithSelenium:

    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def gototheURL(self):
        self.driver.get("https://www.yatra.com/")
        self.driver.find_element(By.XPATH,"(//img[@alt='cross'])[1]").click()
        self.driver.maximize_window()


    def captureScreenShot(self):       
        workingwithSelenium.gototheURL(self)
        self.driver.find_element(By.XPATH,"//div[normalize-space()='Login / Signup']").click()
        time.sleep(1)
        LoginButton = self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
        LoginButton.click()
        time.sleep(2)
        LoginButton.screenshot("Selenium/Picture/button.png")
        self.driver.save_screenshot("Selenium/Picture/fullPage.png")




dumyobj = workingwithSelenium()
dumyobj.captureScreenShot()