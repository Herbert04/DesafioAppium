from src.Object.BasePageObject import BasePageObject
from  src.Object.LocatorObject import StartLocator

class StartPageObeject(BasePageObject, StartLocator):

    def White_Account_Click(self, Driver):
        self.Find_Element(Driver, self.WHITE_ACCOUNT_INPUT_XPATH).click()
