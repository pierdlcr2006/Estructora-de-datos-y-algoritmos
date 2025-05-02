class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(node):
    def check_height(current):
        if current is None:
            return 0
        
        left_height = check_height(current.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(current.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1

    return check_height(node) != -1

def test_is_balanced():
    # Caso 1: Árbol balanceado
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    print(is_balanced(root1))  # Esperado: True

    # Caso 2: Árbol desbalanceado (muy cargado a la izquierda)
    #        1
    #       /
    #      2
    #     /
    #    3
    #   /
    #  4
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    print(is_balanced(root2))  # Esperado: False

    # Caso 3: Árbol justo en el límite de desbalance (altura desigual = 2)
    #        1
    #       / \
    #      2   3
    #     /
    #    4
    #   /
    #  5
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.left.left = TreeNode(5)
    print(is_balanced(root3))  # Expected output: False

test_is_balanced()