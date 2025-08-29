# Remove Duplicates From Sorted DLL
# GeekForGeeks

'''
Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.

Example 1:
Input:
n = 6
1<->1<->1<->2<->3<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of node with value 1 is 
retained, rest nodes with value = 1 are deleted.

Example 2:
Input:
n = 7
1<->2<->2<->3<->3<->4<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of nodes with values 2,3 and 4 are 
retained, rest repeating nodes are deleted.
'''
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    #Function to remove duplicates from sorted doubly linked list.
    def removeDuplicates(self, head):
        cur = head  # Current node pointer for traversal
        
        while cur:
            # Check if current node is duplicate of previous node
            if cur.prev and cur.prev.val == cur.val:
                # Handle case where previous node is the head
                if cur.prev == head:
                    cur.prev = None        # Remove backward link
                    head = cur            # Update head to current node
                else:
                    # Remove the previous duplicate node by updating links
                    cur.prev.prev.next = cur     # Connect prev's prev to current
                    cur.prev = cur.prev.prev     # Connect current to prev's prev
            
            cur = cur.next  # Move to next node
        
        return head

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(3)

n1.next, n2.prev = n2, n1
n2.next, n3.prev = n3, n2
n3.next, n4.prev = n4, n3
n4.next, n5.prev = n5, n4

dll = Solution()
head = dll.removeDuplicates(n1)

# Print list
cur = head
while cur:
    print(cur.val, end=" ")
    cur = cur.next
