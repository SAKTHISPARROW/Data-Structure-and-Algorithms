# Given a string s, find the length of the longest without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


# Approach 1: Brute Force

def length_of_longest_substring_1(s):
    if s == "":
        return 0

    res = ""
    max_count = 1
    for i in range(len(s)):
        res = s[i]
        for j in range(i + 1, len(s)):
            if s[j] in res:
                break
            res += s[j]
            max_count = max(max_count, len(res))
    return max_count

print(length_of_longest_substring_1("1R1T7"))

# Time & Space Complexity

#     Time complexity: O(n∗m)
#     Space complexity: O(m)


#  Approach 2: Sliding Window

def length_of_longest_substring(s):
    res = 0
    for i in range(len(s)):
        charSet = set()
        for j in range(i, len(s)):
            if s[j] in charSet:
                break
            charSet.add(s[j])
        res = max(res, len(charSet))
    return res

print(length_of_longest_substring("pwwkew"))

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(m)
#  Where n is the length of the string and m is the total number of unique characters in the string.
