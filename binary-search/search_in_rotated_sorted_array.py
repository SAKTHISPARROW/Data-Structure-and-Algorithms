# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Approach 1: Sorted Binary Search(Only 148 test cases passed)

def search(nums, target):
    rotated_index = 0
    while nums[0] > nums[-1]:
        rotated_index += 1
        nums.append(nums[0])
        nums.pop(0)
    
    # binary search
    left, right = 0, len(nums) - 1

    while left <= right:
        mid_value = left + (right - left) // 2
        if nums[mid_value] == target:
            return mid_value + rotated_index

        if nums[mid_value] > target:
            right = mid_value - 1
        else:
            left = mid_value + 1

    return -1

print(search([4,5,6,7,0,1,2], 0))

# Time & Space Complexity

#     Time complexity: O(log n)
#     Space complexity: O(1)


# Approach 2: Binary Search

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid_value = left + (right - left) // 2

        if nums[mid_value] == target:
            return mid_value

        if nums[mid_value] >= nums[left]:
            if target < nums[left] or target > nums[mid_value]:
                left = mid_value + 1
            else:
                right = mid_value - 1
        else:
            if target > nums[right] or target < nums[mid_value]:
                right = mid_value - 1
            else:
                left = mid_value + 1

    return -1

print(search([4,5,6,7,0,1,2], 0))

# Time & Space Complexity

#     Time complexity: O(log n)
#     Space complexity: O(1)
