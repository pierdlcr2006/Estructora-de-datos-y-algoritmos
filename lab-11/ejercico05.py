# 📦 Definición del nodo
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # actúa como prev en DLL
        self.right = None  # actúa como next en DLL

# 🔨 Función para insertar en BST
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

# 🔨 Construcción de un BST completo
def build_bst(values):
    root = None
    for val in values:
        root = insert_bst(root, val)
    return root

# 🔨 Construcción de un BST degenerado (como lista)
def build_degenerate_bst(values):
    root = None
    for val in values:
        node = TreeNode(val)
        if not root:
            root = node
            curr = root
        else:
            curr.right = node
            curr = curr.right
    return root

# 🔄 Conversión BST → Circular DLL ordenada
def bst_to_dll(root):
    """Convert BST to sorted circular doubly linked list"""
    if not root:
        return None

    first = last = None

    def inorder(node):
        nonlocal first, last
        if not node:
            return
        inorder(node.left)
        if last:
            last.right = node  # next
            node.left = last   # prev
        else:
            first = node  # primer nodo del DLL
        last = node
        inorder(node.right)

    inorder(root)

    # Circularidad
    first.left = last
    last.right = first

    return first

# ✅ Validación del DLL circular generado
def validate_circular_dll(head, expected):
    if not head and not expected:
        return True
    result = []
    node = head
    for _ in range(len(expected)):
        result.append(node.val)
        node = node.right
    return result == expected and node == head  # debe volver al inicio

# 🔎 Casos de prueba
head1 = bst_to_dll(build_bst([2, 1, 3]))
print(validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗 Simple conversion

head2 = bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7]))
print(validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 📊 Complex

head3 = bst_to_dll(build_bst([5]))
print(validate_circular_dll(head3, [5]) == True)  # 🌱 Single node

head4 = bst_to_dll(build_degenerate_bst([1, 2, 3, 4]))
print(validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Degenerate

head5 = bst_to_dll(None)
print(head5 is None)  # 📭 Empty tree
