# 🔧 Definición de clase y utilidades de BST
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def build_bst(values):
    root = None
    for val in values:
        root = insert_bst(root, val)
    return root

# 🌲 Función principal: encontrar Lowest Common Ancestor (LCA)
def find_lca(root, val1, val2):
    """Find lowest common ancestor of two values in BST"""
    current = root
    while current:
        if val1 < current.val and val2 < current.val:
            current = current.left  # Ir a la izquierda 👈
        elif val1 > current.val and val2 > current.val:
            current = current.right  # Ir a la derecha 👉
        else:
            return current.val  # Encontrado 🎯
    return None  # Seguridad

# ✅ Test cases
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)  # 🌲 Root as LCA
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 0, 4) == 2)  # 📊 Subtree LCA
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 3) == 2)  # 🔗 Ancestor relationship
print(find_lca(build_bst([5, 3, 7]), 5, 5) == 5)                    # 🎯 Same node
print(find_lca(build_bst([4, 2, 6, 1, 3, 5, 7]), 1, 3) == 2)        # 🌱 Leaf nodes
