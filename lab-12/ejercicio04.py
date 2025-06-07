class AVLNode:
    """🌳 Clase que representa un nodo del árbol AVL"""
    def __init__(self, key):
        self.key = key          # Valor del nodo
        self.left = None        # Hijo izquierdo
        self.right = None       # Hijo derecho
        self.height = 1         # Altura del nodo (inicialmente 1)

class AVLTree:
    """🌲 Clase principal del árbol AVL con verificador de balance"""
    
    def get_height(self, root):
        """📏 Obtiene la altura de un nodo"""
        if not root:            # Si el nodo es None (vacío)
            return 0            # La altura es 0
        return root.height      # Retorna la altura almacenada en el nodo
    
    def get_balance(self, root):
        """⚖️ Calcula el factor de balance de un nodo"""
        if not root:            # Si el nodo es None
            return 0            # El balance es 0
        # Balance = altura del subárbol izquierdo - altura del subárbol derecho
        return self.get_height(root.left) - self.get_height(root.right)
    
    def is_avl_balanced(self, root):
        """📏 Verifica si el árbol es un AVL válido"""
        # Función auxiliar que retorna la altura si es válido, -1 si no es válido
        def check_balance_and_height(node):
            if not node:                    # Caso base: nodo vacío
                return 0                    # Altura 0 (válido)
            
            # Verificar recursivamente el subárbol izquierdo
            left_height = check_balance_and_height(node.left)
            if left_height == -1:           # Si el subárbol izquierdo no es válido
                return -1                   # Propagar el error hacia arriba
            
            # Verificar recursivamente el subárbol derecho
            right_height = check_balance_and_height(node.right)
            if right_height == -1:          # Si el subárbol derecho no es válido
                return -1                   # Propagar el error hacia arriba
            
            # Calcular el factor de balance del nodo actual
            balance_factor = left_height - right_height
            
            # Verificar si el factor de balance está en el rango válido [-1, 1]
            if abs(balance_factor) > 1:     # Si el balance excede los límites
                return -1                   # El árbol no es AVL válido
            
            # Si llegamos aquí, el nodo es válido
            # Retornar la altura del nodo actual (máximo de subárboles + 1)
            return max(left_height, right_height) + 1
        
        # Llamar a la función auxiliar y verificar si el resultado es válido
        result = check_balance_and_height(root)
        return result != -1                 # True si es válido, False si no
    
    def insert(self, root, key):
        """🔧 Método auxiliar para insertar nodos (para testing)"""
        # Inserción normal de BST
        if not root:                        # Si no hay nodo, crear uno nuevo
            return AVLNode(key)
        
        if key < root.key:                  # Si la clave es menor
            root.left = self.insert(root.left, key)     # Insertar en subárbol izquierdo
        elif key > root.key:                # Si la clave es mayor
            root.right = self.insert(root.right, key)   # Insertar en subárbol derecho
        else:                               # Si la clave ya existe
            return root                     # No insertar duplicados
        
        # Actualizar altura del nodo actual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Obtener factor de balance
        balance = self.get_balance(root)
        
        # Rotaciones para mantener balance AVL
        # Rotación derecha (caso Left-Left)
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        
        # Rotación izquierda (caso Right-Right)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        
        # Rotación izquierda-derecha (caso Left-Right)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # Rotación derecha-izquierda (caso Right-Left)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root                         # Retornar el nodo (sin cambios si está balanceado)
    
    def rotate_left(self, z):
        """🔄 Rotación izquierda"""
        y = z.right                         # y es el hijo derecho de z
        T2 = y.left                         # T2 es el subárbol izquierdo de y
        
        # Realizar rotación
        y.left = z                          # z se convierte en hijo izquierdo de y
        z.right = T2                        # T2 se convierte en hijo derecho de z
        
        # Actualizar alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y                            # y es la nueva raíz
    
    def rotate_right(self, z):
        """🔄 Rotación derecha"""
        y = z.left                          # y es el hijo izquierdo de z
        T3 = y.right                        # T3 es el subárbol derecho de y
        
        # Realizar rotación
        y.right = z                         # z se convierte en hijo derecho de y
        z.left = T3                         # T3 se convierte en hijo izquierdo de z
        
        # Actualizar alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y                            # y es la nueva raíz

# 🧪 Casos de prueba completos
def test_is_avl_balanced():
    """🧪 Función que ejecuta todos los tests"""
    avl = AVLTree()
    
    # Test 1: Árbol balanceado retorna True
    print("🧪 Test 1: Árbol balanceado")
    root = None
    for val in [20, 10, 30]:               # Insertar valores para crear árbol balanceado
        root = avl.insert(root, val)
    result1 = avl.is_avl_balanced(root)
    print(f"   Resultado: {result1} (Esperado: True) {'✅' if result1 == True else '❌'}")
    
    # Test 2: Árbol manualmente desbalanceado retorna False
    print("\n🧪 Test 2: Árbol desbalanceado manualmente")
    unbalanced = AVLNode(10)               # Crear árbol desbalanceado manualmente
    unbalanced.right = AVLNode(20)         # Solo hijos derechos (como una lista)
    unbalanced.right.right = AVLNode(30)
    result2 = avl.is_avl_balanced(unbalanced)
    print(f"   Resultado: {result2} (Esperado: False) {'✅' if result2 == False else '❌'}")
    
    # Test 3: Árbol vacío retorna True
    print("\n🧪 Test 3: Árbol vacío")
    result3 = avl.is_avl_balanced(None)
    print(f"   Resultado: {result3} (Esperado: True) {'✅' if result3 == True else '❌'}")
    
    # Test 4: Árbol con desbalance profundo retorna False
    print("\n🧪 Test 4: Árbol con desbalance profundo")
    deep_unbalanced = AVLNode(1)           # Crear una cadena larga hacia la derecha
    current = deep_unbalanced
    for i in range(2, 6):                  # Agregar nodos 2, 3, 4, 5
        current.right = AVLNode(i)
        current = current.right
    result4 = avl.is_avl_balanced(deep_unbalanced)
    print(f"   Resultado: {result4} (Esperado: False) {'✅' if result4 == False else '❌'}")
    
    # Test 5: Árbol que cumple todas las reglas AVL retorna True
    print("\n🧪 Test 5: Árbol AVL válido complejo")
    root_complex = None
    for val in [50, 25, 75, 10, 30, 60, 80, 5, 15]:  # Insertar múltiples valores
        root_complex = avl.insert(root_complex, val)
    result5 = avl.is_avl_balanced(root_complex)
    print(f"   Resultado: {result5} (Esperado: True) {'✅' if result5 == True else '❌'}")
    
    # Resumen de resultados
    print(f"\n📊 Resumen: {sum([result1, not result2, result3, not result4, result5])}/5 tests pasaron")

# 🚀 Ejecutar todas las pruebas
if __name__ == "__main__":
    print("🌳 Iniciando verificador de balance AVL...")
    test_is_avl_balanced()