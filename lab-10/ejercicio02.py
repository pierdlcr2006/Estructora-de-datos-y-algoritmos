class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(postfix):
    stack = []

    for token in postfix:
        if token not in "+-*/":
            stack.append(Node(token))
        else:
            right = stack.pop()
            left = stack.pop()
            
            operator_node = Node(token)
            
            operator_node.left = left
            operator_node.right = right
            
            stack.append(operator_node)
            
    return stack[0] if stack else None

tokens1 = ['2', '3', '+']
tree1 = build_expression_tree(tokens1)
print(tree1.value == '+' and tree1.left.value == '2' and tree1.right.value == '3')

tokens2 = ['2', '3', '4', '*', '+']
tree2 = build_expression_tree(tokens2)
print(tree2.value == '+' and tree2.left.value == '2' and tree2.right.value == '*')

tokens3 = ['1', '2', '+', '3', '4', '-', '*']
tree3 = build_expression_tree(tokens3)
print(tree3.value == '*' and tree3.left.value == '+' and tree3.right.value == '-')

tokens4 = ['a', 'b', 'c', '*', '+']
tree4 = build_expression_tree(tokens4)
print(tree4.value == '+' and tree4.left.value == 'a' and tree4.right.value == '*')

tokens5 = ['a', 'b', '+', 'c', 'd', '-', '/']
tree5 = build_expression_tree(tokens5)
print(tree5.value == '/' and tree5.left.value == '+' and tree5.right.value == '-')