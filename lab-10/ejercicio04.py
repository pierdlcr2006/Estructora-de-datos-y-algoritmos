class Node:
    def __init__(self, value):
        # Initialize a new node with a given value
        self.value = value
        # Set left child to None initially
        self.left = None
        # Set right child to None initially
        self.right = None

def inorder_traversal(node):
    # If the current node is None, return an empty list (base case)
    if node is None:
        return []
    # Recursively traverse the left subtree, then visit the current node,
    # then recursively traverse the right subtree and combine the results
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)

def preorder_traversal(node):
    # If the current node is None, return an empty list (base case)
    if node is None:
        return []
    # Visit the current node first, then recursively traverse the left subtree,
    # then recursively traverse the right subtree and combine the results
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)

def postorder_traversal(node):
    # If the current node is None, return an empty list (base case)
    if node is None:
        return []
    # Recursively traverse the left subtree, then the right subtree,
    # and finally visit the current node, combining the results
    return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value]

# ====== Test cases to verify the traversal functions ======

# Test 1: Simple expression tree
node1 = Node('+')              # Create root node with value '+'
node1.left = Node('2')         # Left child with value '2'
node1.right = Node('3')        # Right child with value '3'
print(inorder_traversal(node1) == ['2', '+', '3'])      # Inorder should be left-root-right
print(preorder_traversal(node1) == ['+', '2', '3'])     # Preorder should be root-left-right
print(postorder_traversal(node1) == ['2', '3', '+'])    # Postorder should be left-right-root

# Test 2: More complex tree with nested subtree
node2 = Node('+')              # Root node '+'
node2.left = Node('*')         # Left child '*'
node2.right = Node('5')        # Right child '5'
node2.left.left = Node('2')    # Left child of '*' is '2'
node2.left.right = Node('3')   # Right child of '*' is '3'
print(inorder_traversal(node2) == ['2', '*', '3', '+', '5'])   # Inorder left-root-right with nested subtree
print(preorder_traversal(node2) == ['+', '*', '2', '3', '5'])  # Preorder root-left-right
print(postorder_traversal(node2) == ['2', '3', '*', '5', '+']) # Postorder left-right-root

# Test 3: Single node tree (no children)
node3 = Node('X')              # Single node 'X'
print(inorder_traversal(node3) == ['X'])           # Inorder just the node itself
print(preorder_traversal(node3) == ['X'])          # Preorder just the node itself
print(postorder_traversal(node3) == ['X'])         # Postorder just the node itself

# Test 4: Empty tree case (root is None)
print(inorder_traversal(None) == [])               # Should return empty list for inorder
print(preorder_traversal(None) == [])               # Should return empty list for preorder
print(postorder_traversal(None) == [])              # Should return empty list for postorder