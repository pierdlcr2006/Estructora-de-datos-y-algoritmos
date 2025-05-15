
# -------------------------------
# Árbol Genérico: Buscador de Hojas
# -------------------------------
# Descripción: Este programa define un árbol genérico y funciones para
# encontrar todos los nodos hoja (nodos sin hijos) dentro del árbol.

import colorama
from colorama import Fore, Style, Back
import time
import os

# Inicializar colorama (necesario para Windows)
colorama.init(autoreset=True)

# -------------------------------
# Definición de la clase del nodo
# -------------------------------

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
        """
        Inicializa un nuevo nodo con el valor especificado.
        
        Parámetros:
        -----------
        value : any
            El valor a almacenar en este nodo
        """
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
        # Construcción de representación visual mejorada del árbol
        prefix = "│   " * (level - 1) + "├── " if level > 0 else ""
        result = prefix + f"{Fore.CYAN}{self.value}{Style.RESET_ALL}\n"
        
        # Agregar representaciones de los hijos con indentación y líneas conectoras
        for i, child in enumerate(self.children):
            is_last = i == len(self.children) - 1
            result += child.__str__(level + 1)
            
        return result


# -------------------------------
# Funciones para encontrar hojas
# -------------------------------

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
    # Caso base: árbol vacío
    if root is None:
        return []
    
    # Caso base: nodo hoja (sin hijos)
    if not root.children:
        return [root.value]
    
    # Recolectar hojas de todos los hijos
    leaves = []
    for child in root.children:
        leaves.extend(find_leaves(child))
    
    return leaves


# -------------------------------
# Funciones auxiliares para test
# -------------------------------

def _create_linear_tree():
    """
    Crea un árbol lineal para pruebas.
    
    Returns:
        Raíz de un árbol lineal con nodos A->B->C
    """
    linear_tree = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    linear_tree.add_child(b)
    b.add_child(c)
    return linear_tree


def _create_balanced_tree():
    """
    Crea un árbol balanceado para pruebas.
    
    Returns:
        Raíz de un árbol balanceado con varios nodos
    """
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
    
    return balanced_tree


def _create_complex_tree():
    """
    Crea un árbol complejo para pruebas.
    
    Returns:
        Raíz de un árbol complejo con estructura irregular
    """
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
    
    return complex_tree


# -------------------------------
# Funciones de visualización
# -------------------------------

def print_header(text):
    """
    Imprime un encabezado formateado para las pruebas.
    """
    width = 60
    print("\n" + "═" * width)
    print(f"{Fore.GREEN}{Style.BRIGHT}{text.center(width)}{Style.RESET_ALL}")
    print("═" * width)


def print_tree_info(title, tree, delay=0.5):
    """
    Imprime información del árbol con animación.
    
    Parámetros:
    -----------
    title : str
        Título de la prueba
    tree : GenericTreeNode
        Árbol a visualizar
    delay : float
        Retraso para efecto de animación
    """
    print_header(title)
    
    print(f"\n{Fore.YELLOW}▶ Estructura del árbol:{Style.RESET_ALL}")
    time.sleep(delay)
    
    if tree is None:
        print(f"{Fore.RED}   (Árbol vacío){Style.RESET_ALL}")
    else:
        print(tree)
    
    time.sleep(delay)
    
    leaves = find_leaves(tree)
    print(f"\n{Fore.YELLOW}▶ Nodos hoja encontrados:{Style.RESET_ALL}")
    time.sleep(delay)
    
    if not leaves:
        print(f"{Fore.RED}   (Ninguno){Style.RESET_ALL}")
    else:
        print(f"   {Fore.MAGENTA}{Style.BRIGHT}{leaves}{Style.RESET_ALL}")
    
    print("\n" + "-" * 60)


# -------------------------------
# Función principal de prueba
# -------------------------------

def test_find_leaves():
    """
    Batería de pruebas para encontrar nodos hoja con visualización mejorada.
    """
    # Limpiar pantalla antes de comenzar
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"\n{Back.BLUE}{Fore.WHITE}{Style.BRIGHT} 🍃 BUSCADOR DE NODOS HOJA EN ÁRBOLES GENÉRICOS 🍃 {Style.RESET_ALL}\n")
    time.sleep(1)
    
    # Caso 1: Árbol vacío
    print_tree_info("Prueba 1: Árbol Vacío", None)
    
    # Caso 2: Árbol de un solo nodo
    single_node = GenericTreeNode('A')
    print_tree_info("Prueba 2: Árbol de Un Nodo", single_node)
    
    # Caso 3: Árbol lineal
    linear_tree = _create_linear_tree()
    print_tree_info("Prueba 3: Árbol Lineal", linear_tree)
    
    # Caso 4: Árbol balanceado
    balanced_tree = _create_balanced_tree()
    print_tree_info("Prueba 4: Árbol Balanceado", balanced_tree)
    
    # Caso 5: Árbol complejo
    complex_tree = _create_complex_tree()
    print_tree_info("Prueba 5: Árbol Complejo", complex_tree)
    
    print(f"\n{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} ✅ Todas las pruebas completadas {Style.RESET_ALL}\n")


# Ejecutar las pruebas si este archivo es el principal
if __name__ == "__main__":
    test_find_leaves()
