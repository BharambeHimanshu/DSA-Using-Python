# Using Recursive Approach
# TC -> O(n)   SC -> O(H)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, node):
        if node == None:
            return 0
        leftheight = self.solve(node.left)
        rightheight = self.solve(node.right)
        return 1 + max(leftheight, rightheight)

    def maxDepth(self, root):
        return self.solve(root)


# Example usage:
if __name__ == "__main__":
    # Build a simple binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    print("Maximum Depth:", solution.maxDepth(root))


# Using Iterative Approach       TC -> o(n)  SC -> o(n)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        # If the tree is empty, its height is 0
        if not root:
            return 0

        queue = deque([root])
        height = 0

        # Process level by level
        while queue:
            level_size = len(queue)
            height += 1  # we’re about to process one more level

            # Dequeue all nodes in the current level, enqueue their children
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return height


# Example usage:
if __name__ == "__main__":
    # Build a sample binary tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    print("Maximum Depth:", solution.maxDepth(root)) 

