# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#Link: https://leetcode.com/problems/trapping-rain-water/description/
#  Approach 1: Brute Force

def trap_1(height):
    if not height:
        return 0

    result = 0
    for i in range(len(height)):
        left_max = right_max = height[i]

        for j in range(i):
            left_max = max(left_max, height[j])
        for j in range(i + 1, len(height)):
            right_max = max(height[j], right_max)

        result += min(left_max, right_max) - height[i]
    return result

print(trap_1([0,1,0,2,1,0,1,3,2,1,2,1]))

# Time & Space Complexity

#     Time complexity: O(n^2)
#     Space complexity: O(1)


# Approach 2: Optimized (Two Pointer)

def trap_2(height):
    if not height:
        return 0
    
    result = 0
    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            result += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            result += right_max - height[r]
    
    return result

print(trap_2([0,1,0,2,1,0,1,3,2,1,2,1]))

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(1)
