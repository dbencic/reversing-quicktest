import time
import pickle
from threading import Timer

class cached:
    def __init__(self, function):
        self.__function = function
        self.__store = {}
        self.hits = 0
        self.miss = 0
        print("Created cache for function {0}".format(self.__function))

    def __call__(self, *args, **kwargs):
        key = pickle.dumps(args, 1) + pickle.dumps(kwargs, 1)#non hashable args can be used
        if (key in self.__store):
            print("Returning function result for arguments {0} from cache".format(key))
            self.hits = self.hits + 1
            return self.__store[key].get_item()

        value = self.__function(*args, **kwargs)
        print("Invoking memorized function with key {0}. Got value {1}".format(key, value))
        self.__store[key] = _CachedItem(value, self, key)
        self.miss = self.miss + 1
        return value

    def remove(self, key):
        if key in self.__store:
            del self.__store[key]

    def stat(self):
        return {"hits" : self.hits, "miss" : self.miss}

    def clear(self):
        print("Clearing cache for function {0}".format(self.__function))
        self.__store.clear()
        self.hits = 0
        self.miss = 0


class _CachedItem:
    def __init__(self, item, cache, key):
        self.__item = item
        self.count = 0
        self.created = time.clock()
        self.__cache = cache
        self.__key = key
        #Evicting after 5 min. This may not be best solution for large number different of arguments
        Timer(300, self.evict).start()

    def evict(self):
        print("Evicting function result from cache for key {0}".format(self.__key))
        self.__cache.remove(self.__key)

    def get_item(self):
        self.count = self.count + 1
        if (self.count == 5):
            self.evict()
        return self.__item
