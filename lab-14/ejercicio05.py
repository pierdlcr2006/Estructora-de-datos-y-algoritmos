# Lista que almacenará los resultados de las pruebas
test_results = []

# Función auxiliar para registrar si una prueba fue exitosa o falló
def record_test(test_name, condition):
    # Si la condición es verdadera, se marca como exitoso con ✅, si no con ❌
    emoji = "[OK]" if condition else "[X]"
    # Se guarda el resultado en la lista de pruebas
    test_results.append(f"{emoji} {test_name}")

# Definición de la clase MaxHeap
class MaxHeap:
    def __init__(self):
        # Inicializa el heap como una lista vacía
        self.heap = []

    def insert(self, value):
        # Inserta un nuevo valor al final del heap
        self.heap.append(value)
        # Reorganiza el heap hacia arriba para mantener la propiedad de max-heap
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        # Si el heap está vacío, no hay nada que eliminar
        if not self.heap:
            return None
        # Guarda el valor máximo (raíz del heap)
        max_value = self.heap[0]
        # Mueve el último elemento a la raíz
        self.heap[0] = self.heap[-1]
        # Elimina el último elemento
        self.heap.pop()
        # Reorganiza el heap hacia abajo para restaurar la propiedad de max-heap
        self._heapify_down(0)
        # Retorna el valor máximo eliminado
        return max_value

    def build_heap(self, array):
        # Copia los valores del arreglo al heap
        self.heap = array[:]
        # Comienza desde el último nodo no hoja y reorganiza hacia abajo
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):
        # Mientras no estemos en la raíz y el nodo actual sea mayor que su padre
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                # Intercambia el nodo con su padre
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                # Sube en el árbol
                index = parent
            else:
                # Si no necesita subir, se detiene
                break

    def _heapify_down(self, index):
        # Obtiene el tamaño del heap
        size = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            # Compara con el hijo izquierdo si existe
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            # Compara con el hijo derecho si existe
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            # Si el más grande no es el nodo actual, intercambia y sigue bajando
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

# Función que contiene todas las pruebas del reto
def test_1_5():
    heap = MaxHeap()

    # 1.5.1 Inserción: el valor más grande debe estar en la raíz
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)

    # 1.5.2 Eliminación del máximo: debe retornar el mayor valor
    max_val = heap.delete_max()
    record_test("1.5.2 MaxHeap deletion", max_val == 5)

    # 1.5.3 Construcción del heap desde un arreglo desordenado
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))

    # 1.5.4 Verificación de propiedad del heap: padres ≥ hijos
    valid_max_heap = all(
        heap.heap[i] >= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        and heap.heap[i] >= heap.heap[2*i+2] if 2*i+2 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.5.4 Heap property verification", valid_max_heap)

    # 1.5.5 Manejo de arreglo vacío en build_heap
    heap.build_heap([])
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)

# Ejecuta las pruebas
test_1_5()

# Imprime los resultados de cada prueba
for r in test_results:
    print(r)