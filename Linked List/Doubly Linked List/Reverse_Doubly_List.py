# Reverse a Doubly Linked List
# GeekforGeeks Problem 
'''
You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.
Examples:

Input: head = 3 <-> 4 <-> 5
Output: 5 <-> 4 <-> 3

Input: head = 75 <-> 122 <-> 59 <-> 196
Output: 196 <-> 59 <-> 122 <-> 75
'''

# Brute Force Solution   TC -> o(2N)   SC -> o(N)
# Same as Singly Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev


    # Optimal Solution     TC -> o(N)       SC -> o(1)

    def optimal(self,head):
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        while curr is not None:
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = front
        return prev

def reverselist(head):
    temp = head
    stack = []
    while temp is not None:
        stack.append(temp.val)
        temp = temp.next
    temp = head
    while temp is not None:
        e = stack.pop()
        temp.val = e
        temp = temp.next
    return head



def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

sll = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# reversed_head = sll.reverseList(head)
reverse = sll.optimal(head)
# print_linked_list(reversed_head)
print_linked_list(reverse)
