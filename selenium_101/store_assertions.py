from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from secrets import driver_path
from selenium import webdriver
import unittest


class StoreAssertionTest(unittest.TestCase):
    """
    Test http://demo-store.seleniumacademy.com/      
    """

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        """
        Identify if element is available

        :param how: type of selector

        :param what: value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='', report_name='store-assertion-report'))
