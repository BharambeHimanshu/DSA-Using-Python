# How to create Node

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class doublylinkedlist:
    def __init__(self):
        self.head = None
# Insert At Head

    def insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    print()


# Append [Add At Last]

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:        # Find the last node
                current = current.next
            current.next = new_node    # Connect last node to new node
            new_node.prev = current    # Connect new node back to last node


# Insert At Position
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
    
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
    
        if current is None:
            print("Position out of bounds")
            return
    
        new_node.next = current.next    # Connect new node to next node
        new_node.prev = current         # Connect new node to current node
        if current.next:
            current.next.prev = new_node  # Update next node's prev pointer
        current.next = new_node         # Connect current node to new node


# Traversal Operation
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next    # Move forward
    print()

    def traverse_backward(self):
        current = self.head
        while current.next:        # Go to the last node
            current = current.next
        while current:
            print(current.val, end=" ")
            current = current.prev  # Move backward
        print()
dll = doublylinkedlist()
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_head(30)
dll.insert_at_head(40)
dll.append(100)
dll.insert_at(40,2)
dll.traverse_forward()