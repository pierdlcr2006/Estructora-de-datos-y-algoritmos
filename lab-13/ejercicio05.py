class MaxHeap:
    # 🦁 MaxHeap data structure using list
    def __init__(self):
        self.heap = []  # Inicializa una lista vacía para almacenar elementos del heap
    
    def insert(self, value):
        # Insert and heapify up for max-heap property
        self.heap.append(value)  # Agrega el nuevo valor al final de la lista
        self.heapify_up(len(self.heap) - 1)  # Llama heapify_up con el índice del último elemento
    
    def heapify_up(self, index):
        # Move up while parent < current
        if index == 0:  # Si el índice es 0, es la raíz, no tiene padre
            return  # Termina la recursión
        
        parent_index = (index - 1) // 2  # Calcula el índice del padre usando la fórmula
        
        # If current element is greater than parent, swap them
        if self.heap[index] > self.heap[parent_index]:  # Si el elemento actual es mayor que su padre
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  # Intercambia elementos
            self.heapify_up(parent_index)  # Recursivamente sube desde la nueva posición del elemento
    
    def delete_max(self):
        # Remove and return the largest (root) element
        if not self.heap:  # Si el heap está vacío
            return None  # Retorna None
        
        if len(self.heap) == 1:  # Si solo hay un elemento
            return self.heap.pop()  # Lo elimina y retorna directamente
        
        # Store the max value (root)
        max_value = self.heap[0]  # Guarda el valor máximo (raíz) antes de eliminarlo
        
        # Move last element to root
        self.heap[0] = self.heap.pop()  # Mueve el último elemento a la raíz y lo elimina del final
        
        # Heapify down from root
        self.heapify_down(0)  # Reorganiza el heap desde la raíz hacia abajo
        
        return max_value  # Retorna el valor máximo que se eliminó
    
    def heapify_down(self, index):
        # Move down while current < child
        left_child = 2 * index + 1  # Calcula el índice del hijo izquierdo
        right_child = 2 * index + 2  # Calcula el índice del hijo derecho
        largest = index  # Asume que el elemento actual es el más grande inicialmente
        
        # Find the largest among parent and children
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:  # Si hijo izquierdo existe y es mayor
            largest = left_child  # Actualiza el índice del elemento más grande
        
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:  # Si hijo derecho existe y es mayor
            largest = right_child  # Actualiza el índice del elemento más grande
        
        # If largest is not the parent, swap and continue heapifying
        if largest != index:  # Si el elemento más grande no es el padre actual
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]  # Intercambia elementos
            self.heapify_down(largest)  # Recursivamente baja desde la nueva posición

# 🧪 Test cases
def test_max_heap():
    h = MaxHeap()  # Crea una nueva instancia de MaxHeap
    h.insert(1)  # Inserta el valor 1 en el heap
    print("🦁 Test 1:", h.heap==[1])  # Verifica que el heap contenga solo [1]
    
    for v in [3,2,8,5]:  # Itera sobre los valores a insertar
        h.insert(v)  # Inserta cada valor en el heap
    print("🦁 Test 2:", h.heap[0]==max(h.heap))  # Verifica que la raíz sea el máximo elemento
    
    h.delete_max()  # Elimina el elemento máximo (raíz)
    print("🦁 Test 3:", h.heap[0]==max(h.heap))  # Verifica que la nueva raíz siga siendo el máximo
    
    h = MaxHeap()  # Crea un nuevo heap para el siguiente test
    for v in [5,3,1]:  # Inserta valores en orden descendente
        h.insert(v)  # Inserta cada valor
    h.delete_max()  # Elimina el máximo (5)
    print("🦁 Test 4:", h.heap==[3,1])  # Verifica que queden [3,1] en el heap
    
    h = MaxHeap()  # Crea otro heap nuevo
    h.insert(10)  # Inserta solo un elemento
    print("🦁 Test 5:", h.delete_max()==10 and h.heap==[])  # Verifica que retorne 10 y el heap quede vacío

# Ejecutar tests
test_max_heap()  # Llama a la función que ejecuta todos los tests