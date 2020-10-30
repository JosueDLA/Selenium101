from secrets import driver_path, test_user
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import unittest


class RegisterNewUser(unittest.TestCase):
    """
    Test http://demo-store.seleniumacademy.com/      
    """

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_new_user(self):
        # Account span
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        self.driver.find_element_by_link_text('Log In').click()

        # Create account button
        create_account_button = self.driver.find_element_by_xpath(
            '//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed()
                        and create_account_button.is_enabled())
        create_account_button.click()

        # Assert Window Name
        self.assertEqual('Create New Customer Account', self.driver.title)

        first_name = self.driver.find_element_by_id('firstname')
        middle_name = self.driver.find_element_by_id('middlename')
        last_name = self.driver.find_element_by_id('lastname')
        email_address = self.driver.find_element_by_id('email_address')
        news_letter_subscription = self.driver.find_element_by_id(
            'is_subscribed')
        password = self.driver.find_element_by_id('password')
        confirm_password = self.driver.find_element_by_id('confirmation')
        submit_button = self.driver.find_element_by_xpath(
            '//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and news_letter_subscription.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and submit_button.is_enabled())

        first_name.send_keys(test_user['first_name'])
        middle_name.send_keys(test_user['middle_name'])
        last_name.send_keys(test_user['last_name'])
        email_address.send_keys(test_user['email_address'])
        password.send_keys(test_user['password'])
        confirm_password.send_keys(test_user['confirm_password'])
        submit_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='', report_name='store-new-user-report'))
