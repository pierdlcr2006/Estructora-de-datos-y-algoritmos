from collections import deque

class AVLNode:
    def __init__(self, val):
        self.val = val          # Valor del nodo
        self.left = None        # Hijo izquierdo
        self.right = None       # Hijo derecho
        self.height = 1         # Altura inicial del nodo

class AVLTree:
    def get_height(self, node):
        """📏 Obtiene la altura de un nodo"""
        if not node:            # Si el nodo es None
            return 0            # La altura es 0
        return node.height      # Retorna la altura almacenada
    
    def get_balance(self, node):
        """⚖️ Calcula el factor de balance de un nodo"""
        if not node:            # Si el nodo es None
            return 0            # El balance es 0
        return self.get_height(node.left) - self.get_height(node.right)  # Balance = altura_izq - altura_der
    
    def update_height(self, node):
        """🔄 Actualiza la altura de un nodo basado en sus hijos"""
        if not node:            # Si el nodo es None
            return              # No hacer nada
        # La altura es 1 + la máxima altura de los hijos
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def rotate_right(self, y):
        """↪️ Rotación simple hacia la derecha"""
        x = y.left              # x será la nueva raíz
        T2 = x.right            # Guardamos el subárbol derecho de x
        
        # Realizamos la rotación
        x.right = y             # y se convierte en hijo derecho de x
        y.left = T2             # T2 se convierte en hijo izquierdo de y
        
        # Actualizamos alturas (primero y, luego x)
        self.update_height(y)   # Actualizar altura de y primero
        self.update_height(x)   # Actualizar altura de x después
        
        return x                # x es la nueva raíz
    
    def rotate_left(self, x):
        """↩️ Rotación simple hacia la izquierda"""
        y = x.right             # y será la nueva raíz
        T2 = y.left             # Guardamos el subárbol izquierdo de y
        
        # Realizamos la rotación
        y.left = x              # x se convierte en hijo izquierdo de y
        x.right = T2            # T2 se convierte en hijo derecho de x
        
        # Actualizamos alturas (primero x, luego y)
        self.update_height(x)   # Actualizar altura de x primero
        self.update_height(y)   # Actualizar altura de y después
        
        return y                # y es la nueva raíz
    
    def insert(self, node, val):
        """➕ Inserta un valor en el árbol AVL manteniendo el balance"""
        # Paso 1: Inserción normal de BST
        if not node:            # Si llegamos a una posición vacía
            return AVLNode(val) # Crear un nuevo nodo
        
        if val < node.val:      # Si el valor es menor
            node.left = self.insert(node.left, val)    # Insertar en subárbol izquierdo
        elif val > node.val:    # Si el valor es mayor
            node.right = self.insert(node.right, val)  # Insertar en subárbol derecho
        else:                   # Si el valor ya existe
            return node         # No insertar duplicados
        
        # Paso 2: Actualizar altura del nodo actual
        self.update_height(node)
        
        # Paso 3: Obtener el factor de balance
        balance = self.get_balance(node)
        
        # Paso 4: Realizar rotaciones si es necesario
        # Caso Left-Left: balance > 1 y el nuevo nodo está en el subárbol izquierdo del hijo izquierdo
        if balance > 1 and val < node.left.val:
            return self.rotate_right(node)
        
        # Caso Right-Right: balance < -1 y el nuevo nodo está en el subárbol derecho del hijo derecho
        if balance < -1 and val > node.right.val:
            return self.rotate_left(node)
        
        # Caso Left-Right: balance > 1 y el nuevo nodo está en el subárbol derecho del hijo izquierdo
        if balance > 1 and val > node.left.val:
            node.left = self.rotate_left(node.left)     # Rotación izquierda en hijo izquierdo
            return self.rotate_right(node)              # Rotación derecha en nodo actual
        
        # Caso Right-Left: balance < -1 y el nuevo nodo está en el subárbol izquierdo del hijo derecho
        if balance < -1 and val < node.right.val:
            node.right = self.rotate_right(node.right)  # Rotación derecha en hijo derecho
            return self.rotate_left(node)               # Rotación izquierda en nodo actual
        
        return node             # Retornar el nodo (sin cambios si no hubo rotaciones)
    
    def print_level_order(self, root):
        """📡 Level-order print with heights"""
        if not root:            # Si el árbol está vacío
            return              # No imprimir nada
        
        queue = deque([root])   # Cola para BFS, comenzando con la raíz
        
        while queue:            # Mientras la cola no esté vacía
            level_size = len(queue)     # Número de nodos en el nivel actual
            level_nodes = []            # Lista para almacenar nodos del nivel actual
            
            # Procesar todos los nodos del nivel actual
            for i in range(level_size):
                node = queue.popleft()  # Sacar el primer nodo de la cola
                
                # Agregar información del nodo al nivel actual
                level_nodes.append(f"{node.val}(h{node.height})")
                
                # Agregar hijos a la cola para el siguiente nivel
                if node.left:           # Si tiene hijo izquierdo
                    queue.append(node.left)     # Agregarlo a la cola
                if node.right:          # Si tiene hijo derecho
                    queue.append(node.right)    # Agregarlo a la cola
            
            # Imprimir todos los nodos del nivel actual en una línea
            print(", ".join(level_nodes))

# 🧪 Test it!
def test_level_order_heights():
    """🧪 Función de prueba para el recorrido por niveles"""
    avl = AVLTree()             # Crear una instancia del árbol AVL
    root = None                 # Inicializar la raíz como vacía
    
    # Insertar valores en el árbol AVL
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)    # Insertar cada valor y actualizar la raíz
    
    print("🧪 Test 1–5: Expected output:")
    print("Actual output:")
    avl.print_level_order(root)         # Imprimir el recorrido por niveles

# 🚀 Go!
test_level_order_heights()

# 🧪 Pruebas adicionales
def additional_tests():
    """🔬 Pruebas adicionales para verificar todos los casos"""
    avl = AVLTree()
    
    # Test 1: Árbol simple [10, 5, 15]
    print("\n📋 Test 1: Árbol [10, 5, 15]")
    root1 = None
    for val in [10, 5, 15]:
        root1 = avl.insert(root1, val)
    avl.print_level_order(root1)
    
    # Test 2: Árbol vacío
    print("\n📋 Test 2: Árbol vacío")
    avl.print_level_order(None)
    
    # Test 3: Árbol con un solo nodo
    print("\n📋 Test 3: Árbol con un solo nodo")
    root3 = avl.insert(None, 42)
    avl.print_level_order(root3)
    
    # Test 4: Árbol más grande
    print("\n📋 Test 4: Árbol más grande [50, 25, 75, 10, 30, 60, 80, 5, 15]")
    root4 = None
    for val in [50, 25, 75, 10, 30, 60, 80, 5, 15]:
        root4 = avl.insert(root4, val)
    avl.print_level_order(root4)

additional_tests()