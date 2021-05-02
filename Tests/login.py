# from selenium.webdriver.support import expected_conditions as EC
import unittest

from selenium import webdriver


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(executable_path="C:/Users/Ram/chromedriver.exe")
        cls.browser.get('http://gmail.com')
        cls.browser.maximize_window()

    def test_login_valid(self):
        self.browser.find_element_by_xpath("//input[@id='identifierId']").send_keys("saisriiram")
        self.browser.find_element_by_xpath("//button[@jsname='LgbsSe']").click()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
