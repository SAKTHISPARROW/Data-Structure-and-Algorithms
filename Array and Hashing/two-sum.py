# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Brute Force
def two_sum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Time & Space Complexity
# Time complexity: O(n^2)
# Space complexity: O(1)


# Optimized
def two_sum(nums, target):
    indicies = {}
    for i, n in enumerate(nums):
        indicies[n] = i
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in indicies and indicies[diff] != i:
            return [i, indicies[diff]]
    return []

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)


def two_sum(nums, target):
    prev_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []
# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)


print(two_sum([3,2,4], 6))