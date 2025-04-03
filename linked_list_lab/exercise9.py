class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        # Devuelve el dato almacenado en el nodo
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
        """Agrega un nuevo nodo al final de la lista."""
        new_node = Node(data)
        if self.head is None:
            # Si la lista está vacía, el nuevo nodo será la cabeza
            self.head = new_node
            return
        current = self.head
        while current.get_next() is not None:
            # Recorre la lista hasta encontrar el último nodo
            current = current.get_next()
        # Establece el nuevo nodo como el siguiente del último nodo
        current.set_next(new_node)

    def search(self, data):
        """
        Busca un valor en la lista enlazada.
        
        Args:
            data: El valor a buscar.
        
        Returns:
            int: La posición de la primera ocurrencia del valor (basado en 0),
                 o -1 si no se encuentra.
        """
        if self.head is None:
            # Si la lista está vacía, devuelve -1
            return -1
        
        current = self.head
        position = 0
        # Recorre la lista buscando el valor
        # y contando la posición de cada nodo
        # hasta que se encuentre el valor o se llegue al final de la lista 
        
        while current is not None:
            # Compara el dato actual con el valor buscado
            if current.get_data() == data:
                return position
            current = current.get_next()
            position += 1
        
        # Si no se encuentra el valor, devuelve -1
        return -1


# Ejemplo de uso
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print(linked_list.search(30))
print(linked_list.search(50))  
print(linked_list.search(10))
print(linked_list.search(40))
print(linked_list.search(20))
print(linked_list.search(100))  
