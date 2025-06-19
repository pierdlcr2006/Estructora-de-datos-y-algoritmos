# Lista para almacenar resultados de los tests
test_results = []

# Registra el resultado de un test con su nombre y condición (True/False)
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# Clase que implementa un montículo mínimo (min-heap)
class MinHeap:
    def __init__(self):
        self.heap = []  # Lista interna que representa el heap

    def insert(self, value):
        self.heap.append(value)  # Agrega el nuevo valor al final
        self._heapify_up(len(self.heap) - 1)  # Aplica heapify hacia arriba desde última posición

    def _heapify_up(self, index):
        while index > 0:  # Mientras no esté en la raíz
            parent = self._parent_index(index)  # Calcula el índice del padre
            if self.heap[index] < self.heap[parent]:  # Si el hijo es menor que el padre
                # Intercambia hijo y padre
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent  # Actualiza el índice para continuar hacia arriba
            else:
                break  # Si el orden es correcto, detiene

    def _parent_index(self, index):
        return (index - 1) // 2 if index > 0 else -1  # Calcula el índice del padre

    def size(self):
        return len(self.heap)  # Devuelve el tamaño del heap

    def peek(self):
        return self.heap[0] if self.heap else None  # Retorna la raíz (mínimo), si existe

# Ejecuta todos los tests requeridos
def test_1_3():
    heap = MinHeap()  # Crea una instancia vacía del heap

    # 1.3.1 Inserción de un solo elemento
    heap.insert(5)
    record_test("1.3.1 Single element insertion", heap.heap == [5])

    # 1.3.2 Múltiples inserciones
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    record_test("1.3.2 Multiple insertions", len(heap.heap) == 4)

    # 1.3.3 Seguimiento del mínimo (debe estar en la raíz)
    record_test("1.3.3 Minimum tracking", heap.peek() == 1)

    # 1.3.4 Validación de la propiedad del heap
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        and heap.heap[i] <= heap.heap[2*i+2] if 2*i+2 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.3.4 Heap property validation", valid_heap)

    # 1.3.5 Consistencia del tamaño
    record_test("1.3.5 Size consistency", heap.size() == 4)

# Ejecuta los tests
test_1_3()

# Muestra el resumen de resultados
for r in test_results:
    print(r)