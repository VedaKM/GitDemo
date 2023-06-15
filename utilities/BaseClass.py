import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        #logger_obj = logging.getLogger(__name__)  # logger obj is responsible to print everything in file in specific format
        logger_obj = logging.getLogger(loggerName)

        # PASS filehandler class object(file location) into it
        filehandler_obj = logging.FileHandler('logfile.log')
        formatter_obj = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler_obj.setFormatter(formatter_obj)
        logger_obj.addHandler(filehandler_obj)  # this method will accept File Handler object
        logger_obj.setLevel(logging.DEBUG)
        return logger_obj
    def verifyLinkPresence(self, text):
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectDropDownByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)