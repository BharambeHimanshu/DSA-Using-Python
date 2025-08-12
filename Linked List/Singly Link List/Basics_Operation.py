class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class SinglyLinkList:
    def __init__(self):
        self.head = None
# Append Operation  TC -> o(N)  SC -> o(1)
# Case 1 :- SLL Can be empty (Assign new node as a head node)
    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
# Case 2 :- SLL is not empty (Assign a variable which traverse from head node to until it get None and once it get None assign the new_node)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
# Traversal Operation  TC -> o(N)     SC -> o(1)
    def traverse(self):
        if self.head is None:
            print("SLL is Empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end= " ")
                curr = curr.next
                print()
sll = SinglyLinkList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()
