'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0  # holds the maximum diameter found

    def calculateHeight(self, root):
        # Base case: empty tree has height 0
        if root == None:
            return 0
        # Recursively find heights of left and right subtrees
        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)

        # Update diameter: path through root uses leftHeight + rightHeight edges
        self.diameter = max(self.diameter, leftHeight + rightHeight)

        # Return the height of this subtree (in nodes)
        return 1 + max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root):
        # Initialize diameter and start recursion
        self.diameter = 0
        self.calculateHeight(root)
        return self.diameter

# Build the tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Run solution
sol = Solution()
print(sol.diameterOfBinaryTree(root))
