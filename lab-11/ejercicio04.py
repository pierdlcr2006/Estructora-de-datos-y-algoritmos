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
