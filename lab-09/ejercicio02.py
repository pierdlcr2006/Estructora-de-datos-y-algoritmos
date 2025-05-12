# 🌳 Desafío 2: Construcción de Árbol de Expresión desde Infijo
# Objetivo: Crear un árbol de expresión a partir de una expresión matemática en notación infija
# Características principales:
# - Conversión de infijo a postfijo
# - Construcción de árbol usando método de pila
# - Manejo de expresiones anidadas

class ExpressionNode:
    """
    Nodo para representar un árbol de expresión.
    
    Atributos:
    ----------
    value : str
        Valor del nodo (operador u operando)
    left : ExpressionNode, opcional
        Hijo izquierdo del nodo
    right : ExpressionNode, opcional
        Hijo derecho del nodo
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
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
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret

def infix_to_postfix(tokens):
    """
    Convierte una expresión de infijo a postfijo.
    (Misma implementación del Desafío 1)
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output, operator_stack = [], []
    
    for token in tokens:
        if token not in '+-*/^()':
            output.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
        elif token in '+-*/^':
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                output.append(operator_stack.pop())
            operator_stack.append(token)
    
    while operator_stack:
        output.append(operator_stack.pop())
    
    return output

def build_tree_from_infix(tokens):
    """
    Construye un árbol de expresión a partir de tokens en notación infija.
    
    Parámetros:
    -----------
    tokens : list
        Lista de tokens en notación infija
    
    Retorna:
    --------
    ExpressionNode
        Raíz del árbol de expresión
    """
    # 🔄 Primero convertir infijo a postfijo
    postfix = infix_to_postfix(tokens)
    
    # 📚 Pila para construcción del árbol
    stack = []
    
    for token in postfix:
        # 🔢 Si es operando, crear nodo y apilar
        if token not in '+-*/^':
            node = ExpressionNode(token)
            stack.append(node)
        else:
            # 🧩 Si es operador, crear nodo y conectar operandos
            node = ExpressionNode(token)
            
            # ⚠️ Asegurar que hay suficientes operandos
            if len(stack) >= 2:
                # Orden importante: primero hijo derecho, luego izquierdo
                node.right = stack.pop()
                node.left = stack.pop()
                
                # Apilar subárbol
                stack.append(node)
    
    # 🏁 Retornar raíz del árbol
    return stack[0] if stack else None

def test_build_tree_from_infix():
    """
    Batería de pruebas para construcción de árbol de expresión.
    Prueba diversos escenarios de construcción de árbol.
    """
    # 🧪 Casos de prueba
    test_cases = [
        # Caso 1: Expresión simple
        {
            'input': ['2', '+', '3'],
            'description': 'Expresión básica'
        },
        # Caso 2: Expresión con precedencia
        {
            'input': ['2', '+', '3', '*', '4'],
            'description': 'Expresión con multiplicación'
        },
        # Caso 3: Expresión con paréntesis
        {
            'input': ['(', '2', '+', '3', ')', '*', '4'],
            'description': 'Expresión con paréntesis'
        },
        # Caso 4: Expresión compleja
        {
            'input': ['5', '*', '(', '3', '+', '2', ')', '-', '10'],
            'description': 'Expresión compleja con paréntesis'
        }
    ]
    
    # 🕵️ Ejecutar pruebas
    for i, caso in enumerate(test_cases, 1):
        print(f"🌳 Prueba {i}: {caso['description']}")
        print(f"   Entrada: {caso['input']}")
        
        # Construir árbol
        raiz = build_tree_from_infix(caso['input'])
        
        # Mostrar estructura del árbol
        print("   Estructura del árbol:")
        print(raiz)
        print("\n")

# Descomentar para ejecutar pruebas
test_build_tree_from_infix()