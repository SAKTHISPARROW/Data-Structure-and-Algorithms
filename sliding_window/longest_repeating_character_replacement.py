# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Approach - 1: Sliding Window

def character_replacement(s: str, k: int) -> int:
    count = {}
    max_count = 0
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])

        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

print(character_replacement("AABABBA", 1))

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(m)
#  Where n is the length of the string and m is the total number of unique characters in the string.
