import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class tutorialForSelenium():

    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def handleWindow(self):
        self.driver.get("https://www.yatra.com/")
        self.driver.find_element(By.XPATH,"(//img[@alt='cross'])[1]").click()
        self.driver.maximize_window()
        
        MainWindow_Handle = self.driver.current_window_handle
        print(f"Main Window Handle :- {MainWindow_Handle}")

        self.driver.find_element(By.XPATH,"//img[@alt='Winter Travel Fest - Now Live']").click()
        allHandles = self.driver.window_handles
        print(f"All window Handle :- {allHandles}")

        for handle in allHandles:
            if handle != MainWindow_Handle:
                self.driver.switch_to.window(handle)
                self.driver.find_element(By.XPATH,"//a[@title='Hotels']//img[@alt='Domestic']").click()
                allHandles = self.driver.window_handles
                print(f"All window Handle :- {allHandles}")
                self.driver.close()
                break

        time.sleep(4)

    def HandleIframe(self):
        self.driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        self.driver.maximize_window()

        # Switch Frame With ID
        # self.driver.switch_to.frame("iframeResult")

        # Switch Frame With Name
        #self.driver.switch_to.frame("iframeResult")

        # Switch Frame With XPATH
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))


        self.driver.switch_to.frame(0)
        self.driver.find_element(By.XPATH,"//span[@class='button-text']").click()

        time.sleep(5)
    
    def HandleAlert(self):
        self.driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
        self.driver.maximize_window()
        self.driver.switch_to.frame("iframeResult")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()

        self.driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(2)
        text = self.driver.switch_to.alert.text
        print(f" Text in the POPUP is :- {text}")

    def Mouse_oberation(self):
        self.driver.get("https://www.yatra.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,"(//img[@alt='cross'])[1]").click()
        chain = ActionChains(self.driver)
        button1 = self.driver.find_element(By.XPATH,"//p[normalize-space()='Support']")
        button2 = self.driver.find_element(By.XPATH,"//div[normalize-space()='Login / Signup']")
        chain.move_to_element(button2).click().perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//img[@alt='cross'])[1]").click()

        # FOR RIGHT CLICK --->> chain.context_click("XPATH").perform()
        # For Duble Click --->> chain.double_click("XPATH").perform()
        chain.move_to_element(button1).click().perform()
        time.sleep(4)

    def HandleSlider(self):
        self.driver.get("https://www.snapdeal.com/products/electronics-headphones?sort=plrty")
        self.driver.maximize_window()
        element1 = self.driver.find_element(By.XPATH,'//a[contains(@class,"left-handle")]')
        element2 = self.driver.find_element(By.XPATH,'//a[contains(@class,"right-handle")]')
        chain = ActionChains(self.driver)

        # METHOD - 1
        """
        chain.drag_and_drop_by_offset(element1,50,0).perform()
        time.sleep(2)
        chain.drag_and_drop_by_offset(element2,-10,0).perform()
        time.sleep(4)
        """
        
        # METHOD - 2
        """
        chain.click_and_hold(element1).pause(1).move_by_offset(50,0).release().perform()
        time.sleep(2)
        chain.click_and_hold(element2).pause(1).move_by_offset(-50,0).release().perform()
        time.sleep(4)
        """

        #METHOD - 3

        chain.move_to_element(element1).pause(1).click_and_hold(element1).move_by_offset(30,0).release().perform()
        time.sleep(2)
        chain.move_to_element(element2).pause(1).click_and_hold(element2).move_by_offset(-30,0).release().perform()
        time.sleep(4)
    
    def DragAndDrop(self):
        self.driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop")
        self.driver.maximize_window()
        self.driver.switch_to.frame("iframeResult")
        element1 = self.driver.find_element(By.XPATH,"//img[@id='img1']")
        element2 = self.driver.find_element(By.XPATH,"(//div[@id='div1'])[1]")

        chain = ActionChains(self.driver)

        chain.drag_and_drop(element1,element2).perform()
        time.sleep(4)
        

    def implicitWait(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
        self.driver.maximize_window()
        self.driver.switch_to.frame("iframeResult")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        self.driver.switch_to.alert.dismiss()

        self.driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        text = self.driver.switch_to.alert.text
        print(f" Text in the POPUP is :- {text}")

    def explicitWait(self):
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
        wait =  WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//p[@title='Mumbai']"))).click()
        # self.driver.find_element(By.XPATH,"//p[@title='Mumbai']").click()
        textBox = self.driver.find_element(By.XPATH,"//input[@id='input-with-icon-adornment']")
        textBox.send_keys("Pun")
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
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
        time.sleep(4)




testObj = tutorialForSelenium()
testObj.explicitWait()