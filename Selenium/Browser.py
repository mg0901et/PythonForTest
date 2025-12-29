#Browsers OPERATIONS IN PYTHON USING SELENIUM
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Browser_Operations:
    """ Browser Operations using Selenium WebDriver 
    1. Open Browser --> driver.get("url")  
    2. Maximize Window -->  driver.maximize_window( )
    3. Get Current URL --> driver.current_url
    4. Get Page Title --> driver.title
    5. Fullscreen Window --> driver.fullscreen_window( )
    6. Refresh Page --> driver.refresh( )
    7. Navigate Back --> driver.back( ) 
    8. Navigate Forward --> driver.forward( )
    9. Quit Browser --> driver.quit( )"""

    def __init__(self):
        self.driver = webdriver.Chrome( )
    
    def open_browser(self):
        self.driver.get("https://www.google.com")    
        self.driver.maximize_window( )
        print("Current URL:", self.driver.current_url)
        print("Page Title:", self.driver.title)
        self.driver.fullscreen_window( )
        self.driver.refresh( )
        self.driver.find_element(By.LINK_TEXT, "Store").click( )
        time.sleep(2)
        self.driver.back( )
        time.sleep(2)
        self.driver.forward( )
        time.sleep(2)
        self.driver.quit( )


browserDumy = Browser_Operations( )
browserDumy.open_browser( )

    