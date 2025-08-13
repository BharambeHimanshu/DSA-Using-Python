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


# Insert Operation   
    def insert(self,val,position):
        new_node = Node(val)
        # If We want to insert at head node
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        # If We want to insert at specific position
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current


# Delete Operation
    def delete(self,val):
        # If we want to delete at head node
        temp = self.head       # Assign Temp variable to head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False   # If value doesnt exits in list
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node not found")


sll = SinglyLinkList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.insert(100,2)
sll.delete(20)
sll.traverse()

