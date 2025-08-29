# Find Pairs with given Sum in DLL
# GeekforGeeks Problem

'''
Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.

 

Example 1:

Input:  
1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
target = 7
Output: (1, 6), (2,5)
Explanation: We can see that there are two pairs 
(1, 6) and (2,5) with sum 7.
 

Example 2:

Input: 
1 <-> 5 <-> 6
target = 6
Output: (1,5)
Explanation: We can see that there is one pairs (1,5) with sum 6.
'''

# Brute Force   TC ->o(N^2)         SC -> o(1)
# Approach -> Take two Variable temp1 and temp2

def find(input,target):
    temp1 = head
    result = []
    while temp1 is not None:
        temp2 = temp1.next
        while temp2 is not None:
            if temp1.val + temp2.val == target:
                result.append([temp1.val,temp2.val])
            temp2 = temp1.next
        return result


# Better Solution       TC -> o(N)      SC -> o(N)
# Using Sets and remaining = target - temp.val

def better(input,target):
    my_set = set()
    temp = head
    result = []
    while temp is not None:
        remaining = target - temp.val
        if remaining in my_set:
            result.append([remaining,temp.val])
        my_set.add(temp.val)
        temp = temp.next
    return result


# Optimal Solution         TC -> o(N)       SC -> o(1)
# Approach :- Use two pointer Left and Right
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def findPairsWithGivenSum(self,head,target):
        left = head          # Left pointer starts at head (smallest element)
        right = head         # Right pointer will move to tail (largest element)
        ans = []            # List to store all valid pairs
        
        # Move right pointer to the end of the list
        while right.next is not None:
            right = right.next
        
        # Use two pointers to find pairs
        while left is not None and right is not None and left.val < right.val:
            total = left.val + right.val  # Calculate sum of current pair
            
            if total == target:
                # Found a valid pair, add to results
                ans.append([left.val, right.val])
                left = left.next     # Move left pointer forward
                right = right.prev   # Move right pointer backward
            elif total > target:
                # Sum is too large, move right pointer to smaller element
                right = right.prev
            else:
                # Sum is too small, move left pointer to larger element
                left = left.next
        return ans

# Build a Linked List
head = ListNode(1)
head.next = ListNode(2, None, head)
head.next.next = ListNode(3, None, head.next)
head.next.next.next = ListNode(4, None, head.next.next)
head.next.next.next.next = ListNode(5, None, head.next.next.next)

dll = Solution()

result = dll.findPairsWithGivenSum(head,6)
print(result)

        
