# Find the middle of a linked list
# Leetcode 876

'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

# Brute Force Solution    TC -> o(N+N/2)   SC -> o(1)

# Node structure
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def middle(self):
        # Step 1: Count total nodes
        n = 0
        temp = self.head
        while temp:
            n += 1
            temp = temp.next

        # Step 2: Traverse to middle
        temp = self.head
        for _ in range(n // 2):
            temp = temp.next
        return temp.val

# -------------------
# Build linked list from [1, 2, 3, 4, 5]
# -------------------
ll = LinkedList()
for num in [1, 2, 3, 4, 5]:
    ll.append(num)
print("Middle element:", ll.middle())


# Optimal Solution        TC -> o(N/2)   SC -> o(1)


# Node structure
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Linked list
class LinkList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def Middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val  # returning value instead of node

# Create linked list
ll = LinkList()
for i in [1, 2, 3, 4, 5, 6]:
    ll.append(i)

print("Middle element:", ll.Middle())


