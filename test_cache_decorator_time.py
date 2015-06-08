#cache decorator test file. tests eviction based on elapsed time
import unittest
from cache_decorator import cached
import time
import logging

logging.basicConfig(level=logging.INFO)

class TestCacheDecoratorTime(unittest.TestCase):

    def tearDown(self):
        print("***********tearing down***********")
        current_time.clear()

    def test5minutesEviction(self):
        sleepTime = 301;#5 min and 1 seconds
        logging.debug("Testing evict due to time. going to sleep for {0} seconds".format(sleepTime))
        initial_value = current_time()
        time.sleep(sleepTime)
        self.assertNotEqual(current_time(), initial_value)
        print(current_time.stat())

    def testLessThan5minutesEviction(self):
        sleepTime = 299;#5 min minus 1 second
        logging.debug("Testing evict due to time. going to sleep for {0} seconds".format(sleepTime))
        initial_value = current_time()
        time.sleep(sleepTime)
        self.assertEqual(current_time(), initial_value)
        print(current_time.stat())

@cached
def current_time():
    return time.clock();


if __name__ == '__main__':
    unittest.main()
