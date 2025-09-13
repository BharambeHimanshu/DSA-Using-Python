# Implement Stack (FIFO) Using DLL

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None       # Head -> None

    # Push Operation
    def push(self,data):
        new_node = Node(data)   # Craete a New Node
        new_node.next = self.head    # Next of new node points to the old head
        self.head = new_node         # Move head to new node

    # Pop Operation
    def pop(self):
        if self.head is None:
            return -1
        popped = self.head.data     # Get head data
        self.head = self.head.next  # Move head to next node
        return popped

stack = MyStack()   
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())

