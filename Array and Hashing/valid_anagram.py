# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example
# Input: s = "racecar", t = "carrace"

# Output: true

# Brute Force
def is_anagram(s, t):
    if len(s) != len(t):
            return False

    countS, countT = {}, {}

    for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
    
# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1)



# Optimized Approach
def is_anagram(s, t):
    if len(s) != len(t):
            return False
    
    count = {}
    for i in s:
        count[i] = count.get(i,0) + 1
    
    for j in t:
        if j not in count:
              return False
        count[j] -= 1
        if count[j] < 0:
              return False
    return True

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: 
# O(1) if the alphabet is fixed (e.g., lowercase English letters).
# O(k) if the alphabet is unbounded (depends on unique characters in input).

       
print(is_anagram("rat", "car"))
print(is_anagram("anagram", "nagaram"))