from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(setup):
        setup.browser=webdriver.Chrome()
        setup.browser.get('http://gmail.com')
        setup.browser.implicitly_wait(10)

    def test_login_valid(valid):
        valid.browser.find_element_by_xpath("//input[@id='identifierId']").send_keys("saisriiram")
        valid.browser.find_element_by_xpath("//button[@jsname='LgbsSe']").click()
    @classmethod
    def tearDownClass(tear):
        tear.browser.close()
        tear.browser.quit()

LoginTest()            


