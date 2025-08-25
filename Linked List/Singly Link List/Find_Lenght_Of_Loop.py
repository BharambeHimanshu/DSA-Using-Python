# Find Lenght Of Loop

'''
Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.
Note: 'c' is the position of the node which is the next pointer of the last node of the linkedlist. If c is 0, then there is no loop.

Examples:

Input: head: 1 → 2 → 3 → 4 → 5, c = 2
Output: 4
Explanation: There exists a loop in the linked list and the length of the loop is 4.

Input: head: 25 → 14 → 19 → 33 → 10 → 21 → 39 → 90 → 58 → 45, c = 4
Output: 7
Explanation: The loop is from 33 to 45. So length of loop is 33 → 10 → 21 → 39 → 90 → 58 → 45 = 7.

Input: head: 0 → 1 → 2 → 3, c = 0
Output: 0
Explanation: There is no loop.
'''

# Brute Force   TC -> o(N)     SC -> o(N)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr, pos):
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

def Length(head):
    temp = head
    my_dict = dict()
    travel = 0
    while temp is not None:
        if temp in my_dict:
            return travel - my_dict[temp]  # cycle length
        my_dict[temp] = travel
        travel += 1
        temp = temp.next
    return 0

# Example usage
arr = [1, 2, 3, 4, 5]
pos = 2   # cycle starts at index 2 → value = 3
head = create_linked_list(arr, pos)

print(Length(head))  # Output: 3 (length of cycle: 3 → [3 → 4 → 5 → 3])


# Optimal Solution    TC -> o(N)       SC -> o(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr, pos):
    if not arr: return None
    head = ListNode(arr[0])
    cur = head
    nodes = [head]
    for v in arr[1:]:
        cur.next = ListNode(v)
        cur = cur.next
        nodes.append(cur)
    if pos != -1:           # pos is 0-based index of the cycle entry
        cur.next = nodes[pos]
    return head

def cycle_length(head):
    slow = fast = head
    # phase 1: detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # phase 2: measure the cycle
            count = 1
            p = slow.next
            while p != slow:
                count += 1
                p = p.next
            return count
    return 0

arr = [1,2,3,4,5,6,7,8]
pos = 3     
head = create_linked_list(arr, pos)

print(cycle_length(head)) 


