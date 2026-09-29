# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Link: https://leetcode.com/problems/koko-eating-bananas/description/

# Approach 1: Linear Search(Brute Force)
import math

def min_eating_speed_1(piles, h):
    current_index = 0
    min_no_bananas = 1
    total_hours = 0
    while current_index < len(piles):
        total_hours = total_hours + math.ceil(piles[current_index]/min_no_bananas)
        
        if total_hours > h:
            current_index = 0
            min_no_bananas += 1
            total_hours = 0
            continue
        
        current_index += 1

    return min_no_bananas

print(min_eating_speed_1([3,6,7,11], 8))
print(min_eating_speed_1([30,11,23,4,20], 5))
print(min_eating_speed_1([30,11,23,4,20], 6))

# Time & Space Complexity

#     Time complexity: O(n * m)
#     Space complexity: O(1)
#  where n is the number of piles and m is the maximum number of bananas in a pile


# Approach 2: Binary search
def min_eating_speed_2(piles, h):
    # we are doing binary search on the range of possible eating speeds, 
    # which is from 1 to the maximum number of bananas in a pile
    left, right = 1, max(piles)  

    result = 0

    while left <= right:
        mid_value = (left + right) // 2

        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / mid_value)

        if total_hours <= h:
            result = mid_value
            right = mid_value - 1

        else:
            left = mid_value + 1

    return result

print(min_eating_speed_2([3,6,7,11], 8))
print(min_eating_speed_2([30,11,23,4,20], 5))
print(min_eating_speed_2([30,11,23,4,20], 6))

# Time & Space Complexity

#     Time complexity: O(n * log m)
#     Space complexity: O(1)
#  Where m is the maximum number of bananas in a pile and n is the number of piles.
