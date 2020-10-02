from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
class BasePageObject(object):

    def Find_Element(self,Driver, element_xpath):
        try:
            WebDriverWait(Driver, 20).until(
                lambda driver: Driver.find_element_by_xpath(element_xpath))
            return Driver.find_element_by_xpath(element_xpath)
        except TimeoutException:
            raise AssertionError("Elemento nao encontado: " +element_xpath)

    def click_and_set_element(self, Driver, xpath_element, string):
        self.Find_Element(Driver, xpath_element).click()
        self.Find_Element(Driver, xpath_element).clear()
        Driver.implicitly_wait(15)
        self.Find_Element(Driver, xpath_element).send_keys(string)