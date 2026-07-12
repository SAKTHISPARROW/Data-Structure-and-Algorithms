# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# link: https://leetcode.com/problems/3sum/description/

# Approach 1: Brute Force

def three_sum_1(nums):
    result = set()
    nums.sort()
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp = [nums[i], nums[j], nums[k]]
                    result.add(tuple(tmp))

    
    return [list(res) for res in result]

print(three_sum_1([-1,0,1,2,-1,-4]))

# Time & Space Complexity

#     Time complexity: O(n^3)
#     Space complexity: O(n)


# Approach 2: Optimized (Two Pointer)

def three_sum_2(nums):
    result = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:     # To skip the duplicate values of 'a'
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            current_sum = a + nums[l] + nums[r]
            if current_sum > 0:
                r -= 1
            
            elif current_sum < 0:
                l += 1
            
            else:
                result.append([a, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:     # To skip the duplicate values of 'l'
                    l += 1
    
    return result

print(three_sum_2([-1,0,1,2,-1,-4]))

# Time & Space Complexity

#     Time complexity: O(n^2)
#     Space complexity: O(n) or O(1)
