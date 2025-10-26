# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Brute Force
def product_except_self(nums):
    result = [0] * len(nums)
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i == j:
                continue
            product *= nums[j]
        result[i] = product
    return result

# Time & Space Complexity
# Time complexity: O(n ^ 2)
# Space complexity: 
#  O(1) extra space.
#  O(n) space for the output array.


# Division
def product_except_self(nums):
    prod, zero_cnt = 1, 0
    for num in nums:
        if num:
            prod *= num
        else:
            zero_cnt += 1
    if zero_cnt > 1: 
        return [0] * len(nums)
    
    res = [0] * len(nums)
    for i, c in enumerate(nums):
        if zero_cnt: res[i] = 0 if c else prod
        else:
            res[i] = prod//c
    return res

# Time & Space Complexity
# Time complexity: O(n2)
# Space complexity: 
#  O(1) extra space.
#  O(n) space for the output array.


# Optimized Approach
def product_except_self(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: 
#  O(1) extra space.
#  O(n) space for the output array.

print(product_except_self([1,2,3,4]))