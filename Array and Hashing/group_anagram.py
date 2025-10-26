# Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Brute Force
def group_anagrams(strs):
    visited = [0] * len(strs)
    result = []
    for i in range(len(strs)):
        if visited[i] == 1:
            continue
        visited[i] = 1
        group_anagrams = [strs[i]]
        for j in range(i + 1, len(strs)):
            if is_anagram(strs[i], strs[j]):
                group_anagrams.append(strs[j])
                visited[j] = 1
        result.append(group_anagrams)
    return result

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
# Time complexity: O(n² × m)
# Space complexity: O(n × m)
# n = number of strings
# m = average length of each string.


# Optimized Approach
def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return list(anagrams.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

# Time & Space Complexity
# Time complexity: O(n × m log m)
# Space complexity: O(n × m)
# n = number of strings
# m = average length of each string.
