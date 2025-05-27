# 🔧 Clase base y utilidades de árbol
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inserta respetando reglas de BST
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

# Crea un BST válido desde lista
def build_tree(values):
    root = None
    for val in values:
        root = insert_bst(root, val)
    return root

# 🚫 Crea árbol inválido - violación en izquierda
def build_invalid_tree1():
    root = TreeNode(5)
    root.left = TreeNode(6)  # Violación: 6 > 5
    root.right = TreeNode(7)
    return root

# 🚫 Crea árbol inválido - violación en derecha
def build_invalid_tree2():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(4)  # Violación: 4 < 5
    return root

# ✅ Función principal: validar BST usando min/max
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

# ✅ Test cases
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)   # ✅ Valid BST
print(is_valid_bst(build_invalid_tree1()) == False)             # ❌ Left violation
print(is_valid_bst(build_invalid_tree2()) == False)             # ❌ Right violation
print(is_valid_bst(build_tree([42])) == True)                   # 🌱 Single node
print(is_valid_bst(None) == True)                               # 📭 Empty tree
