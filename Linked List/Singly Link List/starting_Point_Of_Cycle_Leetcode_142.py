# Starting Point Of a Cycle
# Leetcode 142

'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
'''

# Brute Force solution    TC -> o(n)     SC -> o(n)
# Intuition :- Store the Node of the list not the value and find if the address of the same node is same if yes return that value
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


def StartingCycle(head, pos):
    temp = head
    my_set = set()
    while temp is not None:
        if temp in my_set:
            return temp.val
        my_set.add(temp)
        temp = temp.next
    return temp


# Example usage
arr = [3, 2, 0, -4]
pos = 1
head = create_linked_list(arr, pos)

print(StartingCycle(head, pos))  # Output: True


# Optimal Solution               TC -> o(N)          SC ->o(1)
def startingcycle(head,pos):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.val
        return None

# Example usage
arr = [3, 2, 0, -4,5,9]
pos = 2
head = create_linked_list(arr, pos)

print(startingcycle(head,pos))