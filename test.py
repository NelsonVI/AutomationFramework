from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.page_home import *
from pages.result_page import *
from pages.check_out_page import *
import unittest
import time

class FlowAvantrip(unittest.TestCase):

    def setUp(self):
        driverPath = ChromeDriverManager().install()      
        chorme_options = webdriver.ChromeOptions()
        chorme_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(driverPath, options=chorme_options)
        self.driver.implicitly_wait(20)

    def test_flow_buying_flight_national_destination(self):
        self.driver.get("https://avantrip.com")
        Home = HomePage(self.driver)
        Result = ResultPage(self.driver)
        CheckOut = CheckOutPage(self.driver)
        Home.complete_HomePage()
        Result.complete_ResultPage()
        CheckOut.complete_CheckOutPage()

    def tearDown(self):
        self.driver.close()
        

if __name__ == '__main__':
    unittest.main()
