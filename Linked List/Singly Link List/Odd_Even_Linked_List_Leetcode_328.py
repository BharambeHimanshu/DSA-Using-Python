# Odd Even in Linked List    [Put all odd first then even]
# Leetcode 328

'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''

# Brute Force    TC ->o(n)    SC ->o(n)
# Approch :- Create Empty List -> Put all the Odd value -> Then Even Value -> Run index (i) in list -> replace head with list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for v in arr[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def oddeven(head):
    if not head or not head.next:
        return head

    value = []

    # Collect odd nodes
    temp = head
    while temp:
        value.append(temp.val)
        if temp.next:
            temp = temp.next.next
        else:
            break

    # Collect even nodes
    temp = head.next
    while temp:
        value.append(temp.val)
        if temp.next:
            temp = temp.next.next
        else:
            break

    # Rewrite values into the linked list
    temp = head
    index = 0
    while temp:
        temp.val = value[index]
        index += 1
        temp = temp.next

    return head

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

head = create_linked_list([1, 2, 3, 4, 5])
new_head = oddeven(head)
print(print_list(new_head))


# Optimal Solution   TC -> o(n/2)   SC -> o(1)
# Approach :- create two linked list -> one for odd -> one for even -> attach odd with even

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddevens(head):
    if not head or not head.next:   # if list has 0 or 1 node
        return head

    odd = head              # odd pointer starts at head
    even = head.next        # even pointer starts at second node
    even_head = even        # keep start of even list (to attach later)

    # Traverse until we reach the end of even list
    while even and even.next:
        odd.next = odd.next.next   # link odd -> next odd
        odd = odd.next

        even.next = even.next.next # link even -> next even
        even = even.next

    odd.next = even_head    # attach even list after odd list
    return head

# Helper function: convert Python list to Linked List
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function: convert Linked List to Python list (for printing)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Example usage
head = create_linked_list([2,1,3,5,6,4,7])
new_head = oddevens(head)
print(linked_list_to_list(new_head))   # Output: [2,3,6,7,1,5,4] (depends on input arrangement)
