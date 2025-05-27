# 📦 Clase de nodo y utilidades para construir BST
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

# 🔍 Función principal: K-ésimo elemento más pequeño en BST
def kth_smallest(root, k):
    """Find kth smallest element in BST using inorder traversal"""
    count = 0
    result = None

    def inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.val
            return
        inorder(node.right)

    inorder(root)
    return result

# ✅ Casos de prueba
print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)              # 🎯 Segundo menor
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)     # 📊 Mínimo
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)     # 📈 Máximo
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)     # 🔗 Medio
print(kth_smallest(build_bst([10]), 1) == 10)                    # 🌱 Un solo nodo
