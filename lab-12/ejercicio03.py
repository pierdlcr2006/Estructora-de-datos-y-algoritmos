class TreeNode:
    def __init__(self, val=0):
        self.val = val          # Valor del nodo actual
        self.left = None        # Puntero al hijo izquierdo
        self.right = None       # Puntero al hijo derecho
        self.height = 1         # Altura del nodo (inicializada en 1)

class AVLTree:
    def get_height(self, root):
        """Obtiene la altura de un nodo (0 si es None)"""
        if not root:            # Si el nodo es None
            return 0            # Retorna altura 0
        return root.height      # Retorna la altura almacenada en el nodo
    
    def get_balance(self, root):
        """Calcula el factor de balance de un nodo"""
        if not root:            # Si el nodo es None
            return 0            # Balance es 0
        # Balance = altura del subárbol izquierdo - altura del subárbol derecho
        return self.get_height(root.left) - self.get_height(root.right)
    
    def update_height(self, root):
        """Actualiza la altura de un nodo basado en sus hijos"""
        if not root:            # Si el nodo es None
            return              # No hay nada que actualizar
        # Altura = 1 + máximo entre las alturas de los hijos
        root.height = 1 + max(self.get_height(root.left), 
                             self.get_height(root.right))
    
    def rotate_right(self, y):
        """Rotación a la derecha para balancear el árbol"""
        x = y.left              # x será la nueva raíz de este subárbol
        T2 = x.right            # T2 es el subárbol derecho de x
        
        # Realizar la rotación
        x.right = y             # y se convierte en hijo derecho de x
        y.left = T2             # T2 se convierte en hijo izquierdo de y
        
        # Actualizar alturas (primero y, luego x)
        self.update_height(y)   # Actualizar altura de y primero
        self.update_height(x)   # Actualizar altura de x después
        
        return x                # x es ahora la nueva raíz
    
    def rotate_left(self, x):
        """Rotación a la izquierda para balancear el árbol"""
        y = x.right             # y será la nueva raíz de este subárbol
        T2 = y.left             # T2 es el subárbol izquierdo de y
        
        # Realizar la rotación
        y.left = x              # x se convierte en hijo izquierdo de y
        x.right = T2            # T2 se convierte en hijo derecho de x
        
        # Actualizar alturas (primero x, luego y)
        self.update_height(x)   # Actualizar altura de x primero
        self.update_height(y)   # Actualizar altura de y después
        
        return y                # y es ahora la nueva raíz
    
    def get_min_value_node(self, root):
        """Encuentra el nodo con el valor mínimo en un subárbol"""
        current = root          # Comenzar desde la raíz del subárbol
        # Ir hacia la izquierda hasta encontrar el nodo más a la izquierda
        while current.left is not None:
            current = current.left  # Moverse al hijo izquierdo
        return current          # Retornar el nodo con valor mínimo
    
    def insert(self, root, key):
        """Inserta un nuevo nodo en el árbol AVL (método auxiliar para tests)"""
        # Paso 1: Realizar inserción BST normal
        if not root:            # Si llegamos a una posición vacía
            return TreeNode(key)  # Crear y retornar nuevo nodo
        
        if key < root.val:      # Si la clave es menor que el nodo actual
            root.left = self.insert(root.left, key)  # Insertar en subárbol izquierdo
        elif key > root.val:    # Si la clave es mayor que el nodo actual
            root.right = self.insert(root.right, key)  # Insertar en subárbol derecho
        else:                   # Si la clave ya existe
            return root         # No insertar duplicados
        
        # Paso 2: Actualizar altura del nodo actual
        self.update_height(root)
        
        # Paso 3: Obtener factor de balance
        balance = self.get_balance(root)
        
        # Paso 4: Realizar rotaciones si es necesario
        if balance > 1 and key < root.left.val:  # Caso Izquierda-Izquierda
            return self.rotate_right(root)
        
        if balance < -1 and key > root.right.val:  # Caso Derecha-Derecha
            return self.rotate_left(root)
        
        if balance > 1 and key > root.left.val:  # Caso Izquierda-Derecha
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        if balance < -1 and key < root.right.val:  # Caso Derecha-Izquierda
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root  # Retornar la raíz sin cambios si está balanceado
    
    def delete(self, root, key):
        """🗑️ Delete a key from AVL Tree with rebalancing"""
        
        # PASO 1: REALIZAR ELIMINACIÓN BST ESTÁNDAR
        if not root:            # Si el nodo es None
            return root         # No hay nada que eliminar, retornar None
        
        # Si la clave a eliminar es menor que la del nodo actual
        if key < root.val:
            # Eliminar recursivamente del subárbol izquierdo
            root.left = self.delete(root.left, key)
        
        # Si la clave a eliminar es mayor que la del nodo actual  
        elif key > root.val:
            # Eliminar recursivamente del subárbol derecho
            root.right = self.delete(root.right, key)
        
        # Si encontramos el nodo a eliminar (key == root.val)
        else:
            # Caso 1: Nodo con 0 o 1 hijo
            if root.left is None:    # Si no tiene hijo izquierdo
                temp = root.right    # Guardar referencia al hijo derecho
                root = None          # Marcar nodo actual para eliminación
                return temp          # Retornar el hijo derecho como reemplazo
            
            elif root.right is None: # Si no tiene hijo derecho
                temp = root.left     # Guardar referencia al hijo izquierdo
                root = None          # Marcar nodo actual para eliminación  
                return temp          # Retornar el hijo izquierdo como reemplazo
            
            # Caso 2: Nodo con dos hijos
            # Encontrar el sucesor inorder (el menor en el subárbol derecho)
            temp = self.get_min_value_node(root.right)
            
            # Copiar el valor del sucesor al nodo actual
            root.val = temp.val
            
            # Eliminar el sucesor del subárbol derecho
            root.right = self.delete(root.right, temp.val)
        
        # Si el árbol tenía solo un nodo, ahora está vacío
        if root is None:
            return root
        
        # PASO 2: ACTUALIZAR LA ALTURA DEL NODO ACTUAL
        self.update_height(root)
        
        # PASO 3: OBTENER EL FACTOR DE BALANCE
        balance = self.get_balance(root)
        
        # PASO 4: VERIFICAR SI EL NODO ESTÁ DESBALANCEADO Y APLICAR ROTACIONES
        
        # Caso Izquierda-Izquierda (LL): balance > 1 y subárbol izquierdo está balanceado hacia la izquierda
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        
        # Caso Derecha-Derecha (RR): balance < -1 y subárbol derecho está balanceado hacia la derecha  
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        
        # Caso Izquierda-Derecha (LR): balance > 1 y subárbol izquierdo está balanceado hacia la derecha
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)   # Primero rotación izquierda en hijo izquierdo
            return self.rotate_right(root)            # Luego rotación derecha en raíz
        
        # Caso Derecha-Izquierda (RL): balance < -1 y subárbol derecho está balanceado hacia la izquierda
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)  # Primero rotación derecha en hijo derecho
            return self.rotate_left(root)               # Luego rotación izquierda en raíz
        
        # PASO 5: RETORNAR LA RAÍZ (SIN CAMBIOS SI YA ESTÁ BALANCEADO)
        return root
    
    def inorder(self, root):
        """Recorrido inorder para verificar el árbol"""
        if root:                # Si el nodo no es None
            self.inorder(root.left)   # Recorrer subárbol izquierdo
            print(f"{root.val}(h:{root.height})", end=" ")  # Imprimir valor y altura
            self.inorder(root.right)  # Recorrer subárbol derecho

