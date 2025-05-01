# Definición de la clase TreeNode y función tree_height con casos de prueba traducidos al español

class TreeNode:
    def __init__(self, value):
        # Constructor de la clase TreeNode que inicializa un nodo con un valor
        # y referencias nulas a los hijos izquierdo y derecho
        self.value = value  # Valor del nodo
        self.left = None    # Referencia al hijo izquierdo (inicialmente None)
        self.right = None   # Referencia al hijo derecho (inicialmente None)

def tree_height(node):
    """Calcula la altura de un árbol binario."""
    # Caso base: si el nodo es None (árbol vacío), la altura es -1
    # Por convención, un árbol vacío tiene altura -1
    if node is None:
        return -1
    
    # Caso recursivo: la altura es 1 + el máximo entre las alturas de los subárboles
    # Utilizamos recursión para calcular la altura de cada subárbol y tomamos el camino más largo
    return 1 + max(tree_height(node.left), tree_height(node.right))


def test_tree_height():
    # Caso de prueba 1: Árbol inclinado a la derecha (right-skewed)
    # Estructura:  1 -> 2 -> 3 -> 4
    # Es decir, cada nodo solo tiene un hijo derecho
    # Gráficamente:
    #   1
    #    \
    #     2
    #      \
    #       3
    #        \
    #         4
    right_skewed = TreeNode(1)
    right_skewed.right = TreeNode(2)
    right_skewed.right.right = TreeNode(3)
    right_skewed.right.right.right = TreeNode(4)
    print(tree_height(right_skewed))  # Salida esperada: 3 (hay 3 aristas en el camino más largo)

    # Caso de prueba 2: Árbol con estructura equilibrada y grande
    # Estructura de árbol completo en los primeros 2 niveles con algunos nodos adicionales
    # en el tercer nivel (solo bajo el nodo 4)
    # Gráficamente:
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    #   / \
    #  8   9
    balanced = TreeNode(1)
    balanced.left = TreeNode(2)
    balanced.right = TreeNode(3)
    balanced.left.left = TreeNode(4)
    balanced.left.right = TreeNode(5)
    balanced.right.left = TreeNode(6)
    balanced.right.right = TreeNode(7)
    balanced.left.left.left = TreeNode(8)
    balanced.left.left.right = TreeNode(9)
    print(tree_height(balanced))  # Salida esperada: 3 (hay 3 aristas en el camino más largo)

    # Caso de prueba 3: Árbol con un solo hijo por nodo (inclinado a la izquierda)
    # Estructura: 1 -> 2 -> 3 -> 4 -> 5 (cada nodo solo tiene hijo izquierdo)
    # Gráficamente:
    #           1
    #          /
    #         2 
    #        /
    #       3
    #      /
    #     4
    #    /
    #   5
    single_child = TreeNode(1)
    single_child.left = TreeNode(2)
    single_child.left.left = TreeNode(3)
    single_child.left.left.left = TreeNode(4)
    single_child.left.left.left.left = TreeNode(5)
    print(tree_height(single_child))  # Salida esperada: 4 (hay 4 aristas en el camino más largo)

# Ejecutar las pruebas
test_tree_height()