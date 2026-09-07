# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Link: https://leetcode.com/problems/daily-temperatures/description/

# Approach 1: Brute Force(Only 35 out of 48 test cases passed)

def daily_temperatures_1(temperatures):
    result = []
    for l in range(len(temperatures) - 1):
        stack = []
        for r in range(l + 1, len(temperatures)):
            if stack and stack[-1] > temperatures[l]:
                break

            stack.append(temperatures[r])

        result.append(len(stack) if (stack and stack[-1] > temperatures[l]) else 0)
    result.append(0)
    return result

# Time & Space Complexity

#     Time complexity: O(n^2)
#     Space complexity: O(n)


# Approach 2: Stack

def daily_temperatures_2(temperatures):
    stack = []
    res = [0] * len(temperatures)

    for i, temperature in enumerate(temperatures):
        while stack and temperature > stack[-1][0]:
            _, stack_index = stack.pop()
            res[stack_index] = i - stack_index

        stack.append((temperature, i))

    return res

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(n)
