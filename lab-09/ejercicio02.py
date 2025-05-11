# -----------------------------------------
# Definición de nodo para árbol binario
# -----------------------------------------

class TreeNode:
    # Constructor del nodo, recibe un valor
    def __init__(self, value):
        self.value = value      # 📌 Almacena el valor del nodo
        self.left = None        # 👈 Inicializa el hijo izquierdo como None
        self.right = None       # 👉 Inicializa el hijo derecho como None

# ----------------------------------------------------
# Clase para serializar y deserializar árbol binario
# ----------------------------------------------------

class SerializadorArbol:
    # Método para serializar el árbol a una cadena
    def serializar(self, root):
        """Serializa un árbol binario a una cadena usando recorrido por niveles"""
        if not root:                           # Si el árbol está vacío
            return ""                          # Retorna cadena vacía

        from collections import deque          # Importa deque para la cola
        queue = deque([root])                  # Inicializa cola con la raíz
        resultado = []                         # Lista para almacenar los valores

        while queue:                           # Mientras la cola no esté vacía
            nodo = queue.popleft()             # Extrae el nodo del frente

            if nodo:                           # Si el nodo no es None
                resultado.append(str(nodo.value))  # Agrega el valor del nodo a la lista
                queue.append(nodo.left)            # Agrega hijo izquierdo a la cola
                queue.append(nodo.right)           # Agrega hijo derecho a la cola
            else:
                resultado.append("null")       # Si el nodo es None, agrega "null"

        return ','.join(resultado)             # Une los valores con comas y retorna

    # Método para deserializar una cadena a un árbol binario
    def deserializar(self, datos):
        """Convierte una cadena serializada en un árbol binario"""
        if not datos:                          # Si la cadena está vacía
            return None                        # Retorna None

        valores = datos.split(',')             # Separa los valores por coma
        raiz = TreeNode(int(valores[0]))       # Crea la raíz con el primer valor
        from collections import deque          # Importa deque para la cola
        queue = deque([raiz])                  # Inicializa la cola con la raíz
        indice = 1                             # Índice para recorrer la lista de valores

        while queue and indice < len(valores): # Mientras haya nodos y valores por procesar
            nodo = queue.popleft()             # Extrae el nodo actual

            if valores[indice] != "null":      # Si el valor no es "null"
                nodo.left = TreeNode(int(valores[indice]))  # Crea nodo izquierdo
                queue.append(nodo.left)        # Agrega el hijo izquierdo a la cola
            indice += 1                        # Avanza al siguiente valor

            if indice < len(valores) and valores[indice] != "null":  # Si hay valor derecho
                nodo.right = TreeNode(int(valores[indice]))  # Crea nodo derecho
                queue.append(nodo.right)      # Agrega el hijo derecho a la cola
            indice += 1                        # Avanza al siguiente valor

        return raiz                            # Retorna la raíz del árbol reconstruido

# ----------------------------------------------------
# Casos de prueba para serialización y deserialización
# ----------------------------------------------------

# Crear instancia del serializador
serializador = SerializadorArbol()

# -----------------------------------------
# Caso 1: Arbol binario completo
# Estructura:
#         1
#       /   \
#      2     3
#     / \   / \
#    4  5  6  7
# -----------------------------------------
root1 = TreeNode(1)                       # Nodo raíz
root1.left = TreeNode(2)                 # Hijo izquierdo
root1.right = TreeNode(3)                # Hijo derecho
root1.left.left = TreeNode(4)            # Subárbol izquierdo
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)

# Serializar y deserializar el arbol
print("Caso 1: Arbol binario completo")
cadena1 = serializador.serializar(root1)           # Serializa el árbol
print("Serializado:", cadena1)                     # Muestra la cadena generada
reconstruido1 = serializador.deserializar(cadena1) # Deserializa la cadena
print("Raiz deserializada:", reconstruido1.value)  # Muestra el valor de la nueva raíz
print()

# -----------------------------------------
# Caso 2: Arbol con hijos faltantes
# Estructura:
#         10
#        /  \
#       5    15
#        \     \
#         8     20
# -----------------------------------------
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.left.right = TreeNode(8)
root2.right.right = TreeNode(20)

# Serializar y deserializar el árbol
print("Caso 2: Arbol con hijos faltantes")
cadena2 = serializador.serializar(root2)
print("Serializado:", cadena2)
reconstruido2 = serializador.deserializar(cadena2)
print("Raiz deserializada:", reconstruido2.value)
print()

# -----------------------------------------
# Caso 3: Arbol con un solo nodo
# Estructura:
#         42
# -----------------------------------------
root3 = TreeNode(42)

# Serializar y deserializar el árbol
print("Caso 3: Arbol con un solo nodo")
cadena3 = serializador.serializar(root3)
print("Serializado:", cadena3)
reconstruido3 = serializador.deserializar(cadena3)
print("Raiz deserializada:", reconstruido3.value)