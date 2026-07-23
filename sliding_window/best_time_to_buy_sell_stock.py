# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Approach 1: Brute Force

def max_profit_1(prices):
    max_profit = 0

    for i in range(len(prices)):
        buy_price = prices[i]
        for j in range(i + 1, len(prices)):
            sell_price = prices[j]
            profit = sell_price - buy_price
            max_profit = max(max_profit, profit)

    return max_profit

print(max_profit_1([7,6,4,3,1]))

# Time & Space Complexity

#     Time complexity: O(n^2)
#     Space complexity: O(1)


# Approach 2: Sliding Window

def max_profit_2(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

print(max_profit_2([7,1,5,3,6,4]))

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(1)


# Approach 3: Two pointers

def max_profit_3(prices):
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1

    return max_profit

print(max_profit_3([7,1,5,3,6,4]))

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(1)
