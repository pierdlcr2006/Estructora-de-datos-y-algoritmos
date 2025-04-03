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

        # Caso especial: insertar al principio de la lista
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

    def delete_from_end(self):
        """
        Elimina el último nodo de la lista enlazada y devuelve su valor.

        Returns:
            data: El valor del nodo eliminado, o None si la lista está vacía.
        """
        if self.head is None:
            return None  # Si la lista está vacía, no hay nada que eliminar

        if self.head.next is None:
            # Caso especial: solo hay un nodo en la lista
            data = self.head.data  # Guarda el valor del nodo
            self.head = None  # La lista queda vacía
            return data

        # Recorre la lista hasta el penúltimo nodo
        current = self.head
        while current.next and current.next.next:
            current = current.next

        # Guarda el valor del último nodo y lo elimina
        data = current.next.data
        current.next = None  # El penúltimo nodo ahora apunta a None
        return data

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
    print("Lista después de las inserciones:")
    ll.print_list()  # Debería mostrar: 10 → 15 → 20 → None

    # Elimina el último nodo de la lista
    eliminado = ll.delete_from_end()
    print(f"Nodo eliminado: {eliminado}")

    # Imprime los elementos de la lista enlazada después de la eliminación
    print("Lista después de eliminar el último nodo:")
    ll.print_list()  # Debería mostrar: 10 → 15 → None
