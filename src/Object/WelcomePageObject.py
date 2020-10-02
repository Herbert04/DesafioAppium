from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.Object.BasePageObject import BasePageObject
from  src.Object.LocatorObject import WelcomeLocator
import unittest


class WelcomePageObeject(BasePageObject, WelcomeLocator,unittest.TestCase):


    def Deny_Access_Click(self, Driver):
        for i in range(0, 3):
            self.Find_Element(Driver, self.ACCESS_DENY_INPUT_XPATH).click()


    def Advance_Welcome_Click(self, Driver):
        for i in range(0, 2):
            self.Find_Element(Driver, self.PROXIMO_DENY_INPUT_XPATH).click()

        self.Find_Element(Driver,self.START_DENY_INPUT_XPATH).click()

