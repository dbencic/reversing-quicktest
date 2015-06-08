#cache decorator test file. tests eviction based on number of cache hits
import unittest
from cache_decorator import cached
import time
import logging

logging.basicConfig(level=logging.INFO)

class TestCacheDecorator(unittest.TestCase):

    def tearDown(self):
        logging.debug("************tearing down***********")
        current_time.clear()
        current_time_with_args.clear()

    def test10times(self):#testing that value can be retreived 5 times from cache
        logging.info("testing 10 calls, all should return cached value")
        initial_value = current_time()
        for i in range (0, 9):
            current_time()#calls function 4 times
        self.assertEqual(current_time(), initial_value)
        print(current_time.stat())

    def test11times(self):#testing that value on 6-th invocation will be recreated
        logging.info("testing 11 calls, the last should return new value")
        initial_value = current_time()
        for i in range (0, 10):
            current_time()#calls function 5 times
        self.assertNotEqual(current_time(), initial_value)
        print(current_time.stat())

    def test_cache_with_args_10_times(self):#testing that value can be retreived 5 times from cache
        logging.info("Testing 10 calls of function with parameters")
        initial_value = call_function_with_args()
        for i in range (0, 9):
            call_function_with_args()#calls function 4 times
        self.assertEqual(call_function_with_args(), initial_value)
        print(current_time_with_args.stat())

    def test_cache_with_args_11_times(self):#testing that value on 6-th invocation will be recreated
        logging.info("Testing 11 calls of function with parameters, the last call should return new value")
        initial_value = call_function_with_args()
        for i in range (0, 10):
            call_function_with_args()#calls function 5 times
        self.assertNotEqual(call_function_with_args(), initial_value)
        print(current_time_with_args.stat())

    def test_different_arguments_return_different_value(self):
        logging.info("Testing 2 calls vith different parameters. Different results should be returned")
        value1 = current_time_with_args("prefix", "suffix", [1,2,3])
        value2 = current_time_with_args("prefix", "suffix", [1,3,4])
        self.assertNotEqual(value1, value2)
        print(current_time_with_args.stat())

def call_function_with_args():
    return current_time_with_args("prefix", "suffix", [1,2,3])

@cached
def current_time():
    return time.clock();

@cached
def current_time_with_args(prefix, suffix, some_mutable):
    return "{0}-{1}-{2}-mutable:{3}".format(prefix, time.clock(), suffix, some_mutable);


if __name__ == '__main__':
    unittest.main()
