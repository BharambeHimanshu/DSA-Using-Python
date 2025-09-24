'''
Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self,node):
        if node == None:
            return 0
        LH = self.solve(node.left)
        if LH == -1:
            return -1
        RH = self.solve(node.right)
        if RH == -1:
            return -1
        if abs(LH - RH) > 1:
            return -1
        return 1 + max(LH,RH)
    def isBalanced(self, node):
        x = self.solve(node)
        if x == -1:
            return False
        return True

# Build the tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)

# Run solution
sol = Solution()
print(sol.isBalanced(node))