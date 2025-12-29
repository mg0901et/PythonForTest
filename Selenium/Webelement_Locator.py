#WEBELEMENTS IN SELENIUM PYTHON

# WebElement provides methods to interact with the elements on a web page, such as clicking buttons etc.

#LOCATORS IN SELENIUM PYTHON

# Locators are used to find elements on a web page. Selenium provides several locator strategies to identify elements, including:
# 1. ID: Locate an element by its unique ID attribute.
# 2. Name: Locate an element by its name attribute.
# 3. Class Name: Locate an element by its class attribute.
# 4. Tag Name: Locate an element by its HTML tag name.
# 5. Link Text: Locate a link element by its exact text.
# 6. Partial Link Text: Locate a link element by partial text.
# CSS Selector: Locate an element using a CSS selector.
# XPath: Locate an element using an XPath expression.

#ID
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

class DemoFindElement:
    """ELEMENT is used to find SINGLE element and perform action on it"""

    driver.get("https://www.google.com/")
    driver.maximize_window()

    def findElementByIDAndName(self): 
        driver.find_element(By.ID,"APjFqb").send_keys("Selenium Python")
        time.sleep(3)
        driver.quit()
    
    def findElementByXpath(self):
        driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("Selenium Python")
        time.sleep(3)
        driver.quit()
    
    def findElementByCssSelector(self):
        driver.find_element(By.CSS_SELECTOR,"#APjFqb").send_keys("Selenium Python")
        time.sleep(3)
        driver.quit()

    def findElementByLinkText(self):
        driver.find_element(By.LINK_TEXT,"Store").click()
        time.sleep(3)
        driver.quit()

class DemoFindListOfElements:
    """ELEMENTS is used to find MULTIPLE elements"""

    driver.get("https://www.google.com/")
    driver.maximize_window()

    def findElementsByTagName(self):
        elements = driver.find_elements(By.TAG_NAME,"a")
        print("Total links are:", len(elements))
        count = 1
        for element in elements:
            print(f"{count}: {element.text}")
            count += 1
        time.sleep(3)
        driver.quit()


# testobj = DemoFindElement()
# testobj.findElementByLinkText()
testobj = DemoFindListOfElements()
testobj.findElementsByTagName() 