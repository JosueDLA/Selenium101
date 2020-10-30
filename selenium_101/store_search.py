from secrets import driver_path
from selenium import webdriver
import unittest


class StoreSearchTest(unittest.TestCase):
    """
    Test http://demo-store.seleniumacademy.com/      
    """

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search_tee(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        search_field = self.driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='', report_name='store-search-report'))
