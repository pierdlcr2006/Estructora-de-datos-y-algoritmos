# Definition of the binary tree node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function that performs level order traversal
def level_order_traversal(root):
    """Perform level order traversal of a binary tree without using deque."""
    if root is None:
        return []

    result = []
    queue = [root]  # using a list as a FIFO queue

    while queue:
        node = queue.pop(0)  # remove the first element (FIFO)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def test_level_order_traversal():
    # Test Case 1: Full binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(level_order_traversal(root))  # Expected output: [1, 2, 3, 4, 5, 6, 7]

    # Test Case 2: Tree with only left children
    left_only = TreeNode(1)
    left_only.left = TreeNode(2)
    left_only.left.left = TreeNode(3)
    left_only.left.left.left = TreeNode(4)
    print(level_order_traversal(left_only))  # Expected output: [1, 2, 3, 4]

    # Test Case 3: Tree with only right children
    right_only = TreeNode(1)
    right_only.right = TreeNode(2)
    right_only.right.right = TreeNode(3)
    right_only.right.right.right = TreeNode(4)
    print(level_order_traversal(right_only))  # Expected output: [1, 2, 3, 4]


# Run the tests
test_level_order_traversal()