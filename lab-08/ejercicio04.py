# -------------------------
# Definition of binary tree node
# -------------------------
class TreeNode:
    # Constructor for the node, receives a value
    def __init__(self, value):
        self.value = value      # Stores the node's value
        self.left = None        # Initializes the left child as None
        self.right = None       # Initializes the right child as None
# -------------------------
# Binary Tree definition with level-order builder
# -------------------------
class BinaryTree:
    # Constructor for the binary tree
    def __init__(self):
        self.root = None        # Initializes the root as empty

    # Method to build the binary tree from a list (level-order)
    def build_tree_from_list(self, values):
        if not values:
            return              # If the list is empty, nothing to build

        self.root = TreeNode(values[0])  # Create the root node
        queue = [self.root]              # Queue to build tree level by level
        i = 1                            # Index for the values list

        # Traverse the list while there are values and nodes in the queue
        while queue and i < len(values):
            current = queue.pop(0)       # Get the current node from the queue

            # Add left child if available
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            # Add right child if available
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
# -------------------------
# Vertical Order Traversal Function
# -------------------------

def vertical_order_traversal(root):
    if not root:
        return []  # Return empty list if tree is empty

    column_table = {}            # Dictionary to group nodes by horizontal distance (HD)
    queue = [(root, 0)]          # Queue for BFS traversal (node, HD)

    while queue:
        node, hd = queue.pop(0)  # Dequeue node and its HD

        if hd not in column_table:
            column_table[hd] = []  # Initialize list if HD not seen before
        column_table[hd].append(node.value)  # Append node value under the corresponding HD

        # Enqueue left child with HD - 1
        if node.left:
            queue.append((node.left, hd - 1))

        # Enqueue right child with HD + 1
        if node.right:
            queue.append((node.right, hd + 1))

    result = []  # Final result list
    # Sort keys and build the output list in order
    for key in sorted(column_table):
        result.append(column_table[key])
    return result  # Return the vertical traversal result

# -------------------------
# Test Cases for Verification
# -------------------------

def test_vertical_order_traversal():
    print("Running vertical_order_traversal tests...\n")

    # Test Case 1: Regular binary tree
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    result1 = vertical_order_traversal(tree1.root)
    print("Test Case 1:", result1)  # Expected: [[4], [2], [1, 5], [3], [6]]

    # Test Case 2: Left-skewed vertical tree
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, None, 3])
    result2 = vertical_order_traversal(tree2.root)
    print("Test Case 2:", result2)  # Expected: [[3], [2], [1]]

    # Test Case 3: Empty tree
    tree3 = BinaryTree()
    result3 = vertical_order_traversal(tree3.root)
    print("Test Case 3:", result3)  # Expected: []

    # Test Case 4: Single node tree
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1])
    result4 = vertical_order_traversal(tree4.root)
    print("Test Case 4:", result4)  # Expected: [[1]]

    # Test Case 5: Complete binary tree
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    result5 = vertical_order_traversal(tree5.root)
    print("Test Case 5:", result5)  # Expected: [[4], [2], [1, 5, 6], [3], [7]]

# -------------------------
# Run all test cases
# -------------------------

test_vertical_order_traversal()