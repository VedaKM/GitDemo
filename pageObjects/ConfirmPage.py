from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    enterCountry = (By.ID, "country")  #tuple
    selectCountry = (By.LINK_TEXT, "India")
    checkTC = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def enterCountryName(self):
        return self.driver.find_element(*ConfirmPage.enterCountry)

    def selectCountryName(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def checkTandC(self):
        return self.driver.find_element(*ConfirmPage.checkTC)

    def submitOrder(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)
