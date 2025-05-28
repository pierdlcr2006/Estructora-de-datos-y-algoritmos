# Definimos una clase auxiliar para los nodos del árbol binario de búsqueda
class TreeNode:
    def __init__(self, value):
        self.value = value        # Valor del nodo actual
        self.left = None          # Puntero al subárbol izquierdo
        self.right = None         # Puntero al subárbol derecho

# Clase principal para el Árbol Binario de Búsqueda (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Raíz del árbol

    # Método para insertar un nuevo valor en el árbol
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)  # Si el árbol está vacío, el nuevo nodo es la raíz
        else:
            self._insert_recursive(self.root, value)  # Inserción recursiva

    # Método recursivo privado para insertar valores
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)  # Insertar como hijo izquierdo
            else:
                self._insert_recursive(node.left, value)  # Repetir en el subárbol izquierdo
        else:
            if node.right is None:
                node.right = TreeNode(value)  # Insertar como hijo derecho
            else:
                self._insert_recursive(node.right, value)  # Repetir en el subárbol derecho

    # Método para construir un árbol desde una lista de valores
    def build_from_list(self, values):
        for value in values:
            self.insert(value)  # Insertamos cada valor en el árbol

    # ✅ Método solicitado: encontrar los valores dentro del rango [min_val, max_val]
    def range_query(self, min_val, max_val):
        """🎯 Encuentra todos los valores dentro del rango dado en el BST"""
        result = []  # Lista donde almacenaremos los valores válidos

        # Función recursiva para recorrer el árbol en orden
        def inorder(node):
            if not node:
                return  # Caso base: si el nodo es None, terminamos

            # Solo visitamos el subárbol izquierdo si el valor actual es mayor al mínimo
            if node.value > min_val:
                inorder(node.left)

            # Si el valor actual está dentro del rango, lo agregamos al resultado
            if min_val <= node.value <= max_val:
                result.append(node.value)

            # Solo visitamos el subárbol derecho si el valor actual es menor al máximo
            if node.value < max_val:
                inorder(node.right)

        inorder(self.root)  # Iniciamos la búsqueda desde la raíz
        return result  # Devolvemos los valores encontrados

# 🧪 Casos de prueba
def test_range_query():
    bst1 = BinarySearchTree()
    bst1.build_from_list([7, 3, 11, 1, 5, 9, 13])
    print("🧪 Test 1:", bst1.range_query(5, 10) == [5, 7, 9])  # ✅

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 4, 8, 2])
    print("🧪 Test 2:", bst2.range_query(1, 10) == [2, 4, 6, 8])  # 🌐

    bst3 = BinarySearchTree()
    bst3.build_from_list([20, 10, 30])
    print("🧪 Test 3:", bst3.range_query(1, 5) == [])  # 📭

    bst4 = BinarySearchTree()
    bst4.build_from_list([15])
    print("🧪 Test 4:", bst4.range_query(10, 20) == [15])  # 🌱

    bst5 = BinarySearchTree()
    bst5.build_from_list([15, 10, 20, 5, 25])
    print("🧪 Test 5:", bst5.range_query(10, 20) == [10, 15, 20])  # 🔗

# 🚀 Ejecutar los tests
test_range_query()
