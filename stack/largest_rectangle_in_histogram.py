# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# Approach 1: Stack

def largest_rectangle_area_2(heights):
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        start = i

        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index

        stack.append((start, h))

    for index, height in enumerate(stack):
        max_area = max(max_area, height * (len(heights) - index))

    return max_area

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(n)
