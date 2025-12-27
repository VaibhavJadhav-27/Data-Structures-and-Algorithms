# ------------------------------------------------------------------------------------------------------------
# Problem no :  706
# Problem heading :  Design HashMap
# Problem Link : https://leetcode.com/problems/design-hashmap/description/

# Problem Description :
#   Design a HashMap without using any built-in hash table libraries.
#
#   Implement the MyHashMap class:
#
#   MyHashMap() initializes the object with an empty map.
#   void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
#   int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
#   void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input
#   ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
#   [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
#   Output
#   [null, null, null, 1, -1, null, 1, null, -1]
#
#   Explanation
#   MyHashMap myHashMap = new MyHashMap();
#   myHashMap.put(1, 1); // The map is now [[1,1]]
#   myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
#   myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
#   myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
#   myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
#   myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
#   myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
#   myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
#  *******************************************************************

class MyHashMap(object):

    def __init__(self):
        self.buckets = {}
        self.size = 0

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.buckets:
            self.buckets[key] = value
        else:
            self.buckets[key] = value
        self.size =  self.size + 1


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.buckets:
            return self.buckets[key]
        else:
            return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.buckets:
            self.buckets.pop(key)
        else:
            return -1
        self.size =  self.size - 1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)