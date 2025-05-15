# ------------------------- #
# CONVERSIÓN INFIJA A POSTFIJA
# ------------------------- #
# Implementación del algoritmo Shunting-yard para convertir expresiones
# matemáticas de notación infija (común) a notación postfija (RPN)

def infix_to_postfix(tokens):
    """
    Convierte una expresión matemática de notación infija a postfija.
    
    Parámetros:
    -----------
    tokens : list
        Lista de tokens en notación infija
    
    Retorna:
    --------
    list
        Tokens en notación postfija
    
    Ejemplo:
    --------
    Entrada: ['2', '+', '3', '*', '4']
    Salida:  ['2', '3', '4', '*', '+']
    """
    # ------------------------- #
    # CONFIGURACIÓN INICIAL
    # ------------------------- #
    # Diccionario de precedencia de operadores (mayor valor = mayor precedencia)
    precedence = {
        '+': 1,  # Suma: menor precedencia
        '-': 1,  # Resta: menor precedencia
        '*': 2,  # Multiplicación: mayor precedencia
        '/': 2,  # División: mayor precedencia
        '^': 3   # Potencia: mayor precedencia aún
    }
    
    # Estructuras para el algoritmo
    output = []         # Lista de salida en notación postfija
    operator_stack = [] # Pila para manejar operadores temporalmente
    
    # ------------------------- #
    # PROCESAMIENTO DE TOKENS
    # ------------------------- #
    for token in tokens:
        # Caso 1: Operandos (números o variables)
        if token not in '+-*/^()':
            output.append(token)
        
        # Caso 2: Paréntesis de apertura
        elif token == '(':
            operator_stack.append(token)
        
        # Caso 3: Paréntesis de cierre
        elif token == ')':
            # Extraer operadores hasta encontrar el paréntesis de apertura correspondiente
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            
            # Eliminar el paréntesis de apertura
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
        
        # Caso 4: Operadores matemáticos
        elif token in '+-*/^':
            # Extraer operadores con mayor o igual precedencia
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                output.append(operator_stack.pop())
            
            # Apilar el operador actual
            operator_stack.append(token)
    
    # ------------------------- #
    # FINALIZACIÓN
    # ------------------------- #
    # Extraer operadores restantes
    while operator_stack:
        output.append(operator_stack.pop())
    
    return output

# ------------------------- #
# VISUALIZACIÓN Y PRUEBAS
# ------------------------- #
def test_infix_to_postfix():
    """
    Batería de pruebas para la conversión de infijo a postfijo.
    Cubre diversos casos de complejidad creciente.
    """
    # Casos de prueba con diferentes niveles de complejidad
    test_cases = [
        # Caso 1: Expresión simple
        {
            'input': ['2', '+', '3'],
            'expected': ['2', '3', '+'],
            'descripcion': 'Expresión simple'
        },
        # Caso 2: Manejo de precedencia
        {
            'input': ['2', '+', '3', '*', '4'],
            'expected': ['2', '3', '4', '*', '+'],
            'descripcion': 'Manejo de precedencia'
        },
        # Caso 3: Paréntesis simples
        {
            'input': ['(', '2', '+', '3', ')', '*', '4'],
            'expected': ['2', '3', '+', '4', '*'],
            'descripcion': 'Paréntesis simples'
        },
        # Caso 4: Expresión compleja con paréntesis anidados
        {
            'input': ['(', '5', '+', '3', ')', '*', '(', '10', '-', '8', ')'],
            'expected': ['5', '3', '+', '10', '8', '-', '*'],
            'descripcion': 'Expresión compleja'
        },
        # Caso 5: Expresión con potencia y precedencia mixta
        {
            'input': ['3', '+', '4', '*', '2', '/', '(', '1', '-', '5', ')', '^', '2'],
            'expected': ['3', '4', '2', '*', '1', '5', '-', '2', '^', '/', '+'],
            'descripcion': 'Potencia y precedencia mixta'
        }
    ]
    
    # Contadores para el resumen final
    tests_totales = len(test_cases)
    tests_pasados = 0
    
    # Encabezado de la tabla de resultados
    print("\n" + "=" * 80)
    print(f"{'🧮 PRUEBAS DE CONVERSIÓN INFIJA A POSTFIJA':^80}")
    print("=" * 80)
    
    # Ejecutar cada caso de prueba
    for i, caso in enumerate(test_cases, 1):
        resultado = infix_to_postfix(caso['input'])
        es_correcto = resultado == caso['expected']
        
        if es_correcto:
            tests_pasados += 1
        
        # Separador entre pruebas
        print(f"\n{'-' * 80}")
        
        # Información de la prueba
        print(f"🧩 PRUEBA {i}: {caso['descripcion']}")
        print(f"{'-' * 80}")
        
        # Formatear la expresión original de manera legible
        expresion_infija = ' '.join(caso['input'])
        expresion_postfija_esperada = ' '.join(caso['expected'])
        expresion_postfija_resultado = ' '.join(resultado)
        
        # Mostrar las expresiones
        print(f"📥 Expresión infija:      {expresion_infija}")
        print(f"📤 Postfija esperada:     {expresion_postfija_esperada}")
        print(f"🔄 Postfija resultante:   {expresion_postfija_resultado}")
        
        # Indicador de éxito o fracaso
        estado = "✅ CORRECTO" if es_correcto else "❌ INCORRECTO"
        print(f"\n{estado:^80}")
    
    # Resumen final
    print("\n" + "=" * 80)
    print(f"{'RESUMEN DE RESULTADOS':^80}")
    print("=" * 80)
    print(f"Total de pruebas:     {tests_totales}")
    print(f"Pruebas correctas:    {tests_pasados}")
    print(f"Porcentaje de éxito:  {(tests_pasados/tests_totales) * 100:.2f}%")
    print("=" * 80 + "\n")

# Ejecutar las pruebas
if __name__ == "__main__":
    test_infix_to_postfix()