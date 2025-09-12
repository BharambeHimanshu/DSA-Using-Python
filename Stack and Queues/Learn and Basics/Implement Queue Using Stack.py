# Implement Queue(FIFO) Using  2 Stack(LIFO)

from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Helper queue
    
    def push(self, x):
        self.q2.append(x)  # Add new element to helper
        # Move all from main to helper
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap: helper becomes main
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        return self.q1.popleft()  # Remove front (top of stack)
    
    def top(self):
        return self.q1[0]  # Peek front
    
    def empty(self):
        return len(self.q1) == 0  # Check if main is empty
    
stack = MyStack()
stack.push(10)
stack.push(20)
stack.push(30)
print("element popped : ",stack.pop())
print("Top element", stack.top())
stack.push(50)
print("element popped : ",stack.pop())
print("Top element", stack.top())