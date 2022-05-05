from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.webdriver import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
from webdriver_manager.microsoft import IEDriverManager
from pom_tests import conf


class LoginPage:

    def __init__(self):
        self.browser = None

    def get_driver_instance(self, browser_name):
        if conf.browser == 'Chrome':
            self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        if conf.browser == 'Firefox':
            self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        return self.browser


    def hr_login(self, username, userpassword):
        self.browser.get('http://hrm-online.portnov.com/')
        self.browser.maximize_window()
        self.browser.find_element(By.XPATH, '//input[contains(@id, "Username")]').send_keys(username)
        self.browser.find_element(By.NAME, 'txtPassword').send_keys(userpassword)
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="btnLogin"]').click()

