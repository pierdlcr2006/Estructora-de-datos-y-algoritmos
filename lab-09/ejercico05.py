# Clase para nodo de árbol de expresión
class ExpressionNode:
    def __init__(self, value):
        self.value = value        # 📌 Valor del nodo (operando o operador)
        self.left = None          # 👈 Hijo izquierdo
        self.right = None         # 👉 Hijo derecho

# Clase principal para simplificar árbol de expresiones
class ExpressionTree:
    def __init__(self, root=None):
        self.root = root          # 🌱 Nodo raíz del árbol

    def simplify(self):
        """Simplifica subexpresiones constantes en el árbol"""

        # Función auxiliar que verifica si un valor es numérico
        def is_constant(val):
            try:
                float(val)
                return True       # ✅ Si puede convertirse a número, es constante
            except:
                return False      # ❌ Si lanza error, no es constante

        # Función recursiva que evalúa nodos de forma postorden
        def eval_node(node):
            if not node or not node.left or not node.right:
                return node       # Caso base: nodo hoja o incompleto

            # 🔁 Simplificar subárbol izquierdo y derecho
            node.left = eval_node(node.left)
            node.right = eval_node(node.right)

            # Verificar si ambos hijos son constantes
            if is_constant(node.left.value) and is_constant(node.right.value):
                left_val = float(node.left.value)
                right_val = float(node.right.value)

                # Evaluar operación según operador
                if node.value == '+':
                    result = left_val + right_val
                elif node.value == '-':
                    result = left_val - right_val
                elif node.value == '*':
                    result = left_val * right_val
                elif node.value == '/':
                    result = left_val / right_val

                # Reemplazar subárbol con nodo constante
                return ExpressionNode(str(int(result) if result.is_integer() else result))

            return node  # Si no se puede simplificar, retornar nodo original

        # Llamada inicial con la raíz
        self.root = eval_node(self.root)

# (2 + 3) => 5
tree1 = ExpressionTree(ExpressionNode('+'))
tree1.root.left = ExpressionNode('2')
tree1.root.right = ExpressionNode('3')
tree1.simplify()
print(tree1.root.value == '5')

# (2 + 3) * x => 5 * x
tree2 = ExpressionTree(ExpressionNode('*'))
tree2.root.left = ExpressionNode('+')
tree2.root.left.left = ExpressionNode('2')
tree2.root.left.right = ExpressionNode('3')
tree2.root.right = ExpressionNode('x')
tree2.simplify()
print(tree2.root.left.value == '5')

# (2 * 3) + (8 / 4) => 6 + 2 => 8
tree3 = ExpressionTree(ExpressionNode('+'))
tree3.root.left = ExpressionNode('*')
tree3.root.left.left = ExpressionNode('2')
tree3.root.left.right = ExpressionNode('3')
tree3.root.right = ExpressionNode('/')
tree3.root.right.left = ExpressionNode('8')
tree3.root.right.right = ExpressionNode('4')
tree3.simplify()
print(tree3.root.value == '8')