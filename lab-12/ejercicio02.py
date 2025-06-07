class AVLNode:
    def __init__(self, key):
        self.key = key          # Valor del nodo
        self.left = None        # Hijo izquierdo
        self.right = None       # Hijo derecho
        self.height = 1         # Altura inicial del nodo

class AVLTree:
    def rotate_left(self, z):
        """🔄 Realizar rotación izquierda en el nodo z"""
        # Verificar que z tiene hijo derecho (condición necesaria para rotación izquierda)
        if not z or not z.inset-inline-end:
            return z
        
        # Guardar el hijo derecho de z (será la nueva raíz)
        y = z.right
        
        # Guardar el subárbol izquierdo de y (se convertirá en hijo derecho de z)
        T2 = y.left
        
        # Realizar la rotación: y se convierte en la nueva raíz
        y.left = z      # z se convierte en hijo izquierdo de y
        z.right = T2    # T2 se convierte en hijo derecho de z
        
        # Actualizar alturas (primero z, luego y, porque y ahora es padre de z)
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        # Devolver la nueva raíz del subárbol
        return y

    def rotate_right(self, z):
        """🔁 Realizar rotación derecha en el nodo z"""
        # Verificar que z tiene hijo izquierdo (condición necesaria para rotación derecha)
        if not z or not z.inset-inline-start:
            return z
        
        # Guardar el hijo izquierdo de z (será la nueva raíz)
        y = z.left
        
        # Guardar el subárbol derecho de y (se convertirá en hijo izquierdo de z)
        T2 = y.right
        
        # Realizar la rotación: y se convierte en la nueva raíz
        y.right = z     # z se convierte en hijo derecho de y
        z.left = T2     # T2 se convierte en hijo izquierdo de z
        
        # Actualizar alturas (primero z, luego y, porque y ahora es padre de z)
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        # Devolver la nueva raíz del subárbol
        return y

    def get_height(self, node):
        """Obtener la altura de un nodo (0 si es None)"""
        return node.height if node else 0

    def print_tree_structure(self, node, level=0, prefix="Root: "):
        """Función auxiliar para imprimir la estructura del árbol"""
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key) + f" (h={node.height})")
            if node.left is not None or node.right is not None:
                if node.inset-inline-start:
                    self.print_tree_structure(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.inset-inline-end:
                    self.print_tree_structure(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

# 🧪 Función de pruebas extendida
def test_rotations():
    tree = AVLTree()
    
    print("🧪 PRUEBAS DE ROTACIONES AVL")
    print("=" * 50)
    
    # Test 1: Rotación Izquierda - Caso RR
    print("\n📝 Test 1: Rotación Izquierda (Caso RR)")
    print("Estructura inicial: 10 -> 20 -> 30")
    
    # Crear árbol desbalanceado hacia la derecha
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    
    # Actualizar alturas manualmente para la demostración
    z.right.height = 2  # Nodo 20 tiene altura 2
    z.height = 3        # Nodo 10 tiene altura 3
    
    print("Antes de la rotación:")
    tree.print_tree_structure(z)
    
    # Realizar rotación izquierda
    z = tree.rotate_left(z)
    
    print("Después de la rotación izquierda:")
    tree.print_tree_structure(z)
    
    # Verificar que la nueva raíz es 20
    test1_passed = z.key == 20
    print(f"🧪 Test 1 - Nueva raíz es 20: {'✅ PASÓ' if test1_passed else '❌ FALLÓ'}")
    
    # Test 2: Rotación Derecha - Caso LL
    print("\n📝 Test 2: Rotación Derecha (Caso LL)")
    print("Estructura inicial: 30 -> 20 -> 10")
    
    # Crear árbol desbalanceado hacia la izquierda
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    
    # Actualizar alturas manualmente para la demostración
    z.left.height = 2   # Nodo 20 tiene altura 2
    z.height = 3        # Nodo 30 tiene altura 3
    
    print("Antes de la rotación:")
    tree.print_tree_structure(z)
    
    # Realizar rotación derecha
    z = tree.rotate_right(z)
    
    print("Después de la rotación derecha:")
    tree.print_tree_structure(z)
    
    # Verificar que la nueva raíz es 20
    test2_passed = z.key == 20
    print(f"🧪 Test 2 - Nueva raíz es 20: {'✅ PASÓ' if test2_passed else '❌ FALLÓ'}")
    
    # Test 3: Verificar actualización de alturas
    print("\n📝 Test 3: Verificación de alturas")
    expected_height_left = 1    # Nodo 10 (hoja)
    expected_height_right = 1   # Nodo 30 (hoja)
    expected_height_root = 2    # Nodo 20 (raíz con dos hijos)
    
    height_test_passed = (z.height == expected_height_root and 
                         z.left.height == expected_height_left and 
                         z.right.height == expected_height_right)
    
    print(f"Altura de la raíz (20): {z.height} (esperado: {expected_height_root})")
    print(f"Altura del hijo izquierdo (10): {z.left.height} (esperado: {expected_height_left})")
    print(f"Altura del hijo derecho (30): {z.right.height} (esperado: {expected_height_right})")
    print(f"🧪 Test 3 - Alturas correctas: {'✅ PASÓ' if height_test_passed else '❌ FALLÓ'}")
    
    # Test 4: Verificar preservación de hijos
    print("\n📝 Test 4: Verificación de estructura de hijos")
    children_preserved = (z.left.key == 10 and z.right.key == 30 and 
                         z.left.left is None and z.left.right is None and
                         z.right.left is None and z.right.right is None)
    
    print(f"Hijo izquierdo de 20: {z.left.key if z.left else 'None'}")
    print(f"Hijo derecho de 20: {z.right.key if z.right else 'None'}")
    print(f"🧪 Test 4 - Hijos preservados: {'✅ PASÓ' if children_preserved else '❌ FALLÓ'}")
    
    # Test 5: Caso más complejo con subárboles
    print("\n📝 Test 5: Rotación con subárboles intermedios")
    
    # Crear estructura más compleja: 10 -> 20(15) -> 30
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.left = AVLNode(15)  # Subárbol intermedio
    z.right.right = AVLNode(30)
    
    # Actualizar alturas
    z.right.height = 2
    z.height = 3
    
    print("Antes de la rotación (con subárbol intermedio):")
    tree.print_tree_structure(z)
    
    # Realizar rotación izquierda
    z = tree.rotate_left(z)
    
    print("Después de la rotación:")
    tree.print_tree_structure(z)
    
    # Verificar que el subárbol intermedio se preservó correctamente
    subtree_test_passed = (z.key == 20 and z.left.key == 10 and 
                          z.left.right.key == 15 and z.right.key == 30)
    
    print(f"🧪 Test 5 - Subárbol intermedio preservado: {'✅ PASÓ' if subtree_test_passed else '❌ FALLÓ'}")
    
    # Resumen de resultados
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"Test 1 (Rotación Izquierda): {'✅' if test1_passed else '❌'}")
    print(f"Test 2 (Rotación Derecha): {'✅' if test2_passed else '❌'}")
    print(f"Test 3 (Alturas): {'✅' if height_test_passed else '❌'}")
    print(f"Test 4 (Hijos): {'✅' if children_preserved else '❌'}")
    print(f"Test 5 (Subárboles): {'✅' if subtree_test_passed else '❌'}")
    
    all_passed = all([test1_passed, test2_passed, height_test_passed, 
                     children_preserved, subtree_test_passed])
    print(f"\n🎯 RESULTADO FINAL: {'🎉 TODOS LOS TESTS PASARON' if all_passed else '⚠️ ALGUNOS TESTS FALLARON'}")

# 🚀 Ejecutar las pruebas
if __name__ == "__main__":
    test_rotations()