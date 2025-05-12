# 🌟 Desafío 1: Conversión de Expresión Infija a Postfija
# Objetivo: Convertir una expresión matemática de notación infija a postfija
# Características principales:
# - Manejo de precedencia de operadores
# - Soporte para paréntesis
# - Conversión precisa de expresiones

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
    # 📊 Diccionario de precedencia de operadores
    # Cuanto mayor el valor, mayor la precedencia
    precedence = {
        '+': 1,  # Suma: menor precedencia
        '-': 1,  # Resta: menor precedencia
        '*': 2,  # Multiplicación: mayor precedencia
        '/': 2,  # División: mayor precedencia
        '^': 3   # Potencia: mayor precedencia aún
    }
    
    # 📝 Estructuras para almacenar resultados
    output = []        # Lista de salida en notación postfija
    operator_stack = [] # Pila para manejar operadores temporalmente
    
    for token in tokens:
        # 🔢 Si es un número o variable, va directo a la salida
        if token not in '+-*/^()':
            output.append(token)
        
        # 🔤 Manejo de paréntesis
        elif token == '(':
            # Paréntesis de apertura: se apila para procesar después
            operator_stack.append(token)
        
        elif token == ')':
            # 🔒 Paréntesis de cierre: sacar operadores hasta encontrar paréntesis de apertura
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            
            # Eliminar paréntesis de apertura
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
        
        # 🧮 Manejo de operadores
        elif token in '+-*/^':
            # Sacar operadores con mayor o igual precedencia
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                output.append(operator_stack.pop())
            
            # Apilar operador actual
            operator_stack.append(token)
    
    # 🏁 Agregar operadores restantes
    while operator_stack:
        output.append(operator_stack.pop())
    
    return output

# 🧪 Función de pruebas para verificar la conversión
def test_infix_to_postfix():
    """
    Batería de pruebas para la conversión de infijo a postfijo.
    Cubre diversos casos de complejidad creciente.
    """
    # Casos de prueba
    test_cases = [
        # Caso 1: Expresión simple
        {
            'input': ['2', '+', '3'],
            'expected': ['2', '3', '+']
        },
        # Caso 2: Manejo de precedencia
        {
            'input': ['2', '+', '3', '*', '4'],
            'expected': ['2', '3', '4', '*', '+']
        },
        # Caso 3: Paréntesis
        {
            'input': ['(', '2', '+', '3', ')', '*', '4'],
            'expected': ['2', '3', '+', '4', '*']
        },
        # Caso 4: Expresión compleja
        {
            'input': ['(', '5', '+', '3', ')', '*', '(', '10', '-', '8', ')'],
            'expected': ['5', '3', '+', '10', '8', '-', '*']
        }
    ]
    
    # 🕵️ Ejecutar pruebas
    for i, caso in enumerate(test_cases, 1):
        resultado = infix_to_postfix(caso['input'])
        print(f"🧩 Prueba {i}:")
        print(f"   Entrada:    {caso['input']}")
        print(f"   Esperado:   {caso['expected']}")
        print(f"   Resultado:  {resultado}")
        print(f"   ✅ Correcto: {resultado == caso['expected']}\n")

# Descomentar para ejecutar pruebas
test_infix_to_postfix()