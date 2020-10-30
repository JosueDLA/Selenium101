from pyunitreport import HTMLTestRunner
from selenium import webdriver
from secrets import driver_path
import unittest


class HelloWorld(unittest.TestCase):
    """
    Visit www.google.com        
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        cls.driver.implicitly_wait(10)

    def test_hello_world(self):
        self.driver.get('https://google.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='', report_name='hello-world-report'))
