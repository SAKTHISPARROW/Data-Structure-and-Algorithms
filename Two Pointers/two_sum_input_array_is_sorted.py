# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Approach 1 (Brute Force)

def two_sum_1(numbers, target):
    i = 0
    j = i + 1
    while  i <= len(numbers) - 2:
        while j <= len(numbers) - 1:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]  
            j += 1
        i += 1
        j = i + 1

print(two_sum_1([5, 25, 75], 100))

# Time & Space Complexity

#     Time complexity: O(n^2)
#     Space complexity: O(1)


# Approach 2(Two Pointers)

def two_sum_2(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        current_sum = numbers[l] + numbers[r]
        if current_sum == target:
            return [l + 1, r + 1]
        
        elif current_sum < target:
            l += 1
        
        else:
            r -= 1
    return []

print(two_sum_2([5, 25, 75], 100))

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(1)
