# Lista donde se guardan los resultados de las pruebas con íconos
test_results = []

# Función auxiliar para registrar los resultados de las pruebas
def record_test(test_name, condition):
    # Si la condición se cumple, se usa el ícono de check, si no, una X
    emoji = "[OK]" if condition else "[X]"
    # Se agrega el resultado a la lista
    test_results.append(f"{emoji} {test_name}")

# Definición de la clase MinHeap
class MinHeap:
    # Método constructor
    def __init__(self):
        # Inicializa el heap como una lista vacía
        self.heap = []

    # Método privado para obtener el índice del padre de un nodo dado
    def _parent_index(self, index):
        # Si el índice es menor o igual a 0, o fuera del rango del heap, no tiene padre
        if index <= 0 or index >= len(self.heap):
            return -1  # Retorna -1 para indicar que no tiene padre válido
        # Fórmula para obtener el índice del padre
        return (index - 1) // 2

    # Método privado para obtener el índice del hijo izquierdo de un nodo dado
    def _left_child_index(self, index):
        # Se calcula el índice del hijo izquierdo usando la fórmula 2i + 1
        child_index = 2 * index + 1
        # Verifica si el hijo izquierdo está dentro del rango del heap
        if child_index < len(self.heap):
            return child_index  # Retorna el índice si es válido
        # Si está fuera del rango, retorna -1
        return -1

    # Método privado para obtener el índice del hijo derecho de un nodo dado
    def _right_child_index(self, index):
        # Se calcula el índice del hijo derecho usando la fórmula 2i + 2
        child_index = 2 * index + 2
        # Verifica si el hijo derecho está dentro del rango del heap
        if child_index < len(self.heap):
            return child_index  # Retorna el índice si es válido
        # Si está fuera del rango, retorna -1
        return -1

    # Método privado para verificar si el nodo tiene hijo izquierdo
    def _has_left_child(self, index):
        # Retorna verdadero si el índice del hijo izquierdo es menor que el tamaño del heap
        return 2 * index + 1 < len(self.heap)

    # Método privado para verificar si el nodo tiene hijo derecho
    def _has_right_child(self, index):
        # Retorna verdadero si el índice del hijo derecho es menor que el tamaño del heap
        return 2 * index + 2 < len(self.heap)

# Función para ejecutar todas las pruebas del reto 1.2
def test_1_2():
    # Se crea una instancia del MinHeap
    heap = MinHeap()
    # Se establece un heap de ejemplo manualmente
    heap.heap = [1, 3, 2, 7, 4, 5, 8]  # Heap con 7 elementos

    # Prueba 1.2.1: índice 4 debería tener como padre al índice 1
    record_test("1.2.1 Parent calculation", heap._parent_index(4) == 1)

    # Prueba 1.2.2: índice 1 debería tener hijos en los índices 3 y 4
    left_correct = heap._left_child_index(1) == 3  # Verifica hijo izquierdo
    right_correct = heap._right_child_index(1) == 4  # Verifica hijo derecho
    # Registra la prueba solo si ambos hijos son correctos
    record_test("1.2.2 Children calculation", left_correct and right_correct)

    # Prueba 1.2.3: el nodo raíz (índice 0) no debería tener padre
    record_test("1.2.3 Root node edge case", heap._parent_index(0) == -1 or heap._parent_index(0) is None)

    # Prueba 1.2.4: índice 1 debería tener ambos hijos existentes
    has_children = heap._has_left_child(1) and heap._has_right_child(1)
    record_test("1.2.4 Boundary validation", has_children)

    # Prueba 1.2.5: índice 6 no debería tener hijos (está al final del heap)
    no_children = not heap._has_left_child(6) and not heap._has_right_child(6)
    record_test("1.2.5 Invalid index handling", no_children)

# Ejecuta las pruebas definidas anteriormente
test_1_2()

# Imprime los resultados de las pruebas, una por línea
for r in test_results:
    print(r)