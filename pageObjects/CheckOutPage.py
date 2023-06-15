from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    #driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitles = (By.CSS_SELECTOR, ".card-title a")  # tuple
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut1 = (By.CSS_SELECTOR, "a[class*=btn-primary]")
    checkOut2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitles)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems1(self):
        return self.driver.find_element(*CheckOutPage.checkOut1)

    def checkOutItems2(self):
        #return self.driver.find_element(*CheckOutPage.checkOut2)
        self.driver.find_element(*CheckOutPage.checkOut2).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

