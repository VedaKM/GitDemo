from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check1 = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    radio1 = (By.CSS_SELECTOR, "#inlineRadio1")
    submit = (By.XPATH, "//input[@value='Submit']")
    message = (By.CLASS_NAME, "alert-success")

    shop = (By.LINK_TEXT, "Shop")


    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheck1(self):
        return self.driver.find_element(*HomePage.check1)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getRadio1(self):
        return self.driver.find_element(*HomePage.radio1)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)
    def shopItems(self):
        #return self.driver.find_element(*HomePage.shop) # "*" deserialize the tuple as driver.find_element(By.LINK_TEXT, "Shop")
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage