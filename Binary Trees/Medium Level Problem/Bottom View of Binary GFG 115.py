
#Input: 
#     20
#     /  \
#    8   22
#   / \     \
#  5   3     25
#     / \
#    10  14

#Output: [5, 10, 3, 14, 25]
#Explanation: 
#From the bottom, nodes 5, 10, 3, 14, and 25 are visible.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def topview(self, node):
        if node == None:
            return None
        ans = []
        queue = deque()
        # dictionary to store first node for each horizontal distance
        result = {}
        # queue for BFS -> stores (node, line)
        queue.append((node, 0))
        while queue:
            e, line = queue.popleft()
            result[line] = e.val
            # add left and right children with updated line
            if e.left:
                queue.append((e.left, line - 1))
            if e.right:
                queue.append((e.right, line + 1))
        # extract results sorted by line
        for value in sorted(result.items()):
            ans.append(value[1])
        return ans


# Example binary tree
#        1
#       / \
#      2   3
#       \   \
#        4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

sol = Solution()
print(sol.topview(root))
