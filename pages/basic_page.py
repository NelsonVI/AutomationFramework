from selenium.webdriver.common.by import By

class BasicPage():
    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, *locator):    
        return self.driver.find_element(*locator)
    
    def find_elements(self, *locator):    
        return self.driver.find_elements(*locator)
    
    def send_keys_element(self, element, text=''):
        return element.send_keys(text)
    
    def click_element(self, element):
        return element.click()
    