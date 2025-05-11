# Binary Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val            # Store the value of the node
        self.left = None          # Initialize left child to None
        self.right = None         # Initialize right child to None

# Build binary tree from list (level-order)
class BinaryTree:
    def __init__(self):
        self.root = None          # Initialize the root of the binary tree

    def build_tree_from_list(self, values):
        if not values:
            return None           # Return None if the input list is empty

        self.root = TreeNode(values[0])  # First element is the root
        queue = [self.root]              # Use a queue to manage nodes level by level
        i = 1                            # Index to traverse the values list

        while queue and i < len(values):
            current = queue.pop(0)       # Get the next node to assign children

            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])   # Assign left child
                queue.append(current.left)           # Add to queue for future children
            i += 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])  # Assign right child
                queue.append(current.right)          # Add to queue
            i += 1

# Helper to find node by value (DFS search)
def find_node_by_value(root, value):
    if root is None:
        return None                     # Base case: reached a leaf
    if root.val == value:
        return root                    # Found the node with the given value
    left = find_node_by_value(root.left, value)  # Search in left subtree
    return left if left else find_node_by_value(root.right, value)  # If not found, search right

# Lowest Common Ancestor algorithm (recursive)
def lowest_common_ancestor(root, p, q):
    if root is None or root == p or root == q:
        return root                    # If root is None or one of the targets, return it
    left = lowest_common_ancestor(root.left, p, q)    # Search LCA in left subtree
    right = lowest_common_ancestor(root.right, p, q)  # Search LCA in right subtree
    if left and right:
        return root                    # If both sides return a result, current root is LCA
    return left if left else right     # Otherwise, return the non-None result

# Function to run all test cases and print results
def test_lowest_common_ancestor():
    print("🔍 Lowest Common Ancestor Test Results\n")

    # Test 1 - LCA(4, 6) should be 1
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    n4 = find_node_by_value(tree1.root, 4)
    n6 = find_node_by_value(tree1.root, 6)
    lca1 = lowest_common_ancestor(tree1.root, n4, n6)
    print("Test 1 - LCA(4, 6):", lca1.val if lca1 else "None")

    # Test 2 - LCA(2, 4) should be 2
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, 3, 4])
    n2 = find_node_by_value(tree2.root, 2)
    n4 = find_node_by_value(tree2.root, 4)
    lca2 = lowest_common_ancestor(tree2.root, n2, n4)
    print("Test 2 - LCA(2, 4):", lca2.val if lca2 else "None")

    # Test 3 - LCA(2, 3) should be 1
    tree3 = BinaryTree()
    tree3.build_tree_from_list([1, 2, 3])
    n2 = find_node_by_value(tree3.root, 2)
    n3 = find_node_by_value(tree3.root, 3)
    lca3 = lowest_common_ancestor(tree3.root, n2, n3)
    print("Test 3 - LCA(2, 3):", lca3.val if lca3 else "None")

    # Test 4 - LCA(1, 3) should be 1
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    n1 = find_node_by_value(tree4.root, 1)
    n3 = find_node_by_value(tree4.root, 3)
    lca4 = lowest_common_ancestor(tree4.root, n1, n3)
    print("Test 4 - LCA(1, 3):", lca4.val if lca4 else "None")

    # Test 5 - LCA(2, 99), where 99 is not in the tree
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3])
    n2 = find_node_by_value(tree5.root, 2)
    not_in_tree = TreeNode(99)  # Node 99 is created but not inserted
    lca5 = lowest_common_ancestor(tree5.root, n2, not_in_tree)
    print("Test 5 - LCA(2, 99):", lca5.val if lca5 else "None")

# Execute all test cases
test_lowest_common_ancestor()