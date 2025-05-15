# ------------------------- #
# ÁRBOL DE EXPRESIÓN DESDE NOTACIÓN INFIJA
# ------------------------- #
# Implementación que construye un árbol binario de expresión
# a partir de una expresión matemática en notación infija

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
        # Construcción de representación visual del árbol con indentación
        ret = "\t" * level + str(self.value) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret
    
    def to_ascii_tree(self, prefix="", is_left=True):
        """
        Genera una representación ASCII del árbol más visual.
        
        Parámetros:
        -----------
        prefix : str
            Prefijo para la línea actual
        is_left : bool
            Indica si el nodo es hijo izquierdo
        
        Retorna:
        --------
        str
            Representación ASCII del árbol
        """
        result = ""
        
        # Ramificación para el nodo actual
        if self.value != "":
            # Determinar el conector adecuado basado en si es hijo izquierdo o derecho
            connector = "└── " if is_left else "┌── "
            result = prefix + connector + str(self.value) + "\n"
            
            # Nuevos prefijos para los hijos
            new_prefix = prefix + ("    " if is_left else "│   ")
            
            # Procesar hijo derecho primero para que aparezca arriba en la visualización
            if self.right:
                result += self.right.to_ascii_tree(new_prefix, False)
            
            # Luego procesar hijo izquierdo
            if self.left:
                result += self.left.to_ascii_tree(new_prefix, True)
                
        return result

# ------------------------- #
# CONVERSIÓN INFIJA A POSTFIJA
# ------------------------- #
def infix_to_postfix(tokens):
    """
    Convierte una expresión de infijo a postfijo.
    
    Parámetros:
    -----------
    tokens : list
        Lista de tokens en notación infija
    
    Retorna:
    --------
    list
        Lista de tokens en notación postfija
    """
    # Diccionario de precedencia de operadores
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []          # Lista de salida en notación postfija
    operator_stack = []  # Pila para manejar operadores temporalmente
    
    for token in tokens:
        # Caso 1: Operandos
        if token not in '+-*/^()':
            output.append(token)
        
        # Caso 2: Paréntesis de apertura
        elif token == '(':
            operator_stack.append(token)
        
        # Caso 3: Paréntesis de cierre
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
        
        # Caso 4: Operadores
        elif token in '+-*/^':
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                output.append(operator_stack.pop())
            operator_stack.append(token)
    
    # Extraer operadores restantes
    while operator_stack:
        output.append(operator_stack.pop())
    
    return output

# ------------------------- #
# CONSTRUCCIÓN DEL ÁRBOL
# ------------------------- #
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
    # Primero convertir infijo a postfijo
    postfix = infix_to_postfix(tokens)
    
    # Pila para construcción del árbol
    stack = []
    
    for token in postfix:
        # Si es operando, crear nodo y apilar
        if token not in '+-*/^':
            node = ExpressionNode(token)
            stack.append(node)
        else:
            # Si es operador, crear nodo y conectar operandos
            node = ExpressionNode(token)
            
            # Asegurar que hay suficientes operandos
            if len(stack) >= 2:
                # Orden importante: primero hijo derecho, luego izquierdo (para evaluación correcta)
                node.right = stack.pop()  # Segundo operando
                node.left = stack.pop()   # Primer operando
                
                # Apilar subárbol
                stack.append(node)
    
    # Retornar raíz del árbol
    return stack[0] if stack else None

# ------------------------- #
# EVALUACIÓN DEL ÁRBOL
# ------------------------- #
def evaluate_tree(node):
    """
    Evalúa recursivamente un árbol de expresión.
    
    Parámetros:
    -----------
    node : ExpressionNode
        Nodo raíz del árbol a evaluar
    
    Retorna:
    --------
    float
        Resultado de la evaluación
    """
    # Caso base: nodo es un número
    if node.value not in '+-*/^':
        return float(node.value)
    
    # Evaluar recursivamente los hijos
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    
    # Aplicar operación correspondiente
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val
    elif node.value == '^':
        return left_val ** right_val
    
    return 0  # No debería llegar aquí

