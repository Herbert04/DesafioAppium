from src.Object.BasePageObject import BasePageObject
from src.Object.WelcomePageObject import WelcomePageObeject
from src.Object.StartPageObject import StartPageObeject
from src.Object.LocatorObject import LoginLocator

from src.Util import conftest

import unittest

class LoginPageObject(BasePageObject, LoginLocator, unittest.TestCase):

    def go_to_login(self):
        self.driver = conftest.setup()
        welcome = WelcomePageObeject()
        welcome.Deny_Access_Click(self.driver)
        welcome.Advance_Welcome_Click(self.driver)
        StartPageObeject().White_Account_Click(self.driver)

    def set_email(self, email):
        self.click_and_set_element(self.driver, self.EMAIL_LABEL_XPATH, email)

    def set_passoword(self, passoword):
        self.click_and_set_element(self.driver, self.SENHA_LABEL_XPATH, passoword)

    def submit_form(self):
        self.Find_Element(self.driver, self.ACCOUNT_ACESS_XPATH).click()

