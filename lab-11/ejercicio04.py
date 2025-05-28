# 📦 Clase de nodo y utilidades para construir BST
class TreeNode:
    def __init__(self, val):
        self.val = val       # Almacena el valor del nodo
        self.left = None     # Referencia al hijo izquierdo (inicialmente None)
        self.right = None    # Referencia al hijo derecho (inicialmente None)

def insert_bst(root, val):
    if root is None:
        return TreeNode(val)  # Si el árbol está vacío, crea un nuevo nodo raíz
    if val < root.val:
        root.left = insert_bst(root.left, val)  # Si el valor es menor, inserta en subárbol izquierdo
    else:
        root.right = insert_bst(root.right, val)  # Si el valor es mayor o igual, inserta en subárbol derecho
    return root  # Devuelve la raíz actualizada

def build_bst(values):
    root = None  # Comienza con un árbol vacío
    for val in values:
        root = insert_bst(root, val)  # Inserta cada valor en el BST
    return root  # Devuelve la raíz del árbol construido

# 🔍 Función principal: K-ésimo elemento más pequeño en BST
def kth_smallest(root, k):
    """Find kth smallest element in BST using inorder traversal"""
    count = 0    # Contador para seguir cuántos elementos hemos visitado
    result = None  # Variable para almacenar el resultado

    def inorder(node):
        nonlocal count, result  # Usa las variables definidas en el ámbito exterior
        if not node or result is not None:
            return  # Termina si el nodo es None o ya encontramos el resultado
        inorder(node.left)  # Primero visita el subárbol izquierdo (menores)
        count += 1  # Incrementa el contador después de visitar un nodo
        if count == k:
            result = node.val  # Si es el k-ésimo elemento, guarda su valor
            return  # Termina la búsqueda
        inorder(node.right)  # Visita el subárbol derecho (mayores)

    inorder(root)  # Inicia el recorrido inorder desde la raíz
    return result  # Devuelve el k-ésimo elemento más pequeño

# ✅ Casos de prueba
print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)              # 🎯 Segundo menor
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)     # 📊 Mínimo
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)     # 📈 Máximo
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)     # 🔗 Medio
print(kth_smallest(build_bst([10]), 1) == 10)                     # 🌱 Un solo nodo
