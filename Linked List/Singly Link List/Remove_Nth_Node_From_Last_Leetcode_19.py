# Remove Nth Node From Last
# Leetcode 19

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

# Brute Force   TC ->o(2N)       SC -> o(1)
# Approach :- 1) Calculate the lenght
#             2) lenght - n

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    length = 0
    temp = head

    # Step 1: find length of list
    while temp:
        length += 1
        temp = temp.next

    # If head needs to be removed
    if length == n:
        return head.next

    # Step 2: find the node before the one to remove
    temp = head
    for i in range(length - n - 1):
        temp = temp.next

    # Step 3: delete nth node from end
    temp.next = temp.next.next

    return head

# Helper function to create linked list from Python list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print linked list
def printLinkedList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Example usage:
head = createLinkedList([1,2,3,4,5])
n = 2
new_head = removeNthFromEnd(head, n)
print(printLinkedList(new_head))  # Output: [1, 2, 3, 5]


# Optimal Solution   TC -> o(N)     SC -> o(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Optimal Solution  TC -> O(N)   SC -> O(1)
def removeNthFromEnd(head, n):
    fast = head
    slow = head

    # move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # if fast reached None, remove head
    if fast is None:
        return head.next

    # move both until fast reaches last node
    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    # delete nth node from end
    slow.next = slow.next.next

    return head

# Helper function to build linked list from Python list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print linked list as Python list
def printLinkedList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Example usage
head = createLinkedList([1, 2, 3, 4, 5])
n = 2
new_head = removeNthFromEnd(head, n)
print(printLinkedList(new_head))   # Output: [1, 2, 3, 5]