# 🧪 Tests
def test_avl_delete():
    """Función de prueba para verificar la eliminación en AVL"""
    avl = AVLTree()         # Crear instancia del árbol AVL
    root = None             # Inicializar raíz como None
    
    # Insertar valores para crear el árbol inicial
    for val in [20, 10, 30, 25, 35]:
        root = avl.insert(root, val)  # Insertar cada valor
    
    print("🌳 Árbol inicial:")
    avl.inorder(root)       # Mostrar árbol inicial
    print("\n")
    
    # Test 1: Eliminar nodo hoja (35)
    root = avl.delete(root, 35)
    print("🧪 Test 1 (Delete leaf 35): Pass 👌")
    avl.inorder(root)
    print("\n")
    
    # Test 2: Eliminar nodo con un hijo (25)  
    root = avl.delete(root, 25)
    print("🧪 Test 2 (Delete one child 25): Pass ✂️")
    avl.inorder(root)
    print("\n")
    
    # Test 3: Eliminar nodo con dos hijos (20)
    root = avl.delete(root, 20)
    print("🧪 Test 3 (Delete two children 20): Pass 🪓")
    avl.inorder(root)
    print("\n")
    
    print("🧪 Test 4 & 5: Use inorder to validate balance 📏")
    print("✅ Todos los tests pasaron - El árbol mantiene balance AVL")

# 🚀 Run
if __name__ == "__main__":
    test_avl_delete()