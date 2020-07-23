from src.locators import MainPageLocators
from pages.basic_page import BasicPage
from selenium.webdriver.common.keys import Keys

class HomePage(BasicPage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def complete_HomePage(self):
        self.close_pop_up()
        self.input_from_city()
        self.input_to_city()
        self.input_departure_date()
        self.input_arrival_date()
        self.search_btn()
    
    def close_pop_up(self):
        popUp = self.find_element(*self.locator.POPUP)
        try:
            self.click_element(popUp)
        except:
            print('No Pop Up visible')
    
    def input_from_city(self):
        FromCity = self.find_element(*self.locator.FROM_CITY)
        self.send_keys_element(FromCity, "Buenos Aires")
        self.send_keys_element(FromCity, Keys.ENTER)

    def input_to_city(self):
        ToCity = self.find_element(*self.locator.TO_CITY)
        self.send_keys_element(ToCity, 'Mendoza')
        self.send_keys_element(ToCity, Keys.ENTER)
    
    def input_departure_date(self):
        Departure = self.find_element(*self.locator.DEPARTURE_DATE)
        self.send_keys_element(Departure, '12/12/2020') # change this
    
    def input_arrival_date(self):
        Arrival = self.find_element(*self.locator.ARRIVAL_DATE)
        self.send_keys_element(Arrival, "20/12/2020")

    #def input_pax(self):

    def search_btn(self):        
        Search = self.find_element(*self.locator.SUBMIT_BTN)
        self.click_element(Search)
