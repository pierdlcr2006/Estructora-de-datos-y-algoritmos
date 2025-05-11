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
# Binary Search Tree (BST) definition
# -------------------------
class BinarySearchTree:
    # Constructor for the binary search tree
    def __init__(self):
        self.root = None  # Initializes the root as empty

    # Method to insert a value into the BST
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)  # If the tree is empty, set the root
        else:
            self._insert_recursive(self.root, value)  # Insert recursively

    # Recursive helper method for insertion
    def _insert_recursive(self, node, value):
        if value < node.value:  # If the value is smaller, insert it in the left subtree
            if node.left is None:
                node.left = TreeNode(value)  # Insert the node to the left
            else:
                self._insert_recursive(node.left, value)  # Continue recursively
        else:  # If the value is larger or equal, insert it in the right subtree
            if node.right is None:
                node.right = TreeNode(value)  # Insert the node to the right
            else:
                self._insert_recursive(node.right, value)  # Continue recursively

    # Method to perform inorder traversal and return the values in ascending order
    def inorder_traversal(self):
        result = []  # List to store the traversal results
        self._inorder_recursive(self.root, result)  # Perform recursive traversal
        return result  # Return the list of values in inorder

    # Recursive helper method for inorder traversal
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)  # Traverse the left subtree
            result.append(node.value)  # Add the current node’s value to the list
            self._inorder_recursive(node.right, result)  # Traverse the right subtree

# -------------------------
# Function to build a balanced BST from a sorted list
# -------------------------
def build_balanced_bst(values):
    if not values:  # If the list is empty, return None
        return None
    mid = len(values) // 2  # Find the middle element to be the root
    node = TreeNode(values[mid])  # Create a new node for the middle value
    node.left = build_balanced_bst(values[:mid])  # Recursively build the left subtree
    node.right = build_balanced_bst(values[mid+1:])  # Recursively build the right subtree
    return node  # Return the node representing the root of the balanced subtree

# -------------------------
# Function to balance the given BST
# -------------------------
def balance_bst(bst):
    sorted_values = bst.inorder_traversal()  # Step 1: Get sorted values from the BST
    balanced_tree = BinarySearchTree()  # Step 2: Create an empty binary search tree
    balanced_tree.root = build_balanced_bst(sorted_values)  # Step 3: Build the balanced BST
    return balanced_tree  # Return the newly balanced tree


# -------------------------
# Test Cases for verifying the balance_bst function
# -------------------------
def test_balance_bst():
    print("Running balance_bst tests...\n")

    # Test Case 1: Already balanced tree
    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)  # Insert values to form a balanced tree
    balanced1 = balance_bst(bst1)  # Balance the tree
    print("Test Case 1:", balanced1.inorder_traversal())  # Expected: [1, 2, 3, 4, 5, 6, 7]

    # Test Case 2: Right-skewed tree
    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)  # Insert values to form a right-skewed tree
    balanced2 = balance_bst(bst2)  # Balance the tree
    print("Test Case 2:", balanced2.inorder_traversal())  # Expected: [1, 2, 3, 4, 5]

    # Test Case 3: Left-skewed tree
    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)  # Insert values to form a left-skewed tree
    balanced3 = balance_bst(bst3)  # Balance the tree
    print("Test Case 3:", balanced3.inorder_traversal())  # Expected: [1, 2, 3, 4, 5]

    # Test Case 4: Empty tree
    bst4 = BinarySearchTree()  # Create an empty tree
    balanced4 = balance_bst(bst4)  # Balance the tree
    print("Test Case 4:", balanced4.inorder_traversal())  # Expected: []

    # Test Case 5: Single node tree
    bst5 = BinarySearchTree()
    bst5.insert(42)  # Insert a single value
    balanced5 = balance_bst(bst5)  # Balance the tree
    print("Test Case 5:", balanced5.inorder_traversal())  # Expected: [42]

# -------------------------
# Run all test cases
# -------------------------
test_balance_bst()  # Run all the test cases to verify the balance_bst function