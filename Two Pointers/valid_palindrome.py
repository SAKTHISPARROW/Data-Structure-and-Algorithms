# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Approach 1
def is_palindrome(s):
    chars = [c.lower() for c in s if c.isalnum()]
    i = 0
    j = len(chars) - 1
    while i < j:
        if chars[i] != chars[j]:
            return False
        i += 1
        j -= 1
    return True

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)


# Approach 2
def is_palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l].isalnum() or s[l] == '':
            l += 1
            continue
        if not s[r].isalnum() or s[r] == '':
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1)

        
s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))






