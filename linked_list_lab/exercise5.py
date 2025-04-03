class Node:
    def __init__(self, data):
        # Inicializa un nodo con un valor (data) y un puntero al siguiente nodo (next)
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Inicializa una lista enlazada vacía
        self.head = None

    def insert_at_position(self, position, data):
        """
        Inserta un nuevo nodo en una posición específica de la lista enlazada.
        
        Args:
            position (int): La posición donde se insertará el nuevo nodo (basada en 0).
            data: El valor que se almacenará en el nuevo nodo.
        """
        new_node = Node(data)  # Crea un nuevo nodo con el valor proporcionado

        # Inserta al principio de la lista
        if position == 0:
            new_node.next = self.head  # El nuevo nodo apunta al nodo que era la cabeza
            self.head = new_node  # Actualiza la cabeza para que sea el nuevo nodo
            return
        
        # Recorre la lista hasta el nodo anterior a la posición deseada
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return  # Posición inválida (mayor que la longitud de la lista)
            current = current.next

        if current is None:
            return  # Posición inválida

        # Inserta el nuevo nodo en la posición deseada
        new_node.next = current.next  # El nuevo nodo apunta al siguiente nodo
        current.next = new_node  # El nodo actual apunta al nuevo nodo

    def print_list(self):
        """
        Imprime los elementos de la lista enlazada.
        """
        current = self.head  # Comienza desde la cabeza de la lista
        while current:
            # Imprime el valor del nodo actual seguido de " → "
            print(current.data, end=" → ")
            current = current.next  # Avanza al siguiente nodo
        print("None")  # Indica el final de la lista


if __name__ == "__main__":
    # Crea una nueva lista enlazada
    ll = LinkedList()

    # Inserta nodos en posiciones específicas
    ll.insert_at_position(0, 10)  # Inserta 10 en la posición 0
    ll.insert_at_position(1, 20)  # Inserta 20 en la posición 1
    ll.insert_at_position(1, 15)  # Inserta 15 en la posición 1

    # Imprime los elementos de la lista enlazada
    ll.print_list()  # Debería mostrar: 10 → 15 → 20 → None
