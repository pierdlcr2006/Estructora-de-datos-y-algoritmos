import os
import time
from colorama import Fore, Style, Back, init

# Inicializar colorama
init(autoreset=True)

# -----------------------------------
# FUNCIONES AUXILIARES PARA FORMATO
# -----------------------------------
def print_title(title):
    width = 80
    print("\n" + Fore.CYAN + "═" * width)
    print(Fore.CYAN + Style.BRIGHT + title.center(width))
    print(Fore.CYAN + "═" * width + Style.RESET_ALL + "\n")

def print_section(title):
    print(Fore.MAGENTA + Style.BRIGHT + f"\n── {title} ──" + Style.RESET_ALL + "\n")

def print_success():
    print(Back.GREEN + Fore.BLACK + Style.BRIGHT + " ✓ CORRECTO ".center(80) + Style.RESET_ALL + "\n")

def print_failure():
    print(Back.RED + Fore.WHITE + Style.BRIGHT + " ✗ INCORRECTO ".center(80) + Style.RESET_ALL + "\n")

def print_summary(total, passed):
    width = 80
    pct = (passed / total) * 100 if total else 0
    print(Fore.YELLOW + "═" * width)
    print(Fore.YELLOW + Style.BRIGHT + f" 🏁 RESUMEN DE RESULTADOS ".center(width))
    print(Fore.YELLOW + "═" * width)
    print(f"Total de pruebas:     {total}")
    print(f"Pruebas correctas:    {passed}")
    print(f"Porcentaje de éxito:  {pct:.2f}%")
    if pct == 100:
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + " ¡Todas las pruebas pasaron! 🎉 ".center(width))
    elif pct >= 75:
        print(Back.YELLOW + Fore.BLACK + Style.BRIGHT + " Buen trabajo, casi todo correcto! 👍 ".center(width))
    else:
        print(Back.RED + Fore.WHITE + Style.BRIGHT + " Necesitas mejorar, algunos tests fallaron. ❌ ".center(width))
    print(Fore.YELLOW + "═" * width + "\n")


# ========================================================================================
# 1. ESTRUCTURAS DE DATOS BÁSICAS
# ========================================================================================

class GenericTreeNode:
    """Nodo para árbol genérico (múltiples hijos)."""
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def remove_child(self, child):
        self.children.remove(child)
    def __str__(self, level=0):
        ret = "  " * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

