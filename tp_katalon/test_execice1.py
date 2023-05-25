from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username = "Admin"
        self.password = "admin123"

    def login(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys(self.username)
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys(self.password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(5)

    def test_login_logout(self):
        self.login()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[2]/ul/li/span/p").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