# ------------------------- #
# PRUEBAS Y VISUALIZACIÓN
# ------------------------- #
def test_build_tree_from_infix():
    """
    Batería de pruebas para construcción de árbol de expresión.
    Prueba diversos escenarios de construcción de árbol y muestra resultados.
    """
    # Casos de prueba con expresiones de complejidad creciente
    test_cases = [
        # Caso 1: Expresión simple
        {
            'input': ['2', '+', '3'],
            'description': 'Expresión básica',
            'expected_result': 5.0
        },
        # Caso 2: Expresión con precedencia
        {
            'input': ['2', '+', '3', '*', '4'],
            'description': 'Expresión con precedencia de operadores',
            'expected_result': 14.0
        },
        # Caso 3: Expresión con paréntesis
        {
            'input': ['(', '2', '+', '3', ')', '*', '4'],
            'description': 'Expresión con paréntesis',
            'expected_result': 20.0
        },
        # Caso 4: Expresión compleja
        {
            'input': ['5', '*', '(', '3', '+', '2', ')', '-', '10'],
            'description': 'Expresión compleja con paréntesis',
            'expected_result': 15.0
        },
        # Caso 5: Expresión con división y potencia
        {
            'input': ['2', '^', '3', '+', '10', '/', '2'],
            'description': 'Expresión con potencia y división',
            'expected_result': 13.0
        }
    ]
    
    # Contadores para el resumen final
    tests_totales = len(test_cases)
    tests_pasados = 0
    
    # Encabezado de sección de pruebas
    print("\n" + "=" * 80)
    print(f"{'🌳 PRUEBAS DE CONSTRUCCIÓN DE ÁRBOL DE EXPRESIÓN':^80}")
    print("=" * 80)
    
    # Ejecutar cada caso de prueba
    for i, caso in enumerate(test_cases, 1):
        # Construir árbol
        raiz = build_tree_from_infix(caso['input'])
        
        # Evaluar el árbol
        try:
            resultado = evaluate_tree(raiz)
            es_correcto = abs(resultado - caso['expected_result']) < 0.001
            if es_correcto:
                tests_pasados += 1
        except Exception as e:
            resultado = f"Error: {str(e)}"
            es_correcto = False
        
        # Separador entre pruebas
        print(f"\n{'-' * 80}")
        
        # Información de la prueba
        print(f"🔍 PRUEBA {i}: {caso['description']}")
        print(f"{'-' * 80}")
        
        # Formatear la expresión original de manera legible
        expresion_infija = ' '.join(caso['input'])
        expresion_postfija = ' '.join(infix_to_postfix(caso['input']))
        
        # Mostrar información detallada
        print(f"📝 Expresión infija:   {expresion_infija}")
        print(f"📝 Expresión postfija: {expresion_postfija}")
        print(f"🎯 Resultado esperado: {caso['expected_result']}")
        print(f"🧮 Resultado obtenido: {resultado}")
        
        # Indicador de éxito o fracaso
        estado = "✅ CORRECTO" if es_correcto else "❌ INCORRECTO"
        print(f"\n{estado:^80}")
        
        # Visualización del árbol en forma ASCII
        print(f"\n📊 Estructura del árbol:")
        print(f"{'-' * 40}")
        
        # Mostrar la representación ASCII del árbol
        if raiz:
            print(raiz.to_ascii_tree())
        else:
            print("(Árbol vacío)")
    
    # Resumen final
    print("\n" + "=" * 80)
    print(f"{'RESUMEN DE RESULTADOS':^80}")
    print("=" * 80)
    print(f"Total de pruebas:     {tests_totales}")
    print(f"Pruebas correctas:    {tests_pasados}")
    print(f"Porcentaje de éxito:  {(tests_pasados/tests_totales) * 100:.2f}%")
    print("=" * 80 + "\n")

# Ejecutar las pruebas cuando se ejecuta el script directamente
if __name__ == "__main__":
    test_build_tree_from_infix()