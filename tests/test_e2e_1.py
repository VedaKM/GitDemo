import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup") #remove this line by giving fixture knowledge to base class and inherit the same
class TestOne(BaseClass):
    def test_e2e_1(self):

        log = self.getLogger()
        homepage = HomePage(self.driver)
        #homepage.shopItems().click()
        checkoutpage = homepage.shopItems()
        log.info("getting all the card titles")
        #checkoutpage = CheckOutPage(self.driver)
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()
        checkoutpage.checkOutItems1().click()
        time.sleep(3)
        #checkoutpage.checkOutItems2().click()
        confirmpage = checkoutpage.checkOutItems2()
        #confirmpage = ConfirmPage(self.driver)
        log.info("Entering country name as ind")
        confirmpage.enterCountryName().send_keys("ind")
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        self.verifyLinkPresence("India")
        confirmpage.selectCountryName().click()
        confirmpage.checkTandC().click()
        confirmpage.submitOrder().click()
        success_message = confirmpage.getSuccessMessage().text
        log.info("text received from application is "+success_message)

        assert "Success! Thank you!" in success_message
