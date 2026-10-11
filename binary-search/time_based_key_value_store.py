# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:

#     TimeMap() Initializes the object of the data structure.
#     void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#     String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
# Link: https://leetcode.com/problems/time-based-key-value-store/description/

# Approach 1: Binary Search

class TimeMap:

    def __init__(self):
        self.stores= {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.stores:
            self.stores[key] = []
        
        self.stores[key].append([value, timestamp])        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.stores.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            mid_value = left + (right - left) // 2

            if values[mid_value][1] <= timestamp:
                result = values[mid_value][0]
                left = mid_value + 1
            else:
                right = mid_value - 1
             
        return result

obj = TimeMap()
obj.set("foo","bar",1)
param_2 = obj.get("foo",1)
print(param_2)

# Time & Space Complexity

#     Time complexity: O(1) for set() and O(log⁡n) for get()
#     Space complexity: O(m∗n)
# Where n is the total number of values associated with a key and m is the total number of keys.
