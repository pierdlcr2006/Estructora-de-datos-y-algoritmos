# 📦 Definición del nodo
class TreeNode:
    def __init__(self, val):
        self.val = val        # Almacena el valor del nodo
        self.left = None      # Referencia izquierda (actúa como prev en DLL)
        self.right = None     # Referencia derecha (actúa como next en DLL)

# 🔨 Función para insertar en BST
def insert_bst(root, val):
    if not root:
        return TreeNode(val)  # Si el árbol está vacío, crea un nuevo nodo raíz
    if val < root.val:
        root.left = insert_bst(root.left, val)  # Si es menor, inserta en subárbol izquierdo
    else:
        root.right = insert_bst(root.right, val)  # Si es mayor o igual, inserta en subárbol derecho
    return root  # Devuelve la raíz actualizada

# 🔨 Construcción de un BST completo
def build_bst(values):
    root = None  # Comienza con un árbol vacío
    for val in values:
        root = insert_bst(root, val)  # Inserta cada valor manteniendo propiedades BST
    return root  # Devuelve la raíz del BST

# 🔨 Construcción de un BST degenerado (como lista)
def build_degenerate_bst(values):
    root = None  # Inicializa la raíz como None
    for val in values:
        node = TreeNode(val)  # Crea un nuevo nodo con el valor actual
        if not root:
            root = node       # Si es el primer nodo, establece como raíz
            curr = root       # Y como nodo actual para seguimiento
        else:
            curr.right = node  # Agrega nodo a la derecha del actual (como una lista)
            curr = curr.right  # Avanza el puntero al nuevo nodo
    return root  # Devuelve la raíz del árbol degenerado

# 🔄 Conversión BST → Circular DLL ordenada
def bst_to_dll(root):
    """Convert BST to sorted circular doubly linked list"""
    if not root:
        return None  # Si el árbol está vacío, devuelve None

    first = last = None  # Inicializa referencias al primer y último nodo del DLL

    def inorder(node):
        nonlocal first, last  # Usa variables del ámbito exterior
        if not node:
            return  # Si el nodo es None, termina esta rama de recursión
        
        inorder(node.left)  # Procesa subárbol izquierdo primero (menores)
        
        if last:
            last.right = node  # Enlaza el último nodo procesado con el actual (next)
            node.left = last   # Enlaza el nodo actual con el último (prev)
        else:
            first = node  # Si es el primer nodo procesado, establece como cabeza del DLL
            
        last = node  # Actualiza el puntero al último nodo procesado
        
        inorder(node.right)  # Procesa subárbol derecho (mayores)

    inorder(root)  # Inicia el recorrido inorder desde la raíz

    # Establece circularidad conectando extremos
    first.left = last    # El primero apunta al último como prev
    last.right = first   # El último apunta al primero como next

    return first  # Devuelve la cabeza de la lista circular

# ✅ Validación del DLL circular generado
def validate_circular_dll(head, expected):
    if not head and not expected:
        return True  # Si ambos están vacíos, la validación es exitosa
        
    result = []  # Lista para almacenar valores del DLL
    node = head  # Comienza desde la cabeza del DLL
    
    for _ in range(len(expected)):
        result.append(node.val)  # Agrega valor del nodo actual
        node = node.right        # Avanza al siguiente nodo
        
    # Verifica que los valores coincidan y que la lista sea circular
    return result == expected and node == head  # Debe volver al inicio

# 🔎 Casos de prueba
head1 = bst_to_dll(build_bst([2, 1, 3]))
print(validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗 Simple conversion

head2 = bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7]))
print(validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 📊 Complex

head3 = bst_to_dll(build_bst([5]))
print(validate_circular_dll(head3, [5]) == True)  # 🌱 Single node

head4 = bst_to_dll(build_degenerate_bst([1, 2, 3, 4]))
print(validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Degenerate

head5 = bst_to_dll(None)
print(head5 is None)  # 📭 Empty tree
