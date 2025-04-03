class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Agrega un nuevo nodo al final de la lista."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def search(self, data):
        """
        Busca un valor en la lista enlazada.
        
        Args:
            data: El valor a buscar.
        
        Returns:
            int: La posición de la primera ocurrencia del valor (0-based),
                 o -1 si no se encuentra.
        """
        if self.head is None:
            return -1
        
        current = self.head
        position = 0
        
        while current is not None:
            if current.get_data() == data:
                return position
            current = current.get_next()
            position += 1
        
        return -1


# Ejemplo de uso
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print(linked_list.search(30))  # Salida: 2
print(linked_list.search(50))  # Salida: -1
