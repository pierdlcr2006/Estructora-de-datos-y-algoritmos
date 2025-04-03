class Node:
    def __init__(self, data=None):
        # Inicializa un nodo con un valor (data) y un puntero al siguiente nodo (next)
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Inicializa una lista enlazada vacía
        self.head = None

    def insert_at_end(self, data):
        """
        Inserta un nuevo nodo al final de la lista enlazada.
        
        Args:
            data: El valor que se almacenará en el nuevo nodo.
        
        Returns:
            bool: True si la operación se realizó con éxito.
        """
        new_node = Node(data)  # Crea un nuevo nodo con el valor proporcionado

        if self.head is None:
            # Si la lista está vacía, el nuevo nodo será la cabeza
            self.head = new_node
            return True

        current = self.head
        # Recorre la lista hasta encontrar el último nodo
        while current.next:
            current = current.next

        # Establece el nuevo nodo como el siguiente del último nodo
        current.next = new_node
        return True

    def display(self):
        """
        Muestra todos los elementos de la lista enlazada.
        """
        current = self.head  # Comienza desde la cabeza de la lista
        while current:
            # Imprime el valor del nodo actual seguido de " -> "
            print(current.data, end=" -> ")
            current = current.next  # Avanza al siguiente nodo
        print("None")  # Indica el final de la lista

# Pruebas
ll = LinkedList()  # Crea una nueva lista enlazada
ll.insert_at_end(10)  # Inserta 10 al final
ll.insert_at_end(20)  # Inserta 20 al final
ll.insert_at_end(30)  # Inserta 30 al final

ll.display()  # Muestra los elementos de la lista enlazada