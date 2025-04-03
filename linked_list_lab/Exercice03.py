class Node:
    """Un nodo en una lista enlazada."""

    def __init__(self, data=None):
        """Inicializa un nuevo nodo."""
        self.data = data  # Almacena el valor del nodo
        self.next = None  # Apunta al siguiente nodo en la lista (o None si es el último)

class LinkedList:
    """Una clase simple para una lista enlazada."""

    def __init__(self):
        """Inicializa una lista enlazada vacía."""
        self.head = None  # La cabeza de la lista enlazada (primer nodo)

    def insert_at_beginning(self, data):
        """
        Inserta un nuevo nodo al principio de la lista enlazada.
        
        Args:
            data: El valor que se almacenará en el nuevo nodo.
        """
        new_node = Node(data)  # Crea un nuevo nodo con el valor proporcionado
        new_node.next = self.head  # El nuevo nodo apunta al nodo que era la cabeza
        self.head = new_node  # Actualiza la cabeza para que sea el nuevo nodo

    def display(self):
        """
        Muestra todos los elementos de la lista enlazada.
        
        Returns:
            str: Una representación en forma de cadena de la lista enlazada.
        """
        current = self.head  # Comienza desde la cabeza de la lista
        result = ""  # Cadena para almacenar la representación de la lista
        while current:
            # Agrega el valor del nodo actual a la cadena
            result += f"[{current.data}] -> "
            current = current.next  # Avanza al siguiente nodo
        result += "None"  # Indica el final de la lista
        return result

# Prueba de la implementación
if __name__ == "__main__":
    linked_list = LinkedList()  # Crea una nueva lista enlazada
    linked_list.insert_at_beginning(15)  # Inserta 15 al principio
    linked_list.insert_at_beginning(16)  # Inserta 16 al principio
    linked_list.insert_at_beginning(20)  # Inserta 20 al principio

    # Muestra los elementos de la lista enlazada
    print(linked_list.display())
