# Linked List Cycle
# Leetcode 141

'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

# Brute Force solution    TC -> o(n)     SC -> o(n)
# Intuition :- Store the Node of the list not the value and find if the address of the same node is same if yes return true
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr, pos):
    """Creates linked list from arr. 
       If pos != -1, creates a cycle at that index."""
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head
    nodes = [head]

    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)

    if pos != -1:
        curr.next = nodes[pos]  # create cycle

    return head


def ListCycle(head, pos):
    temp = head
    my_set = set()
    while temp is not None:
        if temp in my_set:
            return True
        my_set.add(temp)
        temp = temp.next
    return False


# Example usage
arr = [3, 2, 0, -4]
pos = 1
head = create_linked_list(arr, pos)

print(ListCycle(head, pos))  # Output: True


# Optimal Solution   TC-> O(n)   SC-> o(1)
# Intuition ;- Take a slow and fast Pointer and if this two pointer meets means it is a loop

def Listcycle(head,pos):
    slow = head 
    fast = head 
    while fast is not None and fast.next is not None: 
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast: 
            return True 
    return False

print(Listcycle(head,pos))

