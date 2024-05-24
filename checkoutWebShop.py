import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageObject.loginPage import LoginData,LoginPage
from pageObject.checkoutPage import CheckoutData,CheckoutPage
from basePage import login
from selenium.webdriver.support.ui import Select
import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class WebShopTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_add_cart(self):
        browser = self.driver
        login.setUp(self)
        login.test_login(self,LoginData.email,LoginData.passw)
        login.test_msg_login_success(self)
        browser.find_element(By.CSS_SELECTOR, CheckoutPage.img_produk).click()
        browser.find_element(By.ID, CheckoutPage.recepient_name).send_keys(CheckoutData.recepient_name_data)
        browser.find_element(By.ID, CheckoutPage.recepient_email).send_keys(CheckoutData.recepient_name_email)
        browser.find_element(By.CSS_SELECTOR, CheckoutPage.add_cart_btn).click()
        #add_cart = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification .content"))).text
        #add_cart = browser.find_element(By.CSS_SELECTOR,  "#bar-notification .content").text
        #self.assertIn('The product has been added to your', add_cart )
        
    def test_cart(self):
        browser = self.driver
        browser = self.driver
        login.setUp(self)
        login.test_login(self,LoginData.email,LoginData.passw)
        login.test_msg_login_success(self)
        browser.find_element(By.CLASS_NAME, CheckoutPage.cart_btn).click()
        browser.find_element(By.ID, CheckoutPage.term_condt).click()
        browser.find_element(By.ID, CheckoutPage.checkout_btn).click()
        self.assertEqual(browser.current_url ,CheckoutData.personal_data_url)
        #browser.find_element(By.ID, 'BillingNewAddress_CountryId').click()
        time.sleep(6)

if __name__ == '__main__':
    unittest.main()