import unittest
from src.Object.LoginPageObject import LoginPageObject


class MyTestCase(LoginPageObject, unittest.TestCase):

    def test_sem_api_ao_logar_deve_aparecer_erro(self):
        #arrange
        self.go_to_login()
        self.set_email("testedasilva1@grr.la")
        self.set_passoword("qee123")

        #action
        self.submit_form()

        #assert
        assert self.driver.find_element(self.ERROR_LOGIN).text == "Oops, encontramos um erro no aplicativo."

if __name__ == '__main__':
    unittest.main()


