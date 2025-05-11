# -----------------------------------------
# Definición de nodo para árbol binario
# -----------------------------------------

class TreeNode:
    # Constructor del nodo, recibe un valor
    def __init__(self, value):
        self.value = value      # 📌 Almacena el valor del nodo
        self.left = None        # 👈 Hijo izquierdo
        self.right = None       # 👉 Hijo derecho

# ------------------------------------------------
# Clase con método para podar el árbol binario ✂️
# ------------------------------------------------

class PodaArbol:
    def podar(self, root, objetivo):
        """
        Elimina todos los subárboles que no contienen el valor objetivo.
        Utiliza recorrido postorden (procesa hijos antes que el padre).
        """
        if not root:                     # Si el nodo es nulo
            return None                 # No hay nada que podar

        # Recorrer primero los hijos
        root.left = self.podar(root.left, objetivo)    # Podar subárbol izquierdo
        root.right = self.podar(root.right, objetivo)  # Podar subárbol derecho

        # Si el nodo actual no es el objetivo y no tiene hijos útiles
        if root.value != objetivo and not root.left and not root.right:
            return None   # Se poda este nodo también
        else:
            return root   # Se conserva el nodo

# -----------------------------------------------
# Casos de prueba para la poda de árboles ✂️🌳
# -----------------------------------------------

def probar_poda():
    poda = PodaArbol()

    # Caso 1: Árbol contiene múltiples nodos a podar
    # Estructura inicial:
    #        1
    #       / \
    #      0   1
    #     / \
    #    0   0
    root1 = TreeNode(1)
    root1.left = TreeNode(0)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(0)

    print("Caso 1: Poda con valor objetivo = 1")
    resultado1 = poda.podar(root1, 1)
    print("Raiz despues de la poda:", resultado1.value if resultado1 else "None")
    print()

    # Caso 2: Árbol completamente podado
    # Estructura:
    #      0
    #     / \
    #    0   0
    root2 = TreeNode(0)
    root2.left = TreeNode(0)
    root2.right = TreeNode(0)

    print("Caso 2: Todo el arbol debe ser podado (objetivo = 1)")
    resultado2 = poda.podar(root2, 1)
    print("Raiz despues de la poda:", resultado2.value if resultado2 else "None")
    print()

    # Caso 3: Árbol donde todo se conserva
    # Estructura:
    #     2
    #    / \
    #   2   2
    root3 = TreeNode(2)
    root3.left = TreeNode(2)
    root3.right = TreeNode(2)

    print("Caso 3: Ningun nodo es podado (objetivo = 2)")
    resultado3 = poda.podar(root3, 2)
    print("Raiz despues de la poda:", resultado3.value if resultado3 else "None")
    print()

# Ejecutar los casos
probar_poda()