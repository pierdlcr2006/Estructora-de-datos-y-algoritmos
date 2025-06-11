class MinHeap:
    def __init__(self):
        self.heap = []  # Inicializar la lista vacía que representará el heap
    
    def delete_min(self):
        # Método para eliminar y retornar el elemento más pequeño (raíz)
        
        # Verificar si el heap está vacío
        if not self.heap:
            return None  # Retornar None si no hay elementos
        
        # Caso especial: si solo hay un elemento en el heap
        if len(self.heap) == 1:
            return self.heap.pop()  # Eliminar y retornar el único elemento
        
        # Guardar el valor mínimo (siempre está en la posición 0 - raíz)
        min_val = self.heap[0]
        
        # Mover el último elemento del heap a la posición de la raíz
        self.heap[0] = self.heap.pop()  # pop() elimina y retorna el último elemento
        
        # Restaurar la propiedad del heap llamando heapify_down desde la raíz
        self.heapify_down(0)  # Empezar desde el índice 0 (raíz)
        
        # Retornar el valor mínimo que se eliminó
        return min_val
    
    def heapify_down(self, index):
        # Método para restaurar la propiedad del heap hacia abajo (desde un nodo hacia sus hijos)
        
        # Calcular el índice del hijo izquierdo usando la fórmula 2*i + 1
        left_child = 2 * index + 1
        
        # Calcular el índice del hijo derecho usando la fórmula 2*i + 2
        right_child = 2 * index + 2
        
        # Asumir inicialmente que el nodo actual es el más pequeño
        smallest = index
        
        # Verificar si el hijo izquierdo existe y es menor que el nodo actual
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child  # Actualizar el índice del elemento más pequeño
        
        # Verificar si el hijo derecho existe y es menor que el elemento más pequeño actual
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child  # Actualizar el índice del elemento más pequeño
        
        # Si el elemento más pequeño no es el nodo actual, necesitamos intercambiar
        if smallest != index:
            # Intercambiar el nodo actual con el hijo más pequeño
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            
            # Llamar recursivamente heapify_down en la nueva posición del elemento intercambiado
            self.heapify_down(smallest)  # Continuar heapificando desde la nueva posición

# 🧪 Test cases
def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)
    h.heap=[1]; print("🧹 Test 2:", h.delete_min()==1 and h.heap==[])
    h.heap=[1,3,2]; print("🧹 Test 3:", h.delete_min()==1 and h.heap==[2,3])
    h.heap=[1,3,4,5]; print("🧹 Test 4:", h.delete_min()==1 and h.heap==[3,5,4])
    h.heap=[1,2,3,4,5]
    print("🧹 Test 5:", h.delete_min()==1)

test_min_heap_delete_min()