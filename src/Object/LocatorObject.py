
class LoginLocator(object):
    EMAIL_LABEL_XPATH = "//android.widget.EditText[@text='Seu e-mail']"
    SENHA_LABEL_XPATH = "//android.widget.EditText[@text='Senha']"
    ACCOUNT_ACESS_XPATH = "//android.widget.EditText[@text='Acessar Conta']"
    ERROR_LOGIN = "//android.widget.EditText[@text='Oops, encontramos um erro no aplicativo.']"

class StartLocator(object):
    WHITE_ACCOUNT_INPUT_XPATH = "//android.view.View[@text='Já tenho conta']"

class WelcomeLocator(object):
    ACCESS_DENY_INPUT_XPATH = "//android.widget.Button[@resource-id='com.android.packageinstaller:id/permission_deny_button']"
    PROXIMO_DENY_INPUT_XPATH = "//android.widget.Button[@text='Próximo']"
    START_DENY_INPUT_XPATH = "//android.widget.Button[@text='Vamos começar']"