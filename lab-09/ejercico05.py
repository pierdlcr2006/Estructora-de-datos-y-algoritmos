# -----------------------------------------------------
# 🌲 Simplificador de Árboles de Expresión Matemática 🌲
# -----------------------------------------------------
# Descripción: Este programa implementa un simplificador
# de expresiones matemáticas representadas como árboles binarios.

    import colorama
    from colorama import Fore, Style, Back
    import time
    import os
    from typing import Optional, Union, Tuple
    import math
    
    # Inicializar colorama (necesario para Windows)
    colorama.init(autoreset=True)
    
    # -------------------------
    # Nodo para árbol de expresión
    # -------------------------
    
    class ExpressionNode:
        """
        Representa un nodo en el árbol de expresión matemática.
        
        Atributos:
        ----------
        value : str
            Valor del nodo (operador, número o variable)
        left : ExpressionNode o None
            Referencia al hijo izquierdo
        right : ExpressionNode o None
            Referencia al hijo derecho
        """
        def __init__(self, value: str):
            self.value = value
            self.left = None
            self.right = None
        
        def __str__(self) -> str:
            """Representación de string para depuración"""
            return f"Node({self.value})"
        
        def is_operator(self) -> bool:
            """Verifica si el nodo es un operador"""
            return self.value in "+-*/^"
        
        def is_leaf(self) -> bool:
            """Verifica si el nodo es una hoja (no tiene hijos)"""
            return self.left is None and self.right is None
    
    
    # -------------------------
    # Árbol de expresión
    # -------------------------
    
    class ExpressionTree:
        """
        Implementación de árbol de expresión matemática con capacidad
        de simplificación automática de subexpresiones constantes.
        """
        
        def __init__(self, root=None):
            self.root = root
        
        @staticmethod
        def is_number(s: str) -> bool:
            """
            Verifica si una cadena representa un número.
            
            Parámetros:
            -----------
            s : str
                Cadena a verificar
                
            Retorna:
            --------
            bool
                True si es número, False en caso contrario
            """
            try:
                float(s)
                return True
            except (ValueError, TypeError):
                return False
        
        @staticmethod
        def evaluate_operator(op: str, left_val: str, right_val: str) -> Optional[str]:
            """
            Evalúa una operación matemática entre dos valores.
            
            Parámetros:
            -----------
            op : str
                Operador matemático ('+', '-', '*', '/', '^')
            left_val : str
                Valor izquierdo (debe ser convertible a número)
            right_val : str
                Valor derecho (debe ser convertible a número)
                
            Retorna:
            --------
            str o None
                Resultado de la operación como string o None si hay error
            """
            try:
                left_num = float(left_val)
                right_num = float(right_val)
                
                if op == '+':
                    result = left_num + right_num
                elif op == '-':
                    result = left_num - right_num
                elif op == '*':
                    result = left_num * right_num
                elif op == '/':
                    # Evitar división por cero
                    if right_num == 0:
                        return None
                    result = left_num / right_num
                elif op == '^':
                    result = left_num ** right_num
                else:
                    return None
                    
                # Convertir enteros exactos a enteros para mejor visualización
                if result == int(result):
                    return str(int(result))
                return str(result)
            except (ValueError, TypeError):
                return None
        
        def simplify(self) -> Optional[str]:
            """
            Simplifica el árbol de expresión evaluando las subexpresiones constantes.
            
            Retorna:
            --------
            str o None
                Valor del nodo raíz después de la simplificación, o None si el árbol está vacío
            """
            
            def simplify_node(node: Optional[ExpressionNode]) -> Optional[ExpressionNode]:
                """Función recursiva para simplificar un nodo y sus subárboles"""
                if node is None:
                    return None
                
                # Si es hoja (sin hijos), retornar nodo tal cual
                if node.is_leaf():
                    return node
                
                # Recursivamente simplificar hijos
                node.left = simplify_node(node.left)
                node.right = simplify_node(node.right)
                
                # Si ambos hijos son números, evaluar la operación
                if (node.left and node.right and
                    self.is_number(node.left.value) and 
                    self.is_number(node.right.value)):
                    
                    result = self.evaluate_operator(node.value, node.left.value, node.right.value)
                    if result is not None:
                        # Reemplazar nodo actual por nodo hoja con resultado
                        node.value = result
                        node.left = None
                        node.right = None
                
                # Si no se puede simplificar, dejar el nodo tal cual
                return node
            
            self.root = simplify_node(self.root)
            return self.root.value if self.root else None
        
        def to_string(self) -> str:
            """
            Genera una representación de cadena de la expresión matemática.
            
            Retorna:
            --------
            str
                Expresión matemática en notación infija con paréntesis
            """
            
            def node_to_string(node: Optional[ExpressionNode]) -> str:
                """Función recursiva para convertir un nodo a string"""
                if node is None:
                    return ""
                
                if node.is_leaf():
                    return node.value
                
                left_str = node_to_string(node.left)
                right_str = node_to_string(node.right)
                
                # Agregar paréntesis para claridad
                return f"({left_str} {node.value} {right_str})"
            
            return node_to_string(self.root)
        
        def visualize(self) -> str:
            """
            Genera una representación visual del árbol para consola.
            
            Retorna:
            --------
            str
                Representación visual del árbol con formato
            """
            
            def build_tree_str(node: Optional[ExpressionNode], prefix: str = "", is_left: bool = True) -> str:
                if node is None:
                    return ""
                
                result = ""
                
                # Agregar hijo derecho
                if node.right:
                    new_prefix = prefix + ("│   " if is_left else "    ")
                    result += build_tree_str(node.right, new_prefix, False)
                
                # Agregar nodo actual
                connector = prefix + ("└── " if is_left else "┌── ")
                
                # Colorear según tipo de nodo
                if node.is_operator():
                    node_str = f"{Fore.YELLOW}{node.value}{Style.RESET_ALL}"
                elif self.is_number(node.value):
                    node_str = f"{Fore.CYAN}{node.value}{Style.RESET_ALL}"
                else:
                    node_str = f"{Fore.GREEN}{node.value}{Style.RESET_ALL}"
                    
                result += connector + node_str + "\n"
                
                # Agregar hijo izquierdo
                if node.left:
                    new_prefix = prefix + ("    " if is_left else "│   ")
                    result += build_tree_str(node.left, new_prefix, True)
                
                return result
            
            if self.root is None:
                return f"{Fore.RED}(Árbol vacío){Style.RESET_ALL}"
            
            return build_tree_str(self.root, "", True)
    
    
    # -------------------------
    # Funciones de visualización
    # -------------------------
    
    def print_header(text: str) -> None:
        """
        Imprime un encabezado formateado para las pruebas.
        
        Parámetros:
        -----------
        text : str
            Texto del encabezado
        """
        width = 70
        print("\n" + "═" * width)
        print(f"{Fore.GREEN}{Style.BRIGHT}{text.center(width)}{Style.RESET_ALL}")
        print("═" * width)
    
    
    def print_expression_info(tree: ExpressionTree, title: str, expected: str, delay: float = 0.3) -> None:
        """
        Imprime información detallada de una expresión y su simplificación.
        
        Parámetros:
        -----------
        tree : ExpressionTree
            Árbol de expresión a visualizar
        title : str
            Título de la prueba
        expected : str
            Valor esperado después de la simplificación
        delay : float
            Retraso para efectos de animación
        """
        print_header(title)
        time.sleep(delay)
        
        # Mostrar expresión original
        print(f"\n{Fore.YELLOW}▶ Expresión original:{Style.RESET_ALL}")
        original_expr = tree.to_string()
        print(f"   {Fore.WHITE}{original_expr}{Style.RESET_ALL}")
        time.sleep(delay)
        
        # Mostrar árbol antes de simplificar
        print(f"\n{Fore.YELLOW}▶ Árbol antes de simplificar:{Style.RESET_ALL}")
        print(tree.visualize())
        time.sleep(delay)
        
        # Simplificar y mostrar resultado
        print(f"\n{Fore.YELLOW}▶ Simplificando...{Style.RESET_ALL}")
        time.sleep(delay * 2)
        result = tree.simplify()
        
        # Mostrar árbol después de simplificar
        print(f"\n{Fore.YELLOW}▶ Árbol después de simplificar:{Style.RESET_ALL}")
        print(tree.visualize())
        time.sleep(delay)
        
        # Mostrar expresión resultante
        print(f"\n{Fore.YELLOW}▶ Expresión simplificada:{Style.RESET_ALL}")
        simplified_expr = tree.to_string()
        print(f"   {Fore.WHITE}{simplified_expr}{Style.RESET_ALL}")
        time.sleep(delay)
        
        # Verificar resultado
        if isinstance(expected, tuple):
            # Para casos especiales que verifican múltiples valores
            expected_root, expected_child = expected
            correct = (result == expected_root)
            if tree.root and tree.root.right:
                child_correct = (tree.root.right.value == expected_child)
                correct = correct and child_correct
                print(f"\n{Fore.YELLOW}▶ Verificación:{Style.RESET_ALL}")
                print(f"   Valor raíz esperado:     {Fore.MAGENTA}{expected_root}{Style.RESET_ALL}")
                print(f"   Valor raíz obtenido:     {Fore.MAGENTA}{result}{Style.RESET_ALL}")
                print(f"   Valor hijo der esperado: {Fore.MAGENTA}{expected_child}{Style.RESET_ALL}")
                print(f"   Valor hijo der obtenido: {Fore.MAGENTA}{tree.root.right.value}{Style.RESET_ALL}")
        else:
            # Caso normal
            correct = (result == expected)
            print(f"\n{Fore.YELLOW}▶ Verificación:{Style.RESET_ALL}")
            print(f"   Valor esperado:  {Fore.MAGENTA}{expected}{Style.RESET_ALL}")
            print(f"   Valor obtenido:  {Fore.MAGENTA}{result}{Style.RESET_ALL}")
        
        # Mostrar resultado final
        if correct:
            print(f"\n   {Back.GREEN}{Fore.BLACK} ✓ CORRECTO {Style.RESET_ALL}")
        else:
            print(f"\n   {Back.RED}{Fore.WHITE} ✗ INCORRECTO {Style.RESET_ALL}")
        
        print("\n" + "-" * 70)
    
    
    # -------------------------
    # Casos de prueba
    # -------------------------
    
    def test_expression_tree_simplification() -> None:
        """
        Batería de pruebas para la simplificación de árboles de expresión.
        Prueba varios escenarios desde simples hasta complejos.
        """
        # Limpiar pantalla antes de comenzar
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"\n{Back.BLUE}{Fore.WHITE}{Style.BRIGHT} 🧮 SIMPLIFICADOR DE ÁRBOLES DE EXPRESIÓN MATEMÁTICA 🧮 {Style.RESET_ALL}\n")
        time.sleep(1)
        
        # Caso 1: (2 + 3)
        const_tree = ExpressionTree()
        const_tree.root = ExpressionNode('+')
        const_tree.root.left = ExpressionNode('2')
        const_tree.root.right = ExpressionNode('3')
        
        # Caso 2: (2 + 3) * x
        partial_tree = ExpressionTree()
        partial_tree.root = ExpressionNode('*')
        add_node = ExpressionNode('+')
        add_node.left = ExpressionNode('2')
        add_node.right = ExpressionNode('3')
        partial_tree.root.left = add_node
        partial_tree.root.right = ExpressionNode('x')
        
        # Caso 3: x + y (sin simplificación)
        no_simp_tree = ExpressionTree()
        no_simp_tree.root = ExpressionNode('+')
        no_simp_tree.root.left = ExpressionNode('x')
        no_simp_tree.root.right = ExpressionNode('y')
        
        # Caso 4: ((2 * 3) + (8 / 4))
        complex_tree = ExpressionTree()
        complex_tree.root = ExpressionNode('+')
        mult_node = ExpressionNode('*')
        div_node = ExpressionNode('/')
        mult_node.left = ExpressionNode('2')
        mult_node.right = ExpressionNode('3')
        div_node.left = ExpressionNode('8')
        div_node.right = ExpressionNode('4')
        complex_tree.root.left = mult_node
        complex_tree.root.right = div_node
        
        # Caso 5: x * (6 / 2)
        mixed_tree = ExpressionTree()
        mixed_tree.root = ExpressionNode('*')
        div_node2 = ExpressionNode('/')
        div_node2.left = ExpressionNode('6')
        div_node2.right = ExpressionNode('2')
        mixed_tree.root.left = ExpressionNode('x')
        mixed_tree.root.right = div_node2
        
        tests = [
            (const_tree, "Expresión Constante Simple: (2 + 3)", '5'),
            (partial_tree, "Expresión Parcialmente Simplificable: (2 + 3) * x", '*'),
            (no_simp_tree, "Expresión Sin Simplificación: x + y", '+'),
            (complex_tree, "Expresión Compleja: ((2 * 3) + (8 / 4))", '8'),
            (mixed_tree, "Expresión Mixta: x * (6 / 2)", ('*', '3'))
        ]
        
        for tree, title, expected in tests:
            print_expression_info(tree, title, expected)
        
        print(f"\n{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} ✅ Todas las pruebas completadas {Style.RESET_ALL}\n")
    
    
    # Ejecutar las pruebas si este archivo es el principal
    if __name__ == "__main__":
        test_expression_tree_simplification()

