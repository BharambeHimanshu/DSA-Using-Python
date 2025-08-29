# Delete all occurances of a key
# GeekforGeeks Problem 

'''
You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL.

Example1:
Input: 
2<->2<->10<->8<->4<->2<->5<->2
2
Output: 
10<->8<->4<->5
Explanation: 
All Occurences of 2 have been deleted.

Example2:
Input: 
9<->1<->3<->4<->5<->1<->8<->4
9
Output: 
1<->3<->4<->5<->1<->8<->4
Explanation: 
All Occurences of 9 have been deleted.
'''

# Optimal Solution    TC -> o(N)     SC -> o(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, k):
        # Handle special case: single node that matches the key
        if not head.next and head.val == k:
            return None
        
        temp = head          # Pointer to traverse the list
        previous = None      # Pointer to track previous node
        new_head = head      # Keep track of new head
        
        # Traverse through the entire list
        while temp is not None:
            if temp.val == k:  # Found a node to delete
                # Update previous node's next pointer
                if previous:
                    previous.next = temp.next
                
                # Update next node's prev pointer
                if temp.next:
                    temp.next.prev = previous
                
                # Update head if we're deleting the first node
                if temp == new_head:
                    new_head = new_head.next
            
            previous = temp      # Move previous pointer
            temp = temp.next     # Move to next node
        
        return new_head

# Helper Function    
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(4)

sll = Solution()

# Delete all '2's
new_head = sll.deleteAllOccurOfX(head, 2)

# Print result
print_list(new_head) 