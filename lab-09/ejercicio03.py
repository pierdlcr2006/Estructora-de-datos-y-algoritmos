# ------------------------- #
# ALTURA DE ÁRBOL GENÉRICO
# ------------------------- #
# Implementación para calcular la altura máxima en un árbol 
# donde cada nodo puede tener múltiples hijos (árbol genérico)

# ------------------------- #
# DEFINICIÓN DE CLASES
# ------------------------- #
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
        # Impresión con sangría para mostrar estructura jerárquica
        ret = "\t" * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def to_ascii_tree(self, prefix="", is_last=True, is_root=True):
        """
        Genera una representación ASCII del árbol más visual.
        
        Parámetros:
        -----------
        prefix : str
            Prefijo para la línea actual
        is_last : bool
            Indica si el nodo es el último hijo de su padre
        is_root : bool
            Indica si el nodo es la raíz del árbol
        
        Retorna:
        --------
        str
            Representación ASCII del árbol
        """
        result = ""
        
        # Determinar el prefijo para el nodo actual
        if not is_root:
            result += prefix + ("└── " if is_last else "├── ") + str(self.value) + "\n"
        else:
            result += prefix + str(self.value) + "\n"
        
        # Prefijo para los hijos
        child_prefix = prefix + ("    " if is_last else "│   ")
        
        # Procesar los hijos
        child_count = len(self.children)
        for i, child in enumerate(self.children):
            is_last_child = i == child_count - 1
            result += child.to_ascii_tree(child_prefix, is_last_child, False)
            
        return result

# ------------------------- #
# ALGORITMO DE ALTURA
# ------------------------- #
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
    # Caso base: árbol vacío
    if root is None:
        return 0
    
    # Caso base: nodo hoja (sin hijos)
    if not root.children:
        return 1
    
    # Calcular altura máxima entre todos los hijos
    max_child_height = 0
    for child in root.children:
        # Recursivamente encontrar altura de cada subárbol
        child_height = tree_height(child)
        max_child_height = max(max_child_height, child_height)
    
    # Retornar 1 (nodo actual) + altura máxima de subárboles
    return 1 + max_child_height

# ------------------------- #
# FUNCIONES DE VISUALIZACIÓN
# ------------------------- #
def print_path_to_deepest_node(root, current_path=None, max_path=None):
    """
    Encuentra y retorna el camino más largo desde la raíz hasta una hoja.
    
    Parámetros:
    -----------
    root : GenericTreeNode
        Nodo raíz del árbol o subárbol
    current_path : list, opcional
        Camino acumulado hasta el nodo actual
    max_path : list, opcional
        Camino más largo encontrado hasta ahora
    
    Retorna:
    --------
    list
        Lista de valores que representan el camino más largo
    """
    if root is None:
        return []
    
    # Inicializamos las listas si es la primera llamada
    if current_path is None:
        current_path = []
    if max_path is None:
        max_path = []
    
    # Agregamos el nodo actual al camino
    current_path = current_path + [root.value]
    
    # Si es una hoja, comprobamos si es el camino más largo
    if not root.children:
        if len(current_path) > len(max_path):
            return current_path
        else:
            return max_path
    
    # Recursivamente buscamos el camino más largo entre todos los hijos
    for child in root.children:
        max_path = print_path_to_deepest_node(child, current_path, max_path)
    
    return max_path

# ------------------------- #
# BATERÍA DE PRUEBAS
# ------------------------- #
def test_tree_height():
    """
    Batería de pruebas para verificar la función tree_height.
    Cubre diversos escenarios de estructura de árbol.
    """
    # Casos de prueba con diferentes configuraciones de árboles
    test_cases = [
        {
            'name': 'Árbol Vacío',
            'tree': None,
            'expected': 0,
            'description': 'Un árbol sin nodos (None)'
        },
        {
            'name': 'Árbol de Un Nodo',
            'tree': GenericTreeNode('Raíz'),
            'expected': 1,
            'description': 'Un solo nodo sin hijos'
        },
        {
            'name': 'Árbol Lineal',
            'tree': _create_linear_tree(),
            'expected': 4,
            'description': 'Árbol donde cada nodo tiene exactamente un hijo'
        },
        {
            'name': 'Árbol Balanceado',
            'tree': _create_balanced_tree(),
            'expected': 3,
            'description': 'Árbol donde los nodos tienen múltiples hijos a la misma profundidad'
        },
        {
            'name': 'Árbol No Balanceado',
            'tree': _create_unbalanced_tree(),
            'expected': 6,
            'description': 'Árbol con ramas de diferentes longitudes'
        }
    ]
    
    # Contadores para el resumen final
    tests_totales = len(test_cases)
    tests_pasados = 0
    
    # Encabezado de la tabla de resultados
    print("\n" + "=" * 80)
    print(f"{'🌳 PRUEBAS DE CÁLCULO DE ALTURA EN ÁRBOLES GENÉRICOS':^80}")
    print("=" * 80)
    
    # Ejecutar cada caso de prueba
    for i, caso in enumerate(test_cases, 1):
        # Calcular altura
        altura = tree_height(caso['tree'])
        es_correcto = altura == caso['expected']
        
        if es_correcto:
            tests_pasados += 1
        
        # Separador entre pruebas
        print(f"\n{'-' * 80}")
        
        # Información de la prueba
        print(f"🧩 PRUEBA {i}: {caso['name']}")
        print(f"{'-' * 80}")
        
        # Descripción del caso
        print(f"📝 Descripción: {caso['description']}")
        
        # Mostrar altura calculada y esperada
        print(f"🧮 Altura calculada: {altura}")
        print(f"🎯 Altura esperada:  {caso['expected']}")
        
        # Indicador de éxito o fracaso
        estado = "✅ CORRECTO" if es_correcto else "❌ INCORRECTO"
        print(f"\n{estado:^80}")
        
        # Mostrar estructura del árbol si no es vacío
        if caso['tree'] is not None:
            print(f"\n📊 Estructura del árbol:")
            print(f"{'-' * 40}")
            print(caso['tree'].to_ascii_tree())
            
            # Mostrar camino más largo
            longest_path = print_path_to_deepest_node(caso['tree'])
            print(f"\n🛤️  Camino más largo: {' -> '.join(map(str, longest_path))}")
            print(f"📏 Longitud del camino: {len(longest_path)} nodos")
    
    # Resumen final
    print("\n" + "=" * 80)
    print(f"{'RESUMEN DE RESULTADOS':^80}")
    print("=" * 80)
    print(f"Total de pruebas:     {tests_totales}")
    print(f"Pruebas correctas:    {tests_pasados}")
    print(f"Porcentaje de éxito:  {(tests_pasados/tests_totales) * 100:.2f}%")
    print("=" * 80 + "\n")

