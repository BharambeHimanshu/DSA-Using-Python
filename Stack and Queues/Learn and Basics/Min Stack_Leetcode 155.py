# Min Stack
# Leetcode 155
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

class MinStack:
    def __init__(self):
        # Stack holds pairs: [element_value, current_min]
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            # If stack empty, min is val itself
            self.stack.append([val, val])
        else:
            # Current minimum is top element's min value
            current_min = self.stack[-1][1]
            # New minimum is smaller of val and current min
            new_min = min(current_min, val)
            self.stack.append([val, new_min])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None  # Or raise exception as per requirement
        # Return the value part of the top element
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None  # Or raise exception as per requirement
        # Return the min part of the top element
        return self.stack[-1][1]

m = MinStack()
m.push(10)
m.push(20)
m.push(30)
print(m.pop())
print(m.getMin())