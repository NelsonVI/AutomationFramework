from pages.basic_page import BasicPage
from src.locators import LocatorsResultPage
from selenium.webdriver.common.by import By

class ResultPage(BasicPage):
    def __init__(self, driver):
        self.locator = LocatorsResultPage
        super().__init__(driver)

    def complete_ResultPage(self):
        self.cluster_available()

    def cluster_available(self, cluster = 1):
        Clusters = self.find_elements(*self.locator.LIST_CLUSTER)
        for i in range(len(Clusters)):
            if i == cluster:
                SeeDetailsBtn = Clusters[i -1].find_element(By.CLASS_NAME, "kWgAlQ")
                SeeDetailsBtn.click()
                TotalPrice = Clusters[i -1].find_element(By.CLASS_NAME, "ijqiAd").text              
                print(TotalPrice.split("\n"))
                BuyBtn = Clusters[i -1].find_element(By.CLASS_NAME, "dXaqlz")
                BuyBtn.is_displayed()
                BuyBtn.click()
                #TODO take info from the total amount and return and arrival flight



