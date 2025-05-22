class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)

def preorder_traversal(node):
    if node is None:
        return []
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)

def postorder_traversal(node):
    if node is None:
        return []
    return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value]

node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(inorder_traversal(node1) == ['2', '+', '3'])
print(preorder_traversal(node1) == ['+', '2', '3'])
print(postorder_traversal(node1) == ['2', '3', '+'])

node2 = Node('+')
node2.left = Node('*')
node2.right = Node('5')
node2.left.left = Node('2')
node2.left.right = Node('3')
print(inorder_traversal(node2) == ['2', '*', '3', '+', '5'])
print(preorder_traversal(node2) == ['+', '*', '2', '3', '5'])
print(postorder_traversal(node2) == ['2', '3', '*', '5', '+'])

node3 = Node('X')
print(inorder_traversal(node3) == ['X'])
print(preorder_traversal(node3) == ['X'])
print(postorder_traversal(node3) == ['X'])

print(inorder_traversal(None) == [])
print(preorder_traversal(None) == [])
print(postorder_traversal(None) == [])