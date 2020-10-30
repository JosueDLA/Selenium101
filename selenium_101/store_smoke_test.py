from store_assertions import StoreAssertionTest
from unittest import TestLoader, TestSuite
from store_search import StoreSearchTest
from pyunitreport import HTMLTestRunner

assertoins_test = TestLoader().loadTestsFromTestCase(StoreAssertionTest)
search_test = TestLoader().loadTestsFromTestCase(StoreSearchTest)

smoke_test = TestSuite([assertoins_test, search_test])

kwargs = {'output': 'store-smoke-report'}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
