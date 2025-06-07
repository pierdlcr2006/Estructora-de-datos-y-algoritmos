class AVLNode:
    def __init__(self, key):
        self.key = key          # Almacena el valor del nodo
        self.left = None        # Puntero al hijo izquierdo
        self.right = None       # Puntero al hijo derecho
        self.height = 1         # Altura inicial del nodo (hoja = 1)

class AVLTree:
    def insert(self, root, key):
        """🌱 Inserta una clave y rebalancea el árbol AVL"""
        # Paso 1: Realizar inserción normal de BST
        if not root:
            return AVLNode(key)  # Si no hay raíz, crear nuevo nodo
        
        if key < root.key:
            root.left = self.insert(root.left, key)    # Insertar en subárbol izquierdo
        elif key > root.key:
            root.right = self.insert(root.right, key)  # Insertar en subárbol derecho
        else:
            return root  # No permitir duplicados, retornar nodo existente
        
        # Paso 2: Actualizar la altura del nodo ancestro
        root.height = 1 + max(self.get_height(root.left), 
                             self.get_height(root.right))
        
        # Paso 3: Obtener el factor de balance de este nodo ancestro
        balance = self.get_balance(root)
        
        # Paso 4: Si el nodo está desbalanceado, hay 4 casos posibles
        
        # Caso Izquierda-Izquierda (LL): balance > 1 y key < root.left.key
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)  # Rotación simple a la derecha
        
        # Caso Derecha-Derecha (RR): balance < -1 y key > root.right.key
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)   # Rotación simple a la izquierda
        
        # Caso Izquierda-Derecha (LR): balance > 1 y key > root.left.key
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)    # Primera rotación izquierda
            return self.rotate_right(root)             # Segunda rotación derecha
        
        # Caso Derecha-Izquierda (RL): balance < -1 y key < root.right.key
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right) # Primera rotación derecha
            return self.rotate_left(root)              # Segunda rotación izquierda
        
        # Retornar el nodo raíz sin cambios (si está balanceado)
        return root
    
    def get_height(self, node):
        """📏 Retorna la altura de un nodo"""
        if not node:
            return 0  # Nodo nulo tiene altura 0
        return node.height  # Retorna la altura almacenada en el nodo
    
    def get_balance(self, node):
        """⚖️ Retorna el factor de balance"""
        if not node:
            return 0  # Nodo nulo tiene balance 0
        # Factor de balance = altura_izquierda - altura_derecha
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_left(self, z):
        """🔄 Rotación simple a la izquierda (para caso RR)"""
        y = z.right        # y será la nueva raíz
        T2 = y.left        # Subárbol que se moverá
        
        # Realizar rotación
        y.left = z         # z se convierte en hijo izquierdo de y
        z.right = T2       # T2 se convierte en hijo derecho de z
        
        # Actualizar alturas (primero z, luego y)
        z.height = 1 + max(self.get_height(z.left), 
                          self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), 
                          self.get_height(y.right))
        
        return y  # Retornar nueva raíz
    
    def rotate_right(self, z):
        """🔄 Rotación simple a la derecha (para caso LL)"""
        y = z.left         # y será la nueva raíz
        T3 = y.right       # Subárbol que se moverá
        
        # Realizar rotación
        y.right = z        # z se convierte en hijo derecho de y
        z.left = T3        # T3 se convierte en hijo izquierdo de z
        
        # Actualizar alturas (primero z, luego y)
        z.height = 1 + max(self.get_height(z.left), 
                          self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), 
                          self.get_height(y.right))
        
        return y  # Retornar nueva raíz
    
    def inorder(self, root):
        """📜 Recorrido en orden (in-order traversal)"""
        if root:
            self.inorder(root.left)   # Visitar subárbol izquierdo
            print(root.key, end=" ")  # Imprimir valor del nodo
            self.inorder(root.right)  # Visitar subárbol derecho

# 🧪 Casos de prueba
def test_avl_insert():
    # Test 1: Caso Derecha-Derecha (RR) - requiere rotación izquierda
    avl = AVLTree()
    root = None
    for val in [10, 20, 30]:  # Inserción que causa desbalance RR
        root = avl.insert(root, val)
    print("🧪 Test 1 (RR):", end=" ")
    avl.inorder(root)  # Esperado: 10 20 30
    print()
    
    # Test 2: Caso Izquierda-Izquierda (LL) - requiere rotación derecha
    avl = AVLTree()
    root = None
    for val in [30, 20, 10]:  # Inserción que causa desbalance LL
        root = avl.insert(root, val)
    print("🧪 Test 2 (LL):", end=" ")
    avl.inorder(root)  # Esperado: 10 20 30
    print()
    
    # Test 3: Caso Izquierda-Derecha (LR) - requiere doble rotación
    avl = AVLTree()
    root = None
    for val in [30, 10, 20]:  # Inserción que causa desbalance LR
        root = avl.insert(root, val)
    print("🧪 Test 3 (LR):", end=" ")
    avl.inorder(root)  # Esperado: 10 20 30
    print()
    
    # Test 4: Caso Derecha-Izquierda (RL) - requiere doble rotación
    avl = AVLTree()
    root = None
    for val in [10, 30, 20]:  # Inserción que causa desbalance RL
        root = avl.insert(root, val)
    print("🧪 Test 4 (RL):", end=" ")
    avl.inorder(root)  # Esperado: 10 20 30
    print()
    
    # Test 5: Árbol balanceado - no requiere rotaciones
    avl = AVLTree()
    root = None
    for val in [15, 10, 20, 25, 30]:  # Inserción que mantiene balance
        root = avl.insert(root, val)
    print("🧪 Test 5 (Balanced):", end=" ")
    avl.inorder(root)  # Esperado: 10 15 20 25 30
    print()

# 🚀 Ejecutar todas las pruebas
if __name__ == "__main__":
    test_avl_insert()