
# ------------------------------------------------------------------------------------------------------------
# Problem no :  146
# Problem heading :  LRU Cache
# Problem Link : https://leetcode.com/problems/lru-cache/description/

# Problem Description : 
#   Implement the LRUCache class:
#   LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#   int get(int key) Return the value of the key if the key exists, otherwise return -1.
#   void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#   The functions get and put must each run in O(1) average time complexity.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#           [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#   Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
#   Explanation: 
#   LRUCache lRUCache = new LRUCache(2);
#   lRUCache.put(1, 1); // cache is {1=1}
#   lRUCache.put(2, 2); // cache is {1=1, 2=2}
#   lRUCache.get(1);    // return 1
#   lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
#   lRUCache.get(2);    // returns -1 (not found)
#   lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
#   lRUCache.get(1);    // return -1 (not found)
#   lRUCache.get(3);    // return 3
#   lRUCache.get(4);    // return 4


#  *******************************************************************
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.lru = []


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # Move key to end (most recently used)
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # Update existing key
            self.cache[key] = value
            self.lru.remove(key)
            self.lru.append(key)
        else:
            if len(self.cache) == self.capacity:
                # Evict least recently used
                lru_key = self.lru.pop(0)
                self.cache.pop(lru_key)
            # Insert new key
            self.cache[key] = value
            self.lru.append(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)