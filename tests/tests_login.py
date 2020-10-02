import unittest

from src.Object.LoginPageObject import LoginPageObject

class tests_login(LoginPageObject, unittest.TestCase):
    def test_sem_api_ao_logar_deve_aparecer_erro(self):
        self.go_to_login()
        self.set_email("testedasilva1@grr.la")
        self.set_passoword("qee123")

        self.submit_form()

        assert self.driver.find_element(self.ERROR_LOGIN).text == "Oops, encontramos um erro no aplicativo."