class ExpressionNode:
    """Nodo para árbol de expresión binaria."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def is_operator(self):
        return self.value in ['+', '-', '*', '/', '^']
    def __str__(self, level=0):
        ret = "  " * level + str(self.value) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret


# ========================================================================================
# 2. IMPLEMENTACIONES Y FUNCIONES AUXILIARES
# ========================================================================================

# Challenge 1: Conversión Infija a Postfija
def infix_to_postfix(tokens):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    output = []
    stack = []
    for token in tokens:
        if token not in precedence and token not in '()':
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1],0) >= precedence.get(token,0):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

# Challenge 2: Construcción de árbol desde infija (por conversión a postfija)
class ExpressionTreeBuilder:
    def __init__(self):
        self.root = None

    @classmethod
    def from_infix(cls, tokens):
        obj = cls()
        postfix = infix_to_postfix(tokens)
        stack = []
        for token in postfix:
            node = ExpressionNode(token)
            if node.is_operator():
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        obj.root = stack.pop()
        return obj

def evaluate_expression_tree(node):
    if not node.is_operator():
        return float(node.value)
    l = evaluate_expression_tree(node.left)
    r = evaluate_expression_tree(node.right)
    if node.value == '+': return l + r
    if node.value == '-': return l - r
    if node.value == '*': return l * r
    if node.value == '/': return l / r
    if node.value == '^': return l ** r

# Challenge 3: Altura de árbol genérico
def tree_height(node):
    if node is None:
        return -1
    if not node.children:
        return 0
    return 1 + max(tree_height(c) for c in node.children)

# Challenge 4: Encontrar nodos hoja
def find_leaves(node):
    if node is None:
        return []
    if not node.children:
        return [node.value]
    leaves = []
    for c in node.children:
        leaves.extend(find_leaves(c))
    return leaves

# Challenge 5: Simplificación árbol expresión
def simplify_expression_tree(node):
    if node is None:
        return None
    if not node.is_operator():
        return node
    node.left = simplify_expression_tree(node.left)
    node.right = simplify_expression_tree(node.right)

    # Si ambos hijos son números, evaluar y reemplazar
    try:
        if (node.left and node.right and
            not node.left.is_operator() and
            not node.right.is_operator()):
            lval = float(node.left.value)
            rval = float(node.right.value)
            res = None
            if node.value == '+':
                res = lval + rval
            elif node.value == '-':
                res = lval - rval
            elif node.value == '*':
                res = lval * rval
            elif node.value == '/':
                if rval == 0:
                    return node
                res = lval / rval
            elif node.value == '^':
                res = lval ** rval
            if res is not None:
                node = ExpressionNode(str(int(res) if res == int(res) else res))
                return node
    except:
        pass
    return node


# ========================================================================================
# 3. TESTS ORDENADOS POR CHALLENGE CON SALIDA BONITA
# ========================================================================================

def test_challenge_1():
    test_cases = [
        {'input': ['2', '+', '3'], 'expected': ['2', '3', '+'], 'desc': 'Expresión simple'},
        {'input': ['2', '+', '3', '*', '4'], 'expected': ['2', '3', '4', '*', '+'], 'desc': 'Manejo de precedencia'},
        {'input': ['(', '2', '+', '3', ')', '*', '4'], 'expected': ['2', '3', '+', '4', '*'], 'desc': 'Paréntesis simples'},
        {'input': ['(', '5', '+', '3', ')', '*', '(', '10', '-', '8', ')'], 'expected': ['5', '3', '+', '10', '8', '-', '*'], 'desc': 'Expresión compleja'},
        {'input': ['3', '+', '4', '*', '2', '/', '(', '1', '-', '5', ')', '^', '2'], 'expected': ['3', '4', '2', '*', '1', '5', '-', '2', '^', '/', '+'], 'desc': 'Potencia y precedencia mixta'}
    ]
    total = len(test_cases)
    passed = 0

    print_title("Challenge 1: Conversión Infija a Postfija")

    for i, c in enumerate(test_cases, 1):
        res = infix_to_postfix(c['input'])
        correct = res == c['expected']
        if correct:
            passed += 1
        print_section(f"Prueba {i}: {c['desc']}")
        print(f"📥 Infija:      {' '.join(c['input'])}")
        print(f"📤 Esperada:    {' '.join(c['expected'])}")
        print(f"🔄 Resultado:   {' '.join(res)}")
        print_success() if correct else print_failure()

    print_summary(total, passed)


def test_challenge_2():
    test_cases = [
        {'input': ['2', '+', '3'], 'expected': 5.0, 'desc': 'Expresión básica'},
        {'input': ['2', '+', '3', '*', '4'], 'expected': 14.0, 'desc': 'Con precedencia de operadores'},
        {'input': ['(', '2', '+', '3', ')', '*', '4'], 'expected': 20.0, 'desc': 'Con paréntesis'},
        {'input': ['5', '*', '(', '3', '+', '2', ')', '-', '10'], 'expected': 15.0, 'desc': 'Compleja con paréntesis'},
        {'input': ['2', '^', '3', '+', '10', '/', '2'], 'expected': 13.0, 'desc': 'Potencia y división'}
    ]
    total = len(test_cases)
    passed = 0

    print_title("Challenge 2: Construcción y Evaluación de Árbol de Expresión")

    for i, c in enumerate(test_cases, 1):
        tree_builder = ExpressionTreeBuilder.from_infix(c['input'])
        try:
            result = evaluate_expression_tree(tree_builder.root)
            correct = abs(result - c['expected']) < 1e-6
        except:
            result = None
            correct = False
        if correct:
            passed += 1

        print_section(f"Prueba {i}: {c['desc']}")
        print(f"📝 Infija:   {' '.join(c['input'])}")
        print(f"🎯 Esperado: {c['expected']}")
        print(f"🧮 Obtenido: {result}")
        print_success() if correct else print_failure()
        print("\n📊 Árbol expresión:")
        print(tree_builder.root)

    print_summary(total, passed)


def test_challenge_3():
    # Crear árboles para test
    empty = None
    single = GenericTreeNode('Raíz')

    linear = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    linear.add_child(b)
    b.add_child(c)
    c.add_child(d)

    balanced = GenericTreeNode('Raíz')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    balanced.add_child(b)
    balanced.add_child(c)
    balanced.add_child(d)
    b.add_child(e)
    b.add_child(f)
    c.add_child(g)

    unbalanced = GenericTreeNode('Raíz')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    unbalanced.add_child(b)
    unbalanced.add_child(c)
    b.add_child(d)
    d.add_child(e)
    e.add_child(f)
    f.add_child(g)

    test_cases = [
        {'tree': empty, 'expected': -1, 'desc': 'Árbol vacío'},
        {'tree': single, 'expected': 0, 'desc': 'Árbol de un nodo'},
        {'tree': linear, 'expected': 3, 'desc': 'Árbol lineal'},
        {'tree': balanced, 'expected': 2, 'desc': 'Árbol balanceado'},
        {'tree': unbalanced, 'expected': 5, 'desc': 'Árbol no balanceado'}
    ]

    total = len(test_cases)
    passed = 0

    print_title("Challenge 3: Cálculo de Altura en Árboles Genéricos")

    for i, c in enumerate(test_cases, 1):
        altura = tree_height(c['tree'])
        correct = altura == c['expected']
        if correct:
            passed += 1

        print_section(f"Prueba {i}: {c['desc']}")
        print(f"📝 Altura calculada: {altura}")
        print(f"🎯 Altura esperada:  {c['expected']}")
        print_success() if correct else print_failure()
        if c['tree']:
            print("\n📊 Estructura del árbol:")
            print(c['tree'])

    print_summary(total, passed)


def test_challenge_4():
    empty = None
    single = GenericTreeNode('A')

    linear = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    linear.add_child(b)
    b.add_child(c)

    balanced = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    balanced.add_child(b)
    balanced.add_child(c)
    balanced.add_child(d)
    b.add_child(e)
    b.add_child(f)
    b.add_child(g)

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

    test_cases = [
        {'tree': empty, 'desc': 'Árbol vacío', 'expected': []},
        {'tree': single, 'desc': 'Árbol de un nodo', 'expected': ['A']},
        {'tree': linear, 'desc': 'Árbol lineal', 'expected': ['C']},
        {'tree': balanced, 'desc': 'Árbol balanceado', 'expected': ['E', 'F', 'G', 'C', 'D']},
        {'tree': complex_tree, 'desc': 'Árbol complejo', 'expected': ['E', 'H', 'C', 'G']},  # Corregir aquí
    ]

    total = len(test_cases)
    passed = 0

    print_title("Challenge 4: Buscador de Nodos Hoja en Árboles Genéricos")

    for i, c in enumerate(test_cases, 1):
        leaves = find_leaves(c['tree'])
        # Comparar sin importar el orden utilizando conjuntos
        correct = set(leaves) == set(c['expected'])
        if correct:
            passed += 1

        print_section(f"Prueba {i}: {c['desc']}")
        print(f"▶ Nodos hoja encontrados: {leaves}")
        print(f"▶ Resultado esperado:     {c['expected']}")
        print_success() if correct else print_failure()
        if c['tree']:
            print("\n📊 Estructura del árbol:")
            print(c['tree'])

    print_summary(total, passed)


def test_challenge_5():
    # Caso 1: 2 + 3
    root1 = ExpressionNode('+')
    root1.left = ExpressionNode('2')
    root1.right = ExpressionNode('3')

    # Caso 2: (2 + 3) * x (solo simplifica suma)
    root2 = ExpressionNode('*')
    add = ExpressionNode('+')
    add.left = ExpressionNode('2')
    add.right = ExpressionNode('3')
    root2.left = add
    root2.right = ExpressionNode('x')

    # Caso 3: x + y (no simplifica)
    root3 = ExpressionNode('+')
    root3.left = ExpressionNode('x')
    root3.right = ExpressionNode('y')

    # Caso 4: (2 * 3) + (8 / 4)
    root4 = ExpressionNode('+')
    mul = ExpressionNode('*')
    mul.left = ExpressionNode('2')
    mul.right = ExpressionNode('3')
    div = ExpressionNode('/')
    div.left = ExpressionNode('8')
    div.right = ExpressionNode('4')
    root4.left = mul
    root4.right = div

    # Caso 5: x * (6 / 2)
    root5 = ExpressionNode('*')
    div2 = ExpressionNode('/')
    div2.left = ExpressionNode('6')
    div2.right = ExpressionNode('2')
    root5.left = ExpressionNode('x')
    root5.right = div2

    test_cases = [
        {'root': root1, 'expected': '5', 'desc': 'Expresión constante simple: (2 + 3)'},
        {'root': root2, 'expected': '*', 'desc': 'Expresión parcialmente simplificable: (2 + 3) * x'},
        {'root': root3, 'expected': '+', 'desc': 'Expresión sin simplificación: x + y'},
        {'root': root4, 'expected': '8', 'desc': 'Expresión compleja: ((2 * 3) + (8 / 4))'},
        {'root': root5, 'expected': '*', 'desc': 'Expresión mixta: x * (6 / 2)'},
    ]

    total = len(test_cases)
    passed = 0

    print_title("Challenge 5: Simplificador de Árboles de Expresión Matemática")

    for i, c in enumerate(test_cases, 1):
        simplified_root = simplify_expression_tree(c['root'])
        # Raíz después de simplificar
        root_val = simplified_root.value if simplified_root else None
        correct = (root_val == c['expected'])
        if correct:
            passed += 1
        print_section(f"Prueba {i}: {c['desc']}")
        print(f"▶ Valor raíz después de simplificar: {root_val}")
        print(f"▶ Valor esperado:                    {c['expected']}")
        print_success() if correct else print_failure()

    print_summary(total, passed)


# ========================================================================================
# 4. MAIN
# ========================================================================================

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + Style.BRIGHT + "\n🌿 IMPLEMENTACIÓN Y TESTS DE ÁRBOLES GENÉRICOS Y DE EXPRESIÓN 🌿\n" + Style.RESET_ALL)

    test_challenge_1()
    time.sleep(1)
    test_challenge_2()
    time.sleep(1)
    test_challenge_3()
    time.sleep(1)
    test_challenge_4()
    time.sleep(1)
    test_challenge_5()
    print(Fore.GREEN + Style.BRIGHT + "\n🎉 TODOS LOS TESTS FINALIZARON CORRECTAMENTE 🎉\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
