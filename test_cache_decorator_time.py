#cache decorator test file. tests eviction based on elapsed time
import unittest
from cache_decorator import cached
import time

class TestCacheDecorator(unittest.TestCase):

    def setUp(self):
        current_time.clear()

    def test5minutesEviction(self):
        sleepTime = 302;#5 min and 2 seconds
        print_test_title("Testing evict due to time. going to sleep for {0} seconds".format(sleepTime))
        initial_value = current_time()
        time.sleep(sleepTime)
        self.assertNotEqual(current_time(), initial_value)

    def test5minutesEviction(self):
        sleepTime = 298;#5 min minus 2 seconds
        print_test_title("Testing evict due to time. going to sleep for {0} seconds".format(sleepTime))
        initial_value = current_time()
        time.sleep(sleepTime)
        self.assertEqual(current_time(), initial_value)


def print_test_title(title):
    print("\n****{0}****".format(title))

@cached
def current_time():
    return time.clock();


if __name__ == '__main__':
    unittest.main()