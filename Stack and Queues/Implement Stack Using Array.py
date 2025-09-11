# Implement Stack Using Array
# GFG Problem
'''
Input: oper[] = [1, 2, 1, 3, 2, 1, 4, 2] 
Output: [3, 4]
Explanation: 
push(2)   the stack will be {2}
push(3)   the stack will be {2 3}
pop()     poped element will be 3, the stack will be {2}
push(4)   the stack will be {2 4}
pop()     poped element will be 4
'''

class Stack:
    def __init__(self):
        self.items = []

    # Check if the stack is empty       o(1)
    def is_empty(self):
        return len(self.items) == 0
    
    # Push Operation                    o(1)
    def push(self,item):
        self.items.append(item)

    # Pop Operation                     o(1)
    def pop(self):
        if len(self.items) == 0:
            return "cannot pop, stack is empty"
        x = self.items.pop()
        return x
    
    # Top operation                     o(1)
    def top(self):
        if len(self.items) == 0:
            return "cannot pop, stack is empty"
        return self.items[-1]
    
    # Size
    def size(self):
        return len(self.items)
    
stack = Stack()
stack.push(20)
stack.push(30)
print("Popped:", stack.pop())   # prints popped element
stack.push(40)
print("Popped:", stack.pop())   # prints popped element
print("Top element:", stack.top())  # prints top element
print("Stack size:", stack.size())  # prints size of stack
