# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

#     The valid operators are '+', '-', '*', and '/'.
#     Each operand may be an integer or another expression.
#     The division between two integers always truncates toward zero.
#     There will not be any division by zero.
#     The input represents a valid arithmetic expression in a reverse polish notation.
#     The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/


# Approach 1: stack

def eval_RPN(tokens):
    stack = []

    for c in tokens:
        match c:
            case "+":
                stack.append(stack.pop() + stack.pop())
            case "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            case "*":
                stack.append(stack.pop() * stack.pop())

            case "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            case _:
                stack.append(int(c))

    return stack[-1]

print(eval_RPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

# Time & Space Complexity

#     Time complexity: O(n)
#     Space complexity: O(n)
