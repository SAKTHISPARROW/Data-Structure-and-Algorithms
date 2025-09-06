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
    
# Time & Space Complexity
# Time complexity: O(n+m)
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
# Space complexity: O(k)(k is the number of unique characters, ≤ 26 for lowercase English letters)

       
print(is_anagram("rat", "car"))