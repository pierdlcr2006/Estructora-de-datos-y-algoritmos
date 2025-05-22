class Node:
    """Node for expression tree"""
    def __init__(self, value):
        # Initialize the node with a value (operand or operator)
        self.value = value
        # Left child of the node
        self.left = None
        # Right child of the node
        self.right = None

def evaluate_expression_tree(root):
    """Evaluate an expression tree and return the result"""
    
    # If the tree is empty, return 0
    if root is None:
        return 0

    # If the node is a leaf (operand), return its integer value
    if root.left is None and root.right is None:
        return int(root.value)

    # Recursively evaluate the left subtree
    left_val = evaluate_expression_tree(root.left)
    
    # Recursively evaluate the right subtree
    right_val = evaluate_expression_tree(root.right)

    # Apply the operator stored in the current node
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val // right_val  # Perform integer division

# ✅ Test cases

# Test 1: Simple addition
# Tree:    +
#         / \
#        2   3
# Result: 5
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(evaluate_expression_tree(node1) == 5)  # ➕ Basic addition

# Test 2: Multiplication
# Tree:    *
#         / \
#        4   5
# Result: 20
node2 = Node('*')
node2.left = Node('4')
node2.right = Node('5')
print(evaluate_expression_tree(node2) == 20)  # ✖️ Multiplication

# Test 3: Combined operations
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
# Result: 14
node3 = Node('+')
node3.left = Node('2')
node3.right = Node('*')
node3.right.left = Node('3')
node3.right.right = Node('4')
print(evaluate_expression_tree(node3) == 14)  # 🔢 Combined operations

# Test 4: Division
# Tree:    /
#         / \
#        8   4
# Result: 2
node4 = Node('/')
node4.left = Node('8')
node4.right = Node('4')
print(evaluate_expression_tree(node4) == 2)  # ➗ Division

# Test 5: Complex tree
# Tree:      *
#          /   \
#         +     -
#        / \   / \
#       1   2 8   3
# Result: 15
node5 = Node('*')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('1')
node5.left.right = Node('2')
node5.right.left = Node('8')
node5.right.right = Node('3')
print(evaluate_expression_tree(node5) == 15)  # 🧮 Complex calculation