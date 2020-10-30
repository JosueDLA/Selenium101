from pyunitreport import HTMLTestRunner
from selenium import webdriver
from secrets import driver_path
import unittest


class Store(unittest.TestCase):
    """
    Test http://demo-store.seleniumacademy.com/      
    """

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search_text_field(self):
        """
        Find element by id
        """
        search_field = self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self):
        """
        Find element by name
        """
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_class_name(self):
        """
        Find element by class name
        """
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_search_button_enabled(self):
        """
        Find if button is enabled
        """
        button = self.driver.find_element_by_class_name('button')

    def test_count_banner_images(self):
        """
        Find images in banner
        """
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))

    def test_vip_carousel(self):
        """
        Find element by XPath
        """
        vip_promo = self.driver.find_element_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')

    def test_shoping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector(
            'div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='', report_name='store-report'))
