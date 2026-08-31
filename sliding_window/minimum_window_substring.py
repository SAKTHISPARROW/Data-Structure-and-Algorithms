# Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Link: https://leetcode.com/problems/minimum-window-substring/submissions/2126408792/

# Approach - 1: Brute Force(3 test failed due to timeout error) 

def min_window_1(s, t):
    if len(s) < len(t):
        return ""

    letter_count = {}
    results = []
    for letter in range(len(t)):
        letter_count[t[letter]] = 1 + letter_count.get(t[letter], 0)
    

    for l in range(len(s)):
        if s[l] not in t:
            continue

        letter_freq = letter_count.copy()
        res = ""
        for r in range(l, len(s)):
            if s[r] in t:
                letter_freq[s[r]] -= 1
            res += s[r]
            if all(value <= 0 for value in letter_freq.values()):
                results.append(res)
                break

    return min(results, key=len) if len(results) > 0 else ""

# Time & Space Complexity

#     Time complexity: O(n^2)
#     Space complexity: O(n)


# Approach - 2: Sliding Window

def min_window_2(s, t):
    if t == "":
        return ""

    window, count_t = {}, {}
    for c in t:
        count_t[c] = 1 + count_t.get(c, 0)

    have, need = 0, len(count_t)
    result, res_len = [-1, -1], float("infinity")
    left = 0

    for right in range(len(s)):
        letter = s[right]

        window[letter] = 1 + window.get(letter, 0)

        if letter in count_t and window[letter] == count_t[letter]:
            have += 1

        while have == need:
            if (right - left + 1) < res_len:
                result = [left, right]
                res_len = right - left + 1

            window[s[left]] -= 1
            if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                have -= 1

            left += 1

    left, right = result
    return s[left:right + 1] if res_len != float("infinity") else ""

# Time & Space Complexity

#     Time complexity: O(n+m)
#     Space complexity: O(k)

# Where n is the length of the string s, m is the length of the string t, and k is the total number of unique characters in s and t.

# Building the frequency map takes O(m) time. During the sliding-window pass, the right pointer traverses s once and the left pointer advances at most n times in total, so this pass takes O(2n)=O(n) time.
