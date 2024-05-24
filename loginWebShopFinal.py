import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageObject.loginPage import LoginData,LoginPage
from basePage import login


class WebShopTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login(self):
        login.setUp(self)
        login.test_login(self,LoginData.email,LoginData.passw)
        login.test_msg_login_success(self)

    def test_login_pass_false(self):
        login.setUp(self)
        login.test_login(self,LoginData.email,LoginData.passw_false)
        login.test_msg_login_failed(self,LoginData.false_pass_msg)

    def test_login_email_not_found(self):
        login.setUp(self)
        login.test_login(self,LoginData.email_not_found,LoginData.passw_false)
        login.test_msg_login_failed(self,LoginData.email_notfound_msg)
 
if __name__ == '__main__':
    unittest.main()