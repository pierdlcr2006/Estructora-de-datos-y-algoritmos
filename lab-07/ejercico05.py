# Definición del nodo de un árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value      # Valor almacenado en el nodo
        self.left = None        # Referencia al hijo izquierdo (inicialmente None)
        self.right = None       # Referencia al hijo derecho (inicialmente None)

# Función que realiza el recorrido por niveles
def level_order_traversal(root):
    """Realiza el recorrido por niveles de un árbol binario sin usar la estructura deque."""
    # Caso base: si el árbol está vacío, devolvemos una lista vacía
    if root is None:
        return []

    result = []                # Lista para almacenar el resultado del recorrido
    queue = [root]             # Usamos una lista como una cola FIFO (primero en entrar, primero en salir)
                               # Inicialmente, solo contiene el nodo raíz

    # Mientras la cola no esté vacía, continuamos procesando nodos
    while queue:
        node = queue.pop(0)    # Extraemos el primer elemento de la cola (operación FIFO)
        result.append(node.value)  # Añadimos el valor del nodo actual al resultado
        
        # Si el nodo tiene hijo izquierdo, lo añadimos a la cola para procesarlo después
        if node.left:
            queue.append(node.left)
            
        # Si el nodo tiene hijo derecho, lo añadimos a la cola para procesarlo después
        if node.right:
            queue.append(node.right)

    # Devolvemos la lista con los valores en orden de nivel
    return result


def test_level_order_traversal():
    # Caso de prueba 1: Árbol binario completo
    # Estructura:
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(level_order_traversal(root))  # Salida esperada: [1, 2, 3, 4, 5, 6, 7]

    # Caso de prueba 2: Árbol solo con hijos izquierdos (inclinado a la izquierda)
    # Estructura:
    #         1
    #        /
    #       2
    #      /
    #     3
    #    /
    #   4
    left_only = TreeNode(1)
    left_only.left = TreeNode(2)
    left_only.left.left = TreeNode(3)
    left_only.left.left.left = TreeNode(4)
    print(level_order_traversal(left_only))  # Salida esperada: [1, 2, 3, 4]

    # Caso de prueba 3: Árbol solo con hijos derechos (inclinado a la derecha)
    # Estructura:
    #   1
    #    \
    #     2
    #      \
    #       3
    #        \
    #         4
    right_only = TreeNode(1)
    right_only.right = TreeNode(2)
    right_only.right.right = TreeNode(3)
    right_only.right.right.right = TreeNode(4)
    print(level_order_traversal(right_only))  # Salida esperada: [1, 2, 3, 4]


# Ejecutar las pruebas
test_level_order_traversal()