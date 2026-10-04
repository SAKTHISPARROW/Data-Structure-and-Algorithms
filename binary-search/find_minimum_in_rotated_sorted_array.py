# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Approach 1:

def find_min_1(nums):
    while nums[0] > nums[-1]:
        nums.append(nums[0])
        nums.pop(0)

    return nums[0]

print(find_min_1([3,4,5,1,2]))

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(1)


# Approach 2: 

def find_min_2(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid_value = left + (right - left) // 2

        if nums[mid_value] < nums[right]:
            right = mid_value
        else:
            left = mid_value + 1

    return nums[left]

print(find_min_2([3,4,5,1,2]))

# Time & Space Complexity

#     Time complexity: O(logn)
#     Space complexity: O(1)
