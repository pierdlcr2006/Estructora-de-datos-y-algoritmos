class MinHeap:
    # 📦 MinHeap data structure using list
    def __init__(self):
        # Initialize empty list for heap
        self.heap = []  # Crea una lista vacía que almacenará los elementos del heap
    
    def is_empty(self):
        # Return True if heap is empty
        return len(self.heap) == 0  # Retorna True si la longitud de la lista es 0 (vacía), False si contiene elementos

# 🧪 Test cases
def test_min_heap_init_and_empty():
    h = MinHeap()  # Crear una nueva instancia de MinHeap
    print("🌱 Test 1:", h.is_empty() == True)  # Verificar que el heap recién creado esté vacío
    h.heap.append(1)  # Agregar el elemento 1 directamente a la lista del heap
    print("🌱 Test 2:", h.is_empty() == False)  # Verificar que el heap ya no esté vacío
    h.heap.clear()  # Limpiar toda la lista, eliminando todos los elementos
    print("🌱 Test 3:", h.is_empty() == True)  # Verificar que después de clear() el heap esté vacío
    h.heap.extend([2,3,4])  # Agregar múltiples elementos [2,3,4] a la lista
    print("🌱 Test 4:", h.is_empty() == False)  # Verificar que con elementos el heap no esté vacío
    h.heap.pop(); h.heap.pop(); h.heap.pop()  # Eliminar todos los elementos uno por uno con pop()
    print("🌱 Test 5:", h.is_empty() == True)  # Verificar que después de eliminar todos los elementos esté vacío

test_min_heap_init_and_empty()  # Ejecutar la función de pruebas