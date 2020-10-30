from pyunitreport import HTMLTestRunner
from selenium import webdriver
from secrets import driver_path
import unittest


class HelloWorld(unittest.TestCase):
    """
    Visit www.google.com        
    """

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(10)

    def test_hello_world(self):
        self.driver.get('https://google.com')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='', report_name='hello-world-report'))
