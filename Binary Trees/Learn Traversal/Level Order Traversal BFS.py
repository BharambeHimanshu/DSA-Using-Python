from collections import deque

def level_order_traversal(root):
    """
    Perform a BFS (level-order) traversal on a binary tree and
    return a list of levels, where each level is a list of node values.
    """
    result = []
    if not root:
        return result

    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
