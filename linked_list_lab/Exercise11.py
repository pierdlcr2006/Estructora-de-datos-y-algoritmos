class Node:
    def __init__(self, data):
        # Inicializa un nodo con un valor (data) y un puntero al siguiente nodo (next)
        self.data = data
        self.next = None

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
        if not self.head:
            # Si la lista está vacía, el nuevo nodo será la cabeza
            self.head = new_node
            return
        last = self.head
        # Recorre la lista hasta encontrar el último nodo
        while last.next:
            last = last.next
        # Establece el nuevo nodo como el siguiente del último nodo
        last.next = new_node

    def list_length(self):
        """
        Calcula la longitud de la lista enlazada.
        
        Returns:
            int: El número de nodos en la lista.
        """
        count = 0
        current = self.head
        # Recorre la lista y cuenta los nodos
        while current is not None:
            count += 1
            current = current.next
        return count

    def clear(self):
        """
        Elimina todos los nodos de la lista enlazada.
        
        Returns:
            bool: True si la operación se realizó con éxito.
        """
        self.head = None  # Establece la cabeza como None, eliminando la referencia a los nodos
        return True  

# Ejemplo de uso
lista = LinkedList()
lista.append(10)  # Agrega 10 a la lista
lista.append(20)  # Agrega 20 a la lista
lista.append(30)  # Agrega 30 a la lista

# Imprime el número de nodos antes de limpiar la lista
print("Número de nodos antes de limpiar:", lista.list_length())  # Salida: 3

# Limpia la lista
lista.clear()

# Imprime el número de nodos después de limpiar la lista
print("Número de nodos después de limpiar:", lista.list_length())  # Salida: 0
