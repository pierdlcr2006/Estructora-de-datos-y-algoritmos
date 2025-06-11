class MinHeap:
    def __init__(self):
        self.heap = []  # Inicializa una lista vacía para almacenar los elementos del heap
    
    def insert(self, value):
        # Método para insertar un valor y mantener la propiedad del min-heap
        self.heap.append(value)  # Agrega el nuevo valor al final de la lista (última posición del heap)
        self.heapify_up(len(self.heap) - 1)  # Llama a heapify_up con el índice del último elemento insertado
    
    def heapify_up(self, index):
        # Método para mover un elemento hacia arriba hasta restaurar la propiedad del heap
        while index > 0:  # Continúa mientras no hayamos llegado a la raíz (índice 0)
            parent_index = (index - 1) // 2  # Calcula el índice del padre usando la fórmula estándar
            
            # Verifica si la propiedad del min-heap está satisfecha (padre <= hijo)
            if self.heap[parent_index] <= self.heap[index]:
                break  # Si el padre es menor o igual, la propiedad está cumplida, salir del loop
            
            # Intercambia el elemento actual con su padre usando asignación múltiple
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            
            index = parent_index  # Actualiza el índice al del padre para continuar subiendo

# 🧪 Test cases
def test_min_heap_insert():
    h = MinHeap()  # Crea una nueva instancia del MinHeap
    h.insert(5); print("🍀 Test 1:", h.heap == [5])  # Inserta 5, verifica que el heap sea [5]
    h.insert(3); print("🍀 Test 2:", h.heap == [3,5])  # Inserta 3, debe subir y quedar [3,5]
    h.insert(4); print("🍀 Test 3:", h.heap == [3,5,4])  # Inserta 4, se queda en su lugar [3,5,4]
    h.insert(1); print("🍀 Test 4:", h.heap == [1,3,4,5])  # Inserta 1, sube hasta la raíz [1,3,4,5]
    
    # 🍀 Test 5: Verifica que cada padre sea menor o igual que sus hijos (propiedad min-heap)
    valid = all(  # all() retorna True solo si todas las condiciones son verdaderas
        (h.heap[i] <= h.heap[2*i+1] if 2*i+1 < len(h.heap) else True)  # Verifica hijo izquierdo si existe
        and (h.heap[i] <= h.heap[2*i+2] if 2*i+2 < len(h.heap) else True)  # Verifica hijo derecho si existe
        for i in range(len(h.heap))  # Itera sobre todos los índices del heap
    )
    print("🍀 Test 5:", valid)  # Imprime si la propiedad del min-heap se mantiene

test_min_heap_insert()  # Ejecuta todos los tests