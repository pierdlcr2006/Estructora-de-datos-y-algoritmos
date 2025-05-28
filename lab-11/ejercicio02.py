# 🔧 Definición de clase y utilidades de BST
class TreeNode:
    def __init__(self, val):
        self.val = val       # Almacena el valor del nodo
        self.left = None     # Puntero al hijo izquierdo (inicialmente vacío)
        self.right = None    # Puntero al hijo derecho (inicialmente vacío)

def insert_bst(root, val):
    if root is None:
        return TreeNode(val)  # Si el árbol está vacío, crea un nuevo nodo como raíz
    if val < root.val:
        root.left = insert_bst(root.left, val)  # Si el valor es menor, inserta en subárbol izquierdo
    else:
        root.right = insert_bst(root.right, val)  # Si el valor es mayor o igual, inserta en subárbol derecho
    return root  # Devuelve la raíz actualizada después de la inserción

def build_bst(values):
    root = None  # Comienza con un árbol vacío
    for val in values:
        root = insert_bst(root, val)  # Inserta cada valor en el BST
    return root  # Devuelve la raíz del árbol completo

# 🌲 Función principal: encontrar Lowest Common Ancestor (LCA)
def find_lca(root, val1, val2):
    """Find lowest common ancestor of two values in BST"""
    current = root  # Comenzamos desde la raíz del árbol
    while current:
        if val1 < current.val and val2 < current.val:
            current = current.left  # Si ambos valores son menores que el nodo actual, buscamos en el subárbol izquierdo
        elif val1 > current.val and val2 > current.val:
            current = current.right  # Si ambos valores son mayores que el nodo actual, buscamos en el subárbol derecho
        else:
            # Llegamos al punto de divergencia o uno de los valores es igual al nodo actual
            return current.val  # Este es el LCA, devolvemos su valor
    return None  # En caso de que el árbol esté vacío o los valores no existan (caso de seguridad)

# ✅ Test cases
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)  # 🌲 Prueba cuando la raíz es el LCA
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 0, 4) == 2)  # 📊 Prueba cuando el LCA es un nodo interno
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 3) == 2)  # 🔗 Prueba cuando uno de los nodos es ancestro del otro
print(find_lca(build_bst([5, 3, 7]), 5, 5) == 5)                    # 🎯 Prueba cuando ambos valores son el mismo nodo
print(find_lca(build_bst([4, 2, 6, 1, 3, 5, 7]), 1, 3) == 2)        # 🌱 Prueba con nodos hoja que comparten un ancestro