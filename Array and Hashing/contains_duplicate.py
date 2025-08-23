# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.
# URL: https://leetcode.com/problems/contains-duplicate/description/


# Brute Force
def containsDuplicate(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Time & Space Complexity
# Time complexity: O(n^2)
# Space complexity: O(1)


# Approach 2
def containsDuplicate(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

# Time & Space Complexity
# Time complexity: O(nlogn)
# Space complexity: O(1) or O(n) depending on the sorting algorithm


# Better Approach 
def containsDuplicate(nums):
    return len(set(nums)) < len(nums)

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)
