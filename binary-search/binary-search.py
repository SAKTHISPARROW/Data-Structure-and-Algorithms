# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Link: https://leetcode.com/problems/binary-search/description/

# Approach 1:

def binary_search(left, right, nums, target):
    if left > right:
        return -1

    mid_value = left + ( right - left) // 2

    if nums[mid_value] == target:
        return mid_value

    elif nums[mid_value] < target:
        return binary_search(mid_value + 1, right, nums, target)

    return binary_search(left, mid_value - 1, nums, target)

def search(nums, target):
    return binary_search(0, len(nums) - 1, nums, target)


print(search([-1,0,3,5,9,12], 9))

# Time & Space Complexity

#     Time complexity: O(logn)
#     Space complexity: O(logn)
