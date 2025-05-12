# 🌳 Definición de Clase de Árbol Genérico
class GenericTreeNode:
    """
    Representa un nodo en un árbol genérico con múltiples hijos.
    
    Atributos:
    ----------
    value : any
        Valor almacenado en el nodo
    children : list
        Lista de nodos hijos
    """
    def __init__(self, value):
        """
        Inicializa un nodo del árbol.
        
        Parámetros:
        -----------
        value : any
            Valor a almacenar en el nodo
        """
        self.value = value
        self.children = []
    
    def add_child(self, child):
        """
        Agrega un nodo hijo al nodo actual.
        
        Parámetros:
        -----------
        child : GenericTreeNode
            Nodo hijo a agregar
        """
        self.children.append(child)
    
    def __str__(self, level=0):
        """
        Representación en cadena del árbol para visualización.
        
        Parámetros:
        -----------
        level : int, opcional
            Nivel de profundidad para impresión indentada
        
        Retorna:
        --------
        str
            Representación visual del árbol
        """
        # 🖨️ Impresión con sangría para mostrar estructura jerárquica
        ret = "\t" * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# 📏 Función Principal: Calcular Altura del Árbol
def tree_height(root):
    """
    Calcula la altura de un árbol genérico de manera recursiva.
    
    Parámetros:
    -----------
    root : GenericTreeNode
        Raíz del árbol
    
    Retorna:
    --------
    int
        Altura del árbol
    
    Estrategia:
    -----------
    1. Si el árbol está vacío, retorna 0
    2. Si no tiene hijos, retorna 1
    3. Encuentra la máxima altura entre todos los subárboles
    4. Retorna 1 (nodo actual) + máxima altura de subárboles
    """
    # 🚦 Caso base: árbol vacío
    if root is None:
        return 0
    
    # 🍃 Caso base: nodo hoja (sin hijos)
    if not root.children:
        return 1
    
    # 📊 Calcular altura máxima entre todos los hijos
    max_child_height = 0
    for child in root.children:
        # Recursivamente encontrar altura de cada subárbol
        child_height = tree_height(child)
        max_child_height = max(max_child_height, child_height)
    
    # 🏆 Retornar 1 (nodo actual) + altura máxima de subárboles
    return 1 + max_child_height

# 🧪 Función de Pruebas Detallada
def test_tree_height():
    """
    Batería de pruebas para verificar la función tree_height.
    Cubre diversos escenarios de estructura de árbol.
    """
    # 📊 Casos de prueba
    
    # 🌱 Caso 1: Árbol Vacío
    print("🌳 Prueba 1: Árbol Vacío")
    empty_tree = None
    print(f"   Altura: {tree_height(empty_tree)}")
    print("   Esperado: 0\n")
    
    # 🌿 Caso 2: Árbol de Un Solo Nodo
    print("🌳 Prueba 2: Árbol de Un Nodo")
    single_node = GenericTreeNode('Raíz')
    print("   Estructura:")
    print(single_node)
    print(f"   Altura: {tree_height(single_node)}")
    print("   Esperado: 1\n")
    
    # 🌲 Caso 3: Árbol Lineal
    print("🌳 Prueba 3: Árbol Lineal")
    linear_tree = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    
    linear_tree.add_child(b)
    b.add_child(c)
    c.add_child(d)
    
    print("   Estructura:")
    print(linear_tree)
    print(f"   Altura: {tree_height(linear_tree)}")
    print("   Esperado: 4\n")
    
    # 🌳 Caso 4: Árbol Balanceado
    print("🌳 Prueba 4: Árbol Balanceado")
    balanced_tree = GenericTreeNode('Raíz')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    
    # Primer nivel de hijos
    balanced_tree.add_child(b)
    balanced_tree.add_child(c)
    balanced_tree.add_child(d)
    
    # Segundo nivel de hijos
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    
    b.add_child(e)
    b.add_child(f)
    b.add_child(g)
    
    print("   Estructura:")
    print(balanced_tree)
    print(f"   Altura: {tree_height(balanced_tree)}")
    print("   Esperado: 3\n")
    
    # 🌴 Caso 5: Árbol No Balanceado
    print("🌳 Prueba 5: Árbol No Balanceado")
    unbalanced_tree = GenericTreeNode('Raíz')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    
    unbalanced_tree.add_child(b)
    b.add_child(c)
    c.add_child(d)
    d.add_child(e)
    e.add_child(f)
    
    print("   Estructura:")
    print(unbalanced_tree)
    print(f"   Altura: {tree_height(unbalanced_tree)}")
    print("   Esperado: 5\n")

# 🎓 Explicación Didáctica
def explain_tree_height():
    """
    Explicación detallada del algoritmo de cálculo de altura de árbol.
    """
    print("🧠 Explicación Detallada: Cálculo de Altura de Árbol\n")
    
    print("📝 Pasos del Algoritmo:")
    print("1. Si el árbol está vacío, la altura es 0")
    print("2. Si el nodo no tiene hijos, la altura es 1")
    print("3. Para nodos con hijos:")
    print("   a. Calcular la altura de cada subárbol hijo")
    print("   b. Encontrar la altura máxima entre los subárboles")
    print("   c. Sumar 1 (por el nodo actual) a la altura máxima\n")
    
    print("🔍 Ejemplo de Recursividad:")
    print("Consideremos un árbol:")
    print("       A")
    print("     / | \\")
    print("    B  C  D")
    print("   /|\\    |")
    print("  E F G   H\n")
    
    print("Proceso de Cálculo de Altura:")
    print("1. Nodos E, F, G, H: altura 1 (no tienen hijos)")
    print("2. Nodo B: 1 + max(altura de E, F, G) = 2")
    print("3. Nodos C, D: altura 1")
    print("4. Nodo raíz A: 1 + max(altura de B, C, D) = 3\n")

# Descomentar para ejecutar
test_tree_height()
explain_tree_height()
