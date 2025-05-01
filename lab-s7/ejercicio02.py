class TreeNode:
    def __init__(self, value):
        # Constructor de la clase TreeNode
        # Inicializa un nodo con un valor y referencias nulas a los hijos
        self.value = value  # Valor del nodo
        self.left = None    # Referencia al hijo izquierdo (inicialmente None)
        self.right = None   # Referencia al hijo derecho (inicialmente None)
    
def count_leaves(node):
    """
    Función para contar las hojas de un árbol binario.
    Una hoja es un nodo que no tiene hijos (ni izquierdo ni derecho).
    """
    # Caso base 1: Si el nodo es None (árbol vacío o llegamos al final de una rama)
    if node is None:
        return 0  # No hay hojas en un árbol vacío
    
    # Caso base 2: Si el nodo es una hoja (no tiene hijos)
    if node.left is None and node.right is None:
        return 1  # Encontramos una hoja, devolvemos 1
    
    # Caso recursivo: Si el nodo tiene al menos un hijo
    # Sumamos las hojas del subárbol izquierdo y del subárbol derecho
    return count_leaves(node.left) + count_leaves(node.right)



def test_count_leaves():
    """Función de prueba para verificar el funcionamiento de count_leaves."""
    
    # Test Case 1: Árbol con solo hijos izquierdos (árbol inclinado a la izquierda)
    # Estructura:  1 -> 2 -> 3 -> 4
    # Donde cada nodo solo tiene un hijo izquierdo
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    root4.left.left.left = TreeNode(4)
    resultado4 = count_leaves(root4)
    print(resultado4)  # Salida esperada: 1 (solo el nodo 4 es una hoja)

    # Test Case 2: Árbol con solo hijos derechos (árbol inclinado a la derecha)
    # Estructura:  1 -> 2 -> 3 -> 4
    # Donde cada nodo solo tiene un hijo derecho
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    root5.right.right.right = TreeNode(4)
    resultado5 = count_leaves(root5)
    print(resultado5)  # Salida esperada: 1 (solo el nodo 4 es una hoja)

    # Test Case 3: Árbol lleno hasta el segundo nivel (árbol binario completo)
    # Estructura:
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.left.left = TreeNode(4)
    root6.left.right = TreeNode(5)
    root6.right.left = TreeNode(6)
    root6.right.right = TreeNode(7)
    resultado6 = count_leaves(root6)
    print(resultado6)  # Salida esperada: 4 (los nodos 4, 5, 6 y 7 son hojas)

# Ejecutar tests con resultados visibles
test_count_leaves()