# ------------------------- #
# ÁRBOLES DE PRUEBA
# ------------------------- #
def _create_linear_tree():
    """Crea un árbol lineal para pruebas."""
    linear_tree = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    
    linear_tree.add_child(b)
    b.add_child(c)
    c.add_child(d)
    
    return linear_tree

def _create_balanced_tree():
    """Crea un árbol balanceado para pruebas."""
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
    c.add_child(g)
    
    return balanced_tree

def _create_unbalanced_tree():
    """Crea un árbol no balanceado para pruebas."""
    unbalanced_tree = GenericTreeNode('Raíz')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    
    unbalanced_tree.add_child(b)
    unbalanced_tree.add_child(c)
    
    b.add_child(d)
    
    d.add_child(e)
    
    e.add_child(f)
    
    f.add_child(g)
    
    return unbalanced_tree

# ------------------------- #
# EXPLICACIÓN DIDÁCTICA
# ------------------------- #
def explain_tree_height():
    """
    Explicación detallada del algoritmo de cálculo de altura de árbol.
    """
    print("\n" + "=" * 80)
    print(f"{'🧠 EXPLICACIÓN DETALLADA: CÁLCULO DE ALTURA DE ÁRBOL':^80}")
    print("=" * 80 + "\n")
    
    print("📝 Pasos del Algoritmo:")
    print("1. Si el árbol está vacío, la altura es 0")
    print("2. Si el nodo no tiene hijos (es una hoja), la altura es 1")
    print("3. Para nodos con hijos:")
    print("   a. Calcular recursivamente la altura de cada subárbol hijo")
    print("   b. Encontrar la altura máxima entre los subárboles")
    print("   c. Sumar 1 (por el nodo actual) a la altura máxima\n")
    
    print("🔍 Ejemplo Visual de Recursividad:")
    
    # Crear un árbol de ejemplo para la explicación
    root = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    h = GenericTreeNode('H')
    
    root.add_child(b)
    root.add_child(c)
    root.add_child(d)
    
    b.add_child(e)
    b.add_child(f)
    b.add_child(g)
    
    d.add_child(h)
    
    # Mostrar el árbol
    print("Estructura del árbol de ejemplo:")
    print(root.to_ascii_tree())
    
    print("\nProceso de Cálculo de Altura:")
    print("1. Nodos E, F, G, H (hojas): altura = 1")
    print("2. Nodo B: altura = 1 + max(altura de E, F, G) = 1 + 1 = 2")
    print("3. Nodo C (no tiene hijos): altura = 1")
    print("4. Nodo D: altura = 1 + altura de H = 1 + 1 = 2")
    print("5. Nodo raíz A: altura = 1 + max(altura de B, C, D) = 1 + max(2, 1, 2) = 1 + 2 = 3")
    
    print("\n🎓 Conceptos Clave:")
    print("• La altura de un árbol es la longitud del camino más largo desde la raíz hasta una hoja")
    print("• El camino se mide contando el número de nodos (no de aristas)")
    print("• La recursividad simplifica enormemente el algoritmo")
    print("• La función max() es esencial para encontrar la rama más profunda\n")
    
    print("🔄 Complejidad del Algoritmo:")
    print("• Tiempo: O(n) donde n es el número de nodos (visitamos cada nodo exactamente una vez)")
    print("• Espacio: O(h) donde h es la altura del árbol (máxima profundidad de recursión)")
    
    print("\n💡 Aplicaciones Prácticas:")
    print("• Análisis de rendimiento de estructuras de datos en árbol")
    print("• Optimización de consultas en bases de datos jerárquicas")
    print("• Cálculo de profundidad en árboles de decisión")
    print("• Análisis de estructuras jerárquicas como organigramas o taxonomías")
    
    print("\n" + "=" * 80)

# Ejecutar las pruebas y la explicación cuando se ejecuta el script directamente
if __name__ == "__main__":
    test_tree_height()
    explain_tree_height()