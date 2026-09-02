# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Link: https://leetcode.com/problems/sliding-window-maximum/description/

# Approach 1: Brute Force(Only 38 test cases passed)

from collections import deque


def max_sliding_window_1(nums, k):
    output = []

    for i in range(len(nums) - k + 1):
        maxi = nums[i]
        for j in range(i, i + k):
            maxi = max(maxi, nums[j])
        output.append(maxi)

    return output

# Time & Space Complexity

#     Time complexity: O(n*k)
#     Space complexity: O(n)


# Approach 2: Deque

def max_sliding_window_2(nums, k):
    output = []
    q = deque()

    left = right = 0

    while right < len(nums):
        while q and nums[q[-1]] < nums[right]:
            q.pop()

        q.append(right)

        if left > q[0]:
            q.popleft()

        if (right + 1) >= k:
            output.append(nums[q[0]])
            left += 1

        right += 1

    return output

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(n)
