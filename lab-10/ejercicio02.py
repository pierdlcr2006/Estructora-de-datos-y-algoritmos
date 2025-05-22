class Node:
    """Node for expression tree"""
    def __init__(self, value):
        # Initialize the node with a value (either operand or operator)
        self.value = value
        # Pointer to the left child of the node
        self.left = None
        # Pointer to the right child of the node
        self.right = None

def build_expression_tree(postfix):
    """Build expression tree from postfix notation"""
    
    # Stack to keep track of nodes while building the tree
    stack = []

    # Loop through each token in the postfix expression
    for token in postfix:
        # If the token is an operand (not an operator)
        if token not in "+-*/":
            # Create a new leaf node for the operand and push to stack
            stack.append(Node(token))
        else:
            # Token is an operator: pop two nodes from the stack
            right = stack.pop()  # Right child (popped last)
            left = stack.pop()   # Left child (popped before right)
            
            # Create a new node with the operator
            operator_node = Node(token)
            
            # Set the popped nodes as children of the operator
            operator_node.left = left
            operator_node.right = right
            
            # Push the new subtree back onto the stack
            stack.append(operator_node)
            
    # The final element on the stack is the root of the expression tree
    return stack[0] if stack else None
# ✅ Test cases
# Test 1: Simple addition
# Input: 2 3 +
# Tree:    +
#         / \
#        2   3
tokens1 = ['2', '3', '+']
tree1 = build_expression_tree(tokens1)
print(tree1.value == '+' and tree1.left.value == '2' and tree1.right.value == '3')  # 🌱 Simple tree

# Test 2: Complex expression
# Input: 2 3 4 * +
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
tokens2 = ['2', '3', '4', '*', '+']
tree2 = build_expression_tree(tokens2)
print(tree2.value == '+' and tree2.left.value == '2' and tree2.right.value == '*')  # 📊 Operator precedence

# Test 3: Nested operations
# Input: 1 2 + 3 4 - *
# Tree:    *
#         / \
#        +   -
#       / \ / \
#      1  2 3  4
tokens3 = ['1', '2', '+', '3', '4', '-', '*']
tree3 = build_expression_tree(tokens3)
print(tree3.value == '*' and tree3.left.value == '+' and tree3.right.value == '-')  # 🔗 Nested operations

# Test 4: Expression with variables
# Input: a b c * +
# Tree:    +
#         / \
#        a   *
#           / \
#          b   c
tokens4 = ['a', 'b', 'c', '*', '+']
tree4 = build_expression_tree(tokens4)
print(tree4.value == '+' and tree4.left.value == 'a' and tree4.right.value == '*')  # 🔤 Variable tree

# Test 5: More complex expression
# Input: a b + c d - /
# Tree:    /
#         / \
#        +   -
#       / \ / \
#      a  b c  d
tokens5 = ['a', 'b', '+', 'c', 'd', '-', '/']
tree5 = build_expression_tree(tokens5)
print(tree5.value == '/' and tree5.left.value == '+' and tree5.right.value == '-')  # 🧮 Complex tree