# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#Link: https://leetcode.com/problems/container-with-most-water/description/

# Approach 1: Brute Force

def max_area_1(height):
    result = 0

    for i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            result = max(result, min(height[i], height[j]) * (j - i))
    
    return result

print(max_area_1([1,8,6,2,5,4,8,3,7]))

# Time & Space Complexity

#     Time complexity: O(n^2)
#     Space complexity: O(1)


# Approach 2: Optimized (Two Pointer)

def max_area_2(height):
    result = 0

    l, r = 0, len(height) - 1

    while l < r:
        result = max(result, min(height[l], height[r]) * (r - l))

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    
    return result

print(max_area_2([1,8,6,2,5,4,8,3,7]))

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(1)
