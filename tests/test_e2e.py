import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup") #remove this line by giving fixture knowledge to base class and inherit the same
class TestOne(BaseClass):
    def test_e2e(self):

        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()  # using CSS Selector and regular expression
        # driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click() # using XPATH and regular expression
        # using regular expression is not recommended as there are chances of code break

        self.driver.find_element(By.LINK_TEXT, "Shop").click()  # using link text
        items = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for item in items:
            productName = item.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                item.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*=btn-primary]").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_message = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in success_message
