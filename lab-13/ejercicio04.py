class MinHeap:
    def __init__(self):
        self.heap = []  # Inicializar lista vacía para almacenar el heap
    
    def build_heap(self, array):
        """Transform array into a min-heap in-place in O(n) time"""
        # 🔄 Copiar el array al atributo heap de la clase
        self.heap = array.copy()
        
        # Si el array está vacío o tiene solo un elemento, ya es un heap válido
        if len(self.heap) <= 1:
            return  # Salir de la función, no hay nada que hacer
        
        # 📍 Calcular el índice del último nodo que no es hoja
        # Fórmula: (longitud_total // 2) - 1
        last_non_leaf = (len(self.heap) // 2) - 1
        
        # 🔨 Iterar desde el último nodo no-hoja hacia la raíz (índice 0)
        # range(inicio, fin, paso) donde paso=-1 significa ir hacia atrás
        for i in range(last_non_leaf, -1, -1):
            self.heapify_down(i)  # Aplicar heapify_down a cada nodo
    
    def heapify_down(self, index):
        """Restore heap property by moving element down the tree"""
        heap_size = len(self.heap)  # Obtener el tamaño total del heap
        
        # Bucle infinito que se rompe cuando se satisface la propiedad del heap
        while True:
            smallest = index  # Asumir que el nodo actual es el más pequeño
            left_child = 2 * index + 1   # Calcular índice del hijo izquierdo
            right_child = 2 * index + 2  # Calcular índice del hijo derecho
            
            # Verificar si el hijo izquierdo existe y es menor que el actual más pequeño
            if (left_child < heap_size and  # El hijo izquierdo existe
                self.heap[left_child] < self.heap[smallest]): # Y es menor
                smallest = left_child  # Actualizar el índice del más pequeño
            
            # Verificar si el hijo derecho existe y es menor que el actual más pequeño
            if (right_child < heap_size and  # El hijo derecho existe
                self.heap[right_child] < self.heap[smallest]): # Y es menor
                smallest = right_child  # Actualizar el índice del más pequeño
            
            # Si ningún hijo es menor, la propiedad del heap se satisface
            if smallest == index:
                break  # Salir del bucle while
            
            # Intercambiar el nodo actual con el hijo más pequeño
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest  # Mover el índice al hijo con el que se intercambió

# 🧪 Test cases - Casos de prueba para verificar el funcionamiento
def test_build_heap():
    h = MinHeap()  # Crear una nueva instancia de MinHeap
    
    # Test 1: Array [5,3,8,1,2] - el mínimo (1) debe estar en la raíz
    h.build_heap([5,3,8,1,2])  # Construir heap desde el array
    print("🔨 Test 1:", h.heap[0]==1)  # Verificar que la raíz sea 1
    
    # Test 2: Array [7,6,5,4,3,2,1] - el mínimo (1) debe estar en la raíz
    h.build_heap([7,6,5,4,3,2,1])  # Construir heap desde el array
    print("🔨 Test 2:", h.heap[0]==1)  # Verificar que la raíz sea 1
    
    # Test 3: Array [2,1] - debe resultar en [1,2]
    h.build_heap([2,1])  # Construir heap desde el array
    print("🔨 Test 3:", h.heap==[1,2])  # Verificar el orden completo
    
    # Test 4: Array [10] - un solo elemento, debe permanecer igual
    h.build_heap([10])  # Construir heap desde el array
    print("🔨 Test 4:", h.heap==[10])  # Verificar que permanezca [10]
    
    # Test 5: Array [] - array vacío, debe permanecer vacío
    h.build_heap([])  # Construir heap desde array vacío
    print("🔨 Test 5:", h.heap==[])  # Verificar que permanezca vacío

# Ejecutar todos los tests
test_build_heap()

# Ejemplo adicional para mostrar el funcionamiento paso a paso
print("\n🔍 Ejemplo paso a paso:")
h = MinHeap()  # Crear nueva instancia
print("Array original: [5,3,8,1,2]")  # Mostrar array inicial
h.build_heap([5,3,8,1,2])  # Construir el heap
print("Min-heap resultante:", h.heap)  # Mostrar heap final
# Mostrar el mínimo (siempre en la raíz - índice 0)
print("Mínimo (raíz):", h.heap[0] if h.heap else "Heap vacío")