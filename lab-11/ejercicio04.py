# Definimos el nodo del árbol
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Clase base del BST
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def build_from_list(self, values):
        for value in values:
            self.insert(value)

# Subclase que extiende funcionalidades
class BinarySearchTree(BinarySearchTree):
    def kth_smallest(self, k):
        """📊 Encuentra el k-ésimo menor valor del BST usando recorrido inorden"""

        self.counter = 0       # Para contar nodos visitados
        self.result = None     # Para guardar el resultado cuando lleguemos al k-ésimo

        def inorder(node):
            # Si el nodo es nulo o ya encontramos el resultado, salimos
            if node is None or self.result is not None:
                return

            # Visita izquierda
            inorder(node.left)

            # Incrementamos contador al visitar nodo
            self.counter += 1
            if self.counter == k:
                self.result = node.value
                return  # Terminamos temprano

            # Visita derecha
            inorder(node.right)

        inorder(self.root)
        return self.result
def test_kth_smallest():
    bst1 = BinarySearchTree()
    bst1.build_from_list([3, 1, 4, 2])
    print("🧪 Test 1:", bst1.kth_smallest(2) == 2)  # 🎯 Segundo menor

    bst2 = BinarySearchTree()
    bst2.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 2:", bst2.kth_smallest(1) == 2)  # 📉 El menor

    print("🧪 Test 3:", bst2.kth_smallest(7) == 8)  # 📈 El mayor

    bst3 = BinarySearchTree()
    bst3.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 4:", bst3.kth_smallest(4) == 4)  # 🔗 En el medio

    bst4 = BinarySearchTree()
    bst4.build_from_list([10])
    print("🧪 Test 5:", bst4.kth_smallest(1) == 10)  # 🌱 Un solo nodo

# 🚀 Ejecutar los tests
test_kth_smallest()
