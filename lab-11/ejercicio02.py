# Clase auxiliar para los nodos del árbol binario de búsqueda
class TreeNode:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None    # Subárbol izquierdo
        self.right = None   # Subárbol derecho

# Clase del Árbol Binario de Búsqueda (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Raíz del árbol

    # Método para insertar un nuevo valor
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)  # Si está vacío, el valor se convierte en raíz
        else:
            self._insert_recursive(self.root, value)  # Insertamos recursivamente

    # Método auxiliar para insertar de forma recursiva
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)  # Insertar como hijo izquierdo
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)  # Insertar como hijo derecho
            else:
                self._insert_recursive(node.right, value)

    # Construir el árbol a partir de una lista de valores
    def build_from_list(self, values):
        for value in values:
            self.insert(value)

    # ✅ Método para encontrar el Ancestro Común Más Bajo (Lowest Common Ancestor)
    def find_lca(self, val1, val2):
        """🧬 Encuentra el ancestro común más bajo entre dos valores en el BST"""
        node = self.root  # Empezamos desde la raíz del árbol

        while node:
            # Si ambos valores son menores al nodo actual, buscamos en el subárbol izquierdo
            if val1 < node.value and val2 < node.value:
                node = node.left

            # Si ambos valores son mayores al nodo actual, buscamos en el subárbol derecho
            elif val1 > node.value and val2 > node.value:
                node = node.right

            # Si los valores se separan (uno menor y otro mayor), hemos encontrado el ancestro común
            else:
                return node.value  # Devolvemos el valor del ancestro común

        return None  # Si no se encuentra (caso raro o datos inválidos)

# 🧪 Casos de prueba para verificar el método find_lca
def test_find_lca():
    bst1 = BinarySearchTree()
    bst1.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 1:", bst1.find_lca(2, 8) == 6)  # 🌲 Raíz es el LCA

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 2:", bst2.find_lca(0, 4) == 2)  # 📚 LCA dentro de subárbol

    bst3 = BinarySearchTree()
    bst3.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 3:", bst3.find_lca(2, 3) == 2)  # 🔗 Uno es ancestro del otro

    bst4 = BinarySearchTree()
    bst4.build_from_list([5, 3, 7])
    print("🧪 Test 4:", bst4.find_lca(5, 5) == 5)  # 🎯 Mismo nodo

    bst5 = BinarySearchTree()
    bst5.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 5:", bst5.find_lca(1, 3) == 2)  # 🌿 Ambos están bajo el mismo subárbol

# 🚀 Ejecutar los tests
test_find_lca()
