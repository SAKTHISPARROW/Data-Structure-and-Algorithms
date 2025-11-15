# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Approach 1
def is_valid_sudoku(board):
    # Row checking
    for row in board:
        if contains_duplicate(row):
            return False
    
    # Column checking
    for column in range(len(board[0])):
        column_values = []
        for row in range(len(board[0])):
            column_values.append(board[row][column])
        if contains_duplicate(column_values):
            return False
        
    # Square checking
    for square in range(len(board)):
        seen = set()
        for i in range(3):
            for j in range(3):
                row = (square//3) * 3 + i
                column = (square%3) * 3 + j
                if board[row][column] == ".":
                    continue
                if board[row][column] in seen:
                    return False
                
                seen.add(board[row][column])
    return True


def contains_duplicate(nums):
    for i in range(len(nums) - 1):
        if nums[i] == ".":
            continue
        for j in  range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Time & Space Complexity
# Time complexity: O(n ^ 2)
# Space complexity: O(n) 
    


# Approach 2
def is_valid_sudoku(board):
    row = [set() for _ in range(len(board[0]))]
    column = [set() for _ in range(len(board))]
    squares = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(len(board[0])):
        for c in range(len(board)):
            val = board[r][c]
            if val == ".":
                continue

            if val in row[r] or val in column[c] or val in squares[r//3][c//3]:
                return False
            
            row[r].add(val)
            column[c].add(val)
            squares[r//3][c//3].add(val)
    return True

# Time & Space Complexity
# Time complexity: O(n ^ 2)
# Space complexity: O(n ^ 2)



board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

invalid_board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(is_valid_sudoku(board))