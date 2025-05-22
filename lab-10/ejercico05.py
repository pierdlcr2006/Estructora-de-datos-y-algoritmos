class Node:
    def __init__(self, value):
        self.value = value      # Store the value of the node (operator or operand)
        self.left = None        # Left child initialized as None
        self.right = None       # Right child initialized as None

def is_number(s):
    try:
        float(s)               # Try to convert the string to a float
        return True           # If successful, it is a number
    except:
        return False          # Otherwise, it is not a number

def compute(op, a, b):
    a, b = float(a), float(b)  # Convert both operands to float for calculation
    if op == '+':
        return str(int(a + b))  # Return sum as string (int cast to avoid decimals)
    elif op == '-':
        return str(int(a - b))  # Return difference as string
    elif op == '*':
        return str(int(a * b))  # Return product as string
    elif op == '/':
        return str(int(a / b))  # Return division result as string (integer division)
    return None                 # Return None if operator is unknown

def simplify_expression_tree(root):
    def helper(node):
        if node is None:
            return None          # Base case: if node is None, return None

        # Recursively simplify left and right subtrees first (post-order traversal)
        node.left = helper(node.left)
        node.right = helper(node.right)

        # If both children exist and are numeric, compute the result and replace subtree
        if node.left and node.right:
            if is_number(node.left.value) and is_number(node.right.value):
                return Node(compute(node.value, node.left.value, node.right.value))

        # If no simplification possible, return the current node as is
        return node

    # If root and its children are numeric, simplify entire root directly
    if root and root.left and root.right:
        if is_number(root.left.value) and is_number(root.right.value):
            return Node(compute(root.value, root.left.value, root.right.value))

    # Otherwise simplify subtrees recursively
    root.left = helper(root.left)
    root.right = helper(root.right)
    return root

# ✅ Test cases
# Test 1
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
result1 = simplify_expression_tree(node1)
print(result1.value == '5' and result1.left is None and result1.right is None)

# Test 2
node2 = Node('+')
node2.left = Node('x')
node2.right = Node('3')
result2 = simplify_expression_tree(node2)
print(result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3')

# Test 3
node3 = Node('+')
node3.left = Node('*')
node3.right = Node('-')
node3.left.left = Node('2')
node3.left.right = Node('3')
node3.right.left = Node('8')
node3.right.right = Node('3')
result3 = simplify_expression_tree(node3)
print(result3.value == '+' and result3.left.value == '6' and result3.right.value == '5')

# Test 4
node4 = Node('+')
node4.left = Node('x')
node4.right = Node('y')
result4 = simplify_expression_tree(node4)
print(result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y')

# Test 5 (corrigiendo construcción)
node5 = Node('+')
node5.left = Node('/')
node5.right = Node('*')
node5.left.left = Node('10')
node5.left.right = Node('2')
node5.right.left = Node('z')
node5.right.right = Node('4')
result5 = simplify_expression_tree(node5)
print(result5.value == '+' and result5.left.value == '5' and 
      result5.right.value == '*' and result5.right.left.value == 'z')