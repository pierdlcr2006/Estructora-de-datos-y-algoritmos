# 🔧 Clase base y utilidades de árbol
class TreeNode:
    def __init__(self, val):
        self.val = val        # Almacena el valor del nodo
        self.left = None      # Referencia al hijo izquierdo (inicialmente None)
        self.right = None     # Referencia al hijo derecho (inicialmente None)

# Inserta respetando reglas de BST
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)   # Si el árbol está vacío, crea un nuevo nodo raíz
    if val < root.val:
        root.left = insert_bst(root.left, val)  # Si el valor es menor, inserta en subárbol izquierdo
    else:
        root.right = insert_bst(root.right, val)  # Si el valor es mayor o igual, inserta en subárbol derecho
    return root  # Devuelve la raíz actualizada

# Crea un BST válido desde lista
def build_tree(values):
    root = None  # Comienza con un árbol vacío
    for val in values:
        root = insert_bst(root, val)  # Inserta cada valor manteniendo las propiedades del BST
    return root  # Devuelve la raíz del árbol construido

# 🚫 Crea árbol inválido - violación en izquierda
def build_invalid_tree1():
    root = TreeNode(5)  # Crea nodo raíz con valor 5
    root.left = TreeNode(6)  # Violación: 6 > 5 (en BST válido, hijo izquierdo debe ser menor que padre)
    root.right = TreeNode(7)  # Hijo derecho válido (7 > 5)
    return root  # Retorna árbol inválido para pruebas

# 🚫 Crea árbol inválido - violación en derecha
def build_invalid_tree2():
    root = TreeNode(5)  # Crea nodo raíz con valor 5
    root.left = TreeNode(3)  # Hijo izquierdo válido (3 < 5)
    root.right = TreeNode(4)  # Violación: 4 < 5 (en BST válido, hijo derecho debe ser mayor que padre)
    return root  # Retorna árbol inválido para pruebas

# ✅ Función principal: validar BST usando min/max
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True  # Un árbol vacío es un BST válido
        if not (min_val < node.val < max_val):
            return False  # Si el valor del nodo está fuera del rango permitido, no es un BST válido
        return (validate(node.left, min_val, node.val) and  # Verifica subárbol izquierdo con límite superior actualizado
                validate(node.right, node.val, max_val))    # Verifica subárbol derecho con límite inferior actualizado
    
    return validate(root, float('-inf'), float('inf'))  # Inicia validación con rango infinito

# ✅ Test cases
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)   # ✅ Valid BST - árbol construido correctamente
print(is_valid_bst(build_invalid_tree1()) == False)             # ❌ Left violation - valor izquierdo mayor que padre
print(is_valid_bst(build_invalid_tree2()) == False)             # ❌ Right violation - valor derecho menor que padre
print(is_valid_bst(build_tree([42])) == True)                   # 🌱 Single node - un solo nodo siempre es BST válido
print(is_valid_bst(None) == True)                               # 📭 Empty tree - árbol vacío también es BST válido
