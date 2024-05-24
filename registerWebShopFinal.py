import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageObject.registerPage import RegisterPage,RegisterData
from basePage import register

class WebShopTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_register(self):
        register.setUp(self)
        register.test_register(self,RegisterData.firstname,RegisterData.lastname,RegisterData.email,RegisterData.passw,RegisterData.confirm_pasw)
        register.test_msg_register_success(self)

    def test_register_invalid_email(self):
        register.setUp(self)
        register.test_register(self,RegisterData.firstname,RegisterData.lastname,RegisterData.invalid_email,RegisterData.passw,RegisterData.confirm_pasw)
        register.test_msg_register_failed(self,RegisterPage.invalid_email,RegisterData.invalid_email_msg)

    def test_register_passw_not_match(self):
        register.setUp(self)
        register.test_register(self,RegisterData.firstname,RegisterData.lastname,RegisterData.email,RegisterData.passw,RegisterData.not_confirm_pasw)
        register.test_msg_register_failed(self,RegisterPage.false_password,RegisterData.false_password_msg)
 
if __name__ == '__main__':
    unittest.main()