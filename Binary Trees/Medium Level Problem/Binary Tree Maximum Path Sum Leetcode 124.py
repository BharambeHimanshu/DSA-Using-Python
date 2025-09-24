'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the node.
The path sum of a path is the sum of the node's values in the path.
Given the node of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: node = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: node = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxi = float("-inf")

    def findMaxPathSum(self, node):
        if node == None:
            return 0

        # Recursively get max path sums from left and right children
        leftPathSum = self.findMaxPathSum(node.left)
        rightPathSum = self.findMaxPathSum(node.right)

        # If a path contributes negatively, ignore it
        if leftPathSum < 0:
            leftPathSum = 0
        if rightPathSum < 0:
            rightPathSum = 0

        # Update global maximum: best path that passes through this node
        self.maxi = max(self.maxi, leftPathSum + node.val + rightPathSum)

        # Return best single-branch path sum to parent
        return max(leftPathSum, rightPathSum) + node.val

    def maxPathSum(self, node):
        self.findMaxPathSum(node)
        return self.maxi

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
print(sol.maxPathSum(node))