# You are given an m x n integer matrix matrix with the following two properties:
#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
# Link: https://leetcode.com/problems/search-a-2d-matrix/description/

# Approach 1:

def search_matrix_1(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False

# Time & Space Complexity

#     Time complexity: O(log m+log n) (which reduces to O(log⁡(m∗n))
#     Space complexity: O(1)
#  Where m is the number of rows and n is the number of columns of matrix.


# Approach 2:     

def search_matrix_2(matrix, target):
    ROW, COL = len(matrix), len(matrix[0])

    left, right = 0, ROW * COL - 1

    while left <= right:
        mid_value = left + (right - left) // 2
        row, col = mid_value // COL, mid_value % COL

        if target > matrix[row][col]:
            left = mid_value + 1
        elif target < matrix[row][col]:
            right = mid_value - 1
        else:
            return True

    return False

print(search_matrix_1([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(search_matrix_2([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))

# Time & Space Complexity

#     Time complexity: O(log⁡(m∗n)
#     Space complexity: O(1)
#  Where m is the number of rows and n is the number of columns of matrix.
