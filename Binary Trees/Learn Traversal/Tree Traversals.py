class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class DFSBinaryTree:
    # Preorder Traversal [Root - Left - Right]
    def preorder(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    # Inorder Traversal [Left - Root - Right]
    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    # Postorder Traversal [Left - Right - Root]
    def postorder(self, root, res):
        if not root:
            return
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)


# Build the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Traversals
traversals = DFSBinaryTree()
pre, ino, post = [], [], []
traversals.preorder(root, pre)
traversals.inorder(root, ino)
traversals.postorder(root, post)

print("Preorder =", pre)  
print("Inorder =", ino)  
print("Postorder =", post) 
