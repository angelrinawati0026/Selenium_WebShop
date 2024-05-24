import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageObject.registerPage import RegisterPage,RegisterData

def setUp(self):
    global browser
    browser = self.driver

def test_register(self,inputfirstname,inputlastname,inputemail,inputpassw,inputconfirm_pasw):
    browser.get(RegisterData.url)
    self.assertIn(RegisterData.title, browser.title)
    browser.find_element(By.CLASS_NAME, RegisterPage.register_btn).click()
    self.assertEqual(browser.current_url , RegisterData.url_regist)
    browser.find_element(By.CSS_SELECTOR, RegisterPage.gender_btn).click()
    browser.find_element(By.ID, RegisterPage.firstname).send_keys(inputfirstname)
    browser.find_element(By.ID, RegisterPage.lastname).send_keys(inputlastname)
    browser.find_element(By.ID, RegisterPage.email).send_keys(inputemail)
    browser.find_element(By.ID, RegisterPage.passw).send_keys(inputpassw)
    browser.find_element(By.ID, RegisterPage.confirm_passw).send_keys(inputconfirm_pasw)
    browser.find_element(By.ID, RegisterPage.final_regis_btn).click()

def test_msg_register_success(self): 
    browser.find_element(By.CSS_SELECTOR, RegisterPage.continue_btn).click()
    self.assertEqual(browser.current_url , RegisterPage.successregis_url)

def test_msg_register_failed(self,errorpageinput,messageerror):
    error = browser.find_element(By.XPATH, errorpageinput).text
    self.assertIn(messageerror, error)