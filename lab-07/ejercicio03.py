# Definición de la clase TreeNode
class TreeNode:
    def __init__(self, value):
        # Constructor de la clase TreeNode
        self.value = value  # Valor del nodo
        self.left = None    # Referencia al hijo izquierdo (inicialmente None)
        self.right = None   # Referencia al hijo derecho (inicialmente None)

# Función para convertir un árbol binario en su imagen espejo
def mirror_tree(node):
    """Convierte un árbol binario en su imagen espejo intercambiando recursivamente los hijos izquierdo y derecho."""
    # Caso base: si el nodo es None (árbol vacío o fin de una rama)
    if node is None:
        return None

    # Proceso recursivo: 
    # 1. Primero hacemos imagen espejo de los subárboles derecho e izquierdo 
    # 2. Luego intercambiamos los hijos del nodo actual
    left_mirrored = mirror_tree(node.right)  # El hijo derecho se convertirá en el nuevo hijo izquierdo
    right_mirrored = mirror_tree(node.left)  # El hijo izquierdo se convertirá en el nuevo hijo derecho
    
    # Asignamos los subárboles ya espejados a los hijos opuestos
    node.left = left_mirrored
    node.right = right_mirrored
    
    # Devolvemos el nodo raíz del árbol espejado
    return node

# Función para recorrido inorden (Izquierda - Raíz - Derecha)
def inorder_traversal(node):
    """Devuelve el recorrido inorden del árbol como una lista."""
    # Caso base: si el nodo es None
    if node is None:
        return []
    
    # Recorrido inorden: izquierda, raíz, derecha
    # Utilizamos concatenación de listas para construir el resultado final
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)


# Casos de prueba para la función mirror_tree
def test_mirror_tree():
    # Caso de prueba 1: Árbol normal
    # Estructura original:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Test Case 1 - Normal Tree")
    print("Original inorder:", inorder_traversal(root))  # [4, 2, 5, 1, 3]
    mirror_tree(root)
    # Estructura espejada:
    #        1
    #       / \
    #      3   2
    #         / \
    #        5   4
    print("Mirrored inorder:", inorder_traversal(root))  # [3, 1, 5, 2, 4]
    print()

    # Caso de prueba 2: Árbol vacío
    empty_tree = None
    print("Test Case 2 - Empty Tree")
    mirrored_empty = mirror_tree(empty_tree)
    print("Mirrored inorder:", inorder_traversal(mirrored_empty))  # []
    print()

    # Caso de prueba 3: Árbol con un solo nodo
    single_node = TreeNode(10)
    print("Test Case 3 - Single Node")
    print("Original inorder:", inorder_traversal(single_node))  # [10]
    mirror_tree(single_node)
    print("Mirrored inorder:", inorder_traversal(single_node))  # [10]
    print()

# Ejecutar todos los casos de prueba
test_mirror_tree()