# ✅ Clase TreeNode
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ✅ Función para insertar un valor en el BST
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

# ✅ Función para construir un BST desde una lista
def build_bst(values):
    root = None
    for val in values:
        root = insert_bst(root, val)
    return root

# ✅ Función principal: buscar valores en rango dentro del BST
def range_query(root, min_val, max_val):
    result = []

    def dfs(node):
        if not node:
            return
        if node.val > min_val:
            dfs(node.left)
        if min_val <= node.val <= max_val:
            result.append(node.val)
        if node.val < max_val:
            dfs(node.right)

    dfs(root)
    return result

# ✅ Test cases
print(range_query(build_bst([7, 3, 11, 1, 5, 9, 13]), 5, 10) == [5, 7, 9])          # 🎯 Normal range
print(range_query(build_bst([6, 4, 8, 2]), 1, 10) == [2, 4, 6, 8])                  # 📊 Full coverage
print(range_query(build_bst([20, 10, 30]), 1, 5) == [])                             # 📭 Empty result
print(range_query(build_bst([15]), 10, 20) == [15])                                # 🌱 Single node
print(range_query(build_bst([15, 10, 20, 5, 25]), 10, 20) == [10, 15, 20])          # 🔗 Include boundaries
