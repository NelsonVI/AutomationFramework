from selenium import webdriver
from pages.page_home import *
import unittest
import time

class FlowAvantrip(unittest.TestCase):

    def setUp(self):
        chorme_options = webdriver.ChromeOptions()
        chorme_options.add_argument('--incognito')
        chorme_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome("PythonAutomation/drivers/chromedriver.exe", options=chorme_options)

    def test_flow_buy_flight_National_Destination(self):
        self.driver.get("https://avantrip.com")
        HomePage = Page_Home(self.driver)
        HomePage.input_from_city()
        HomePage.input_to_city()
        HomePage.input_departure_and_arrival_date()
        HomePage.search()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
