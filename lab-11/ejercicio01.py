# Definición de la clase TreeNode que representa un nodo en el árbol binario de búsqueda (BST)
class TreeNode:
    def __init__(self, val):
        self.val = val       # Valor almacenado en el nodo
        self.left = None     # Referencia al hijo izquierdo (inicialmente None)
        self.right = None    # Referencia al hijo derecho (inicialmente None)

# Función recursiva para insertar un valor en el BST manteniendo sus propiedades
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)  # Si el árbol está vacío, crea un nuevo nodo como raíz
    if val < root.val:
        # Si el valor es menor que el nodo actual, inserta en el subárbol izquierdo
        root.left = insert_bst(root.left, val)
    else:
        # Si el valor es mayor o igual, inserta en el subárbol derecho
        root.right = insert_bst(root.right, val)
    return root  # Devuelve la raíz del árbol modificado

# Función para construir un árbol BST completo a partir de una lista de valores
def build_bst(values):
    root = None  # Comienza con un árbol vacío
    for val in values:
        # Inserta cada valor de la lista en el BST
        root = insert_bst(root, val)
    return root  # Devuelve la raíz del BST construido

# Función principal que encuentra todos los valores en un rango específico [min_val, max_val] dentro del BST
def range_query(root, min_val, max_val):
    result = []  # Lista para almacenar los valores encontrados en el rango

    # Función interna para realizar un recorrido en profundidad (DFS) optimizado
    def dfs(node):
        if not node:
            return  # Si el nodo es None, termina esta rama de recursión
        
        if node.val > min_val:
            # Solo explora el subárbol izquierdo si puede contener valores ≥ min_val
            dfs(node.left)
            
        if min_val <= node.val <= max_val:
            # Si el valor actual está en el rango, lo agrega al resultado
            result.append(node.val)
            
        if node.val < max_val:
            # Solo explora el subárbol derecho si puede contener valores ≤ max_val
            dfs(node.right)

    # Inicia el recorrido DFS desde la raíz
    dfs(root)
    # Devuelve la lista de valores dentro del rango especificado
    return result

# Casos de prueba con diferentes escenarios
print(range_query(build_bst([7, 3, 11, 1, 5, 9, 13]), 5, 10) == [5, 7, 9])          # Prueba un rango normal
print(range_query(build_bst([6, 4, 8, 2]), 1, 10) == [2, 4, 6, 8])                  # Prueba un rango que cubre todos los nodos
print(range_query(build_bst([20, 10, 30]), 1, 5) == [])                             # Prueba un rango sin resultados
print(range_query(build_bst([15]), 10, 20) == [15])                                # Prueba con un solo nodo
print(range_query(build_bst([15, 10, 20, 5, 25]), 10, 20) == [10, 15, 20])          # Prueba incluyendo los límites del rango
