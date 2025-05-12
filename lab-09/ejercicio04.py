# 🍃 Desafío 4: Encontrar Hojas en un Árbol Genérico
# Objetivo: Identificar y recolectar todos los nodos hoja de un árbol
# Características principales:
# - Recursividad para traversar el árbol
# - Identificación de nodos sin hijos
# - Recolección de valores de hojas

class GenericTreeNode:
    """
    Nodo para un árbol genérico con múltiples hijos.
    
    Atributos:
    ----------
    value : any
        Valor almacenado en el nodo
    children : list
        Lista de nodos hijos
    """
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        """
        Agrega un nodo hijo al árbol.
        
        Parámetros:
        -----------
        child : GenericTreeNode
            Nodo a agregar como hijo
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
            Representación en cadena del árbol
        """
        # 🌿 Construcción de representación visual del árbol
        ret = "\t" * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

def find_leaves(root):
    """
    Encuentra todos los nodos hoja en un árbol genérico.
    
    Parámetros:
    -----------
    root : GenericTreeNode
        Raíz del árbol
    
    Retorna:
    --------
    list
        Lista de valores de nodos hoja
    
    Notas:
    ------
    - Nodo hoja: nodo sin hijos
    - Retorna lista vacía para árbol vacío
    - Recursivamente busca hojas en todos los subárboles
    """
    # 🚦 Caso base: árbol vacío
    if root is None:
        return []
    
    # 🍃 Caso base: nodo hoja (sin hijos)
    if not root.children:
        return [root.value]
    
    # 🔍 Recolectar hojas de todos los hijos
    leaves = []
    for child in root.children:
        leaves.extend(find_leaves(child))
    
    return leaves

def test_find_leaves():
    """
    Batería de pruebas para encontrar nodos hoja.
    Prueba diversos escenarios de estructura de árbol.
    """
    # 🧪 Caso 1: Árbol vacío
    print("🌳 Prueba 1: Árbol Vacío")
    print(f"   Hojas: {find_leaves(None)}\n")
    
    # 🧪 Caso 2: Árbol de un solo nodo
    print("🌳 Prueba 2: Árbol de Un Nodo")
    single_node = GenericTreeNode('A')
    print("   Estructura:")
    print(single_node)
    print(f"   Hojas: {find_leaves(single_node)}\n")
    
    # 🧪 Caso 3: Árbol lineal
    print("🌳 Prueba 3: Árbol Lineal")
    linear_tree = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    linear_tree.add_child(b)
    b.add_child(c)
    print("   Estructura:")
    print(linear_tree)
    print(f"   Hojas: {find_leaves(linear_tree)}\n")
    
    # 🧪 Caso 4: Árbol balanceado
    print("🌳 Prueba 4: Árbol Balanceado")
    balanced_tree = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    
    balanced_tree.add_child(b)
    balanced_tree.add_child(c)
    balanced_tree.add_child(d)
    
    b.add_child(e)
    b.add_child(f)
    b.add_child(g)
    
    print("   Estructura:")
    print(balanced_tree)
    print(f"   Hojas: {find_leaves(balanced_tree)}\n")
    
    # 🧪 Caso 5: Árbol complejo
    print("🌳 Prueba 5: Árbol Complejo")
    complex_tree = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    h = GenericTreeNode('H')
    
    complex_tree.add_child(b)
    complex_tree.add_child(c)
    complex_tree.add_child(d)
    
    b.add_child(e)
    b.add_child(f)
    
    d.add_child(g)
    f.add_child(h)
    
    print("   Estructura:")
    print(complex_tree)
    print(f"   Hojas: {find_leaves(complex_tree)}\n")

# Descomentar para ejecutar pruebas
test_find_leaves()