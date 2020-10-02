from appium import webdriver
import os

def get_apk():
    apk_path = os.getcwd()
    apk_path = apk_path + "/resoucers/app-release.apk"
    return apk_path

def setup():
    driverOption = {}


    driverOption['app'] = get_apk()
    driverOption['platformName'] = 'Android'
    driverOption['automationName'] = 'UIAutomator2'
    driverOption['deviceName'] = "Android Simulator"
    dirlist = os.listdir("../../tests")

    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", driverOption)

def teardown(driver):
    driver.close()
