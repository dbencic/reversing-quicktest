#cache decorator test file. tests eviction based on number of cache hits
import unittest
from cache_decorator import cached
import time

class TestCacheDecorator(unittest.TestCase):

    def setUp(self):
        current_time.clear()
        current_time_with_args.clear()

    def test5times(self):#testing that value can be retreived 5 times from cache
        print_test_title("testing 5 calls, all should return cached value")
        initial_value = current_time()
        for i in range (0, 4):
            current_time()#calls function 4 times
        self.assertEqual(current_time(), initial_value)
        print(current_time.stat())

    def test6times(self):#testing that value on 6-th invocation will be recreated
        print_test_title("testing 6 calls, the last should return new value")
        initial_value = current_time()
        for i in range (0, 5):
            current_time()#calls function 5 times
        self.assertNotEqual(current_time(), initial_value)
        print(current_time.stat())

    def test_cache_with_args_5_times(self):#testing that value can be retreived 5 times from cache
        print_test_title("Testing 5 calls of function with parameters")
        initial_value = call_function_with_args()
        for i in range (0, 4):
            call_function_with_args()#calls function 4 times
        self.assertEqual(call_function_with_args(), initial_value)
        print(current_time_with_args.stat())

    def test_cache_with_args_6_times(self):#testing that value on 6-th invocation will be recreated
        print_test_title("Testing 5 calls of function with parameters")
        initial_value = call_function_with_args()
        for i in range (0, 5):
            call_function_with_args()#calls function 5 times
        self.assertNotEqual(call_function_with_args(), initial_value)
        print(current_time_with_args.stat())


def print_test_title(title):
    print("\n****{0}****".format(title))

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
