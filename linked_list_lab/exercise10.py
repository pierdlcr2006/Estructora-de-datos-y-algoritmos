class Node:
    def __init__(self, data):
        # Inicializa un nodo con un valor (data) y un puntero al siguiente nodo (next)
        self.data = data
        self.next = None
    
    def get_data(self):
        # Devuelve el valor almacenado en el nodo
        return self.data
    
    def get_next(self):
        # Devuelve el siguiente nodo en la lista
        return self.next
    
    def set_next(self, new_next):
        # Establece el siguiente nodo en la lista
        self.next = new_next

class LinkedList:
    def __init__(self):
        # Inicializa una lista enlazada vacía
        self.head = None
    
    def append(self, data):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        
        Args:
            data: El valor que se almacenará en el nuevo nodo.
        """
        new_node = Node(data)  # Crea un nuevo nodo con el valor proporcionado
        if self.head is None:
            # Si la lista está vacía, el nuevo nodo será la cabeza
            self.head = new_node
            return
        current = self.head
        # Recorre la lista hasta encontrar el último nodo
        while current.get_next() is not None:
            current = current.get_next()
        # Establece el nuevo nodo como el siguiente del último nodo
        current.set_next(new_node)
    
    def get_length(self):
        """
        Calcula la longitud de la lista enlazada.
        
        Returns:
            int: El número de nodos en la lista.
        """
        count = 0
        current = self.head
        # Recorre la lista y cuenta los nodos
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def get_nth_from_end(self, n):
        """
        Obtiene el valor del nodo que está en la posición n desde el final de la lista.
        
        Args:
            n (int): La posición desde el final (1 basado en 1).
        
        Returns:
            data: El valor del nodo en la posición n desde el final, o None si la posición es inválida.
        """
        length = self.get_length()  # Calcula la longitud de la lista
        if n <= 0 or n > length:
            # Si la posición es inválida, devuelve None
            return None
        
        position = length - n  # Calcula la posición desde el inicio
        current = self.head
        count = 0
        
        # Recorre la lista hasta la posición deseada
        while count < position:
            current = current.get_next()
            count += 1
        
        return current.get_data()  # Devuelve el valor del nodo en la posición deseada

# Ejemplo de uso
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

# Imprime el valor del nodo en la posición n desde el final
print(linked_list.get_nth_from_end(2))  # Salida: 40
print(linked_list.get_nth_from_end(5))  # Salida: 10
print(linked_list.get_nth_from_end(6))  # Salida: None
