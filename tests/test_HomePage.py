import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()
        homepage = HomePage(self.driver)
        #homepage.getName().send_keys(getData[0]) # with list
        #homepage.getEmail().send_keys(getData[1])
        log.info("firstname is "+ getData["firstname"])
        homepage.getName().send_keys(getData["firstname"]) # with dictionary
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys("PASSWORD")
        homepage.getCheck1().click()
        #dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        #dropdown.select_by_visible_text('Female')
        #dropdown = Select(homepage.getDropdown())
        #dropdown.select_by_visible_text('Female')
        #homepage.getEmail().send_keys(getData[2])
        self.selectDropDownByText(homepage.getDropdown(), getData["gender"])
        homepage.getRadio1().click()
        time.sleep(3)
        homepage.getSubmit().click()
        time.sleep(3)
        message = homepage.getMessage().text
        assert "Success!" in message
        print(message)
        self.driver.refresh()

    #@pytest.fixture(params=[("veda", "KM", "Female"), ("Megha", "KM", "Male")])
    #@pytest.fixture(params=[{"firstname":"veda","email":"KM","gender":"Female"},{"firstname":"megha","email":"KM", "gender":"Male"}])
    #@pytest.fixture(params=HomePageData.test_HomePage_Data)
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
