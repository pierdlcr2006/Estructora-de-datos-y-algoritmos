# Definimos la clase del nodo del árbol
class Node:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None    # Hijo izquierdo
        self.right = None   # Hijo derecho

# Clase del Árbol Binario de Búsqueda
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Raíz del árbol

    # Inserta valores en el árbol manteniendo la propiedad BST
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)  # Si el árbol está vacío, el nuevo nodo es la raíz
        else:
            self._insert_recursive(self.root, value)

    # Inserción recursiva de nodos
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # Insertar a la izquierda
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)  # Insertar a la derecha
            else:
                self._insert_recursive(node.right, value)

    # Construye el árbol desde una lista de valores
    def build_from_list(self, values):
        for value in values:
            self.insert(value)

    # ✅ Verifica si el árbol es un BST válido
    def is_valid_bst(self):
        """🧼 Verifica que el árbol cumpla con la propiedad de BST"""

        def validate(node, min_val, max_val):
            # Si llegamos a un nodo nulo, es válido
            if node is None:
                return True

            # El valor del nodo debe estar dentro del rango permitido
            if not (min_val < node.value < max_val):
                return False

            # Validar el subárbol izquierdo: todos los valores deben ser < nodo actual
            left_valid = validate(node.left, min_val, node.value)

            # Validar el subárbol derecho: todos los valores deben ser > nodo actual
            right_valid = validate(node.right, node.value, max_val)

            return left_valid and right_valid  # Ambos subárboles deben ser válidos

        # Iniciamos la validación desde la raíz con los límites máximos posibles
        return validate(self.root, float('-inf'), float('inf'))

# 🧪 Casos de prueba para validar árboles BST
def test_is_valid_bst():
    bst1 = BinarySearchTree()
    bst1.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 1:", bst1.is_valid_bst() == True)  # ✅ Árbol válido

    bst2 = BinarySearchTree()
    bst2.root = Node(5)
    bst2.root.left = Node(6)  # ❌ Incorrecto: 6 está a la izquierda de 5
    bst2.root.right = Node(7)
    print("🧪 Test 2:", bst2.is_valid_bst() == False)  # ❌ Violación izquierda

    bst3 = BinarySearchTree()
    bst3.root = Node(5)
    bst3.root.left = Node(3)
    bst3.root.right = Node(4)  # ❌ Incorrecto: 4 está a la derecha de 5
    print("🧪 Test 3:", bst3.is_valid_bst() == False)  # ❌ Violación derecha

    bst4 = BinarySearchTree()
    bst4.build_from_list([42])
    print("🧪 Test 4:", bst4.is_valid_bst() == True)  # 🌱 Nodo único válido

    bst5 = BinarySearchTree()
    print("🧪 Test 5:", bst5.is_valid_bst() == True)  # 📭 Árbol vacío válido

# 🚀 Ejecutar todos los tests
test_is_valid_bst()
