class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # ⬅️ Anterior
        self.right = None  # ➡️ Siguiente

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def build_from_list(self, values):
        for value in values:
            self.insert(value)

class BinarySearchTree(BinarySearchTree):  # Extendemos la clase
    def bst_to_dll(self):
        """🔁 Convertir BST en lista doblemente enlazada circular ordenada"""
        if not self.root:
            return None

        self.first = None  # 🔗 Cabeza de la lista
        self.last = None   # 🔚 Último nodo visitado

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node  # Primer nodo visitado

            self.last = node
            inorder(node.right)

        inorder(self.root)

        # Hacer la lista circular ⭕
        self.first.left = self.last
        self.last.right = self.first

        return self.first

# ✅ Validador de la lista circular
def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []
    values = []
    current = head
    while True:
        values.append(current.value)
        current = current.right
        if current == head:
            break
    return values == expected_values

# 🧪 Pruebas
def test_bst_to_dll():
    bst1 = BinarySearchTree()
    bst1.build_from_list([2, 1, 3])
    head1 = bst1.bst_to_dll()
    print("🧪 Test 1:", validate_circular_dll(head1, [1, 2, 3]) == True)

    bst2 = BinarySearchTree()
    bst2.build_from_list([4, 2, 6, 1, 3, 5, 7])
    head2 = bst2.bst_to_dll()
    print("🧪 Test 2:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)

    bst3 = BinarySearchTree()
    bst3.build_from_list([5])
    head3 = bst3.bst_to_dll()
    print("🧪 Test 3:", validate_circular_dll(head3, [5]) == True)

    bst4 = BinarySearchTree()
    bst4.build_from_list([1, 2, 3, 4])
    head4 = bst4.bst_to_dll()
    print("🧪 Test 4:", validate_circular_dll(head4, [1, 2, 3, 4]) == True)

    bst5 = BinarySearchTree()
    head5 = bst5.bst_to_dll()
    print("🧪 Test 5:", head5 is None)

# 🚀 Ejecutar pruebas
test_bst_to_dll()
