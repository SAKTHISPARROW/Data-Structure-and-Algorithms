# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

#     MinStack() initializes the stack object.
#     void push(int value) pushes the element value onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.

# You must implement a solution with O(1) time complexity for each function.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Link: https://leetcode.com/problems/min-stack/description/

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        min_val = min(value, self.min_stack[-1] if self.min_stack else value) 
        self.min_stack.append(min_val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
    
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
print(obj.getMin())

# Time & Space Complexity

#     Time complexity: O(1)
#     Space complexity: O(n)
