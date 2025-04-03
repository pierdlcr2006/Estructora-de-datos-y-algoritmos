class Node:
    def __init__(self, data=None):
        # Inicializa un nodo con un valor (data) y un puntero al siguiente nodo (next)
        self.data = data
        self.next = None

    def get_data(self):
        # Devuelve el valor almacenado en el nodo
        return self.data
    
    def set_data(self, data):
        # Establece un nuevo valor para el nodo
        self.data = data

    def get_next(self):
        # Devuelve el siguiente nodo en la lista
        return self.next
    
    def set_next(self, next_node):
        # Establece el siguiente nodo en la lista
        self.next = next_node

class LinkedList:

    def __init__(self):
        # Inicializa una lista enlazada vacía
        self.head = None
    
    def display(self):
        """
        Muestra todos los elementos de la lista enlazada.
        
        Returns:
            str: Una representación en forma de cadena de la lista enlazada
        """
        if self.head is None:
            # Si la lista está vacía, devuelve un mensaje indicando esto
            return "Lista vacía"
        
        current = self.head
        result = ""
        
        # Recorre la lista enlazada y construye una cadena con los valores de los nodos
        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()
        
        # Agrega "None" al final para indicar el final de la lista
        return result + "None"

if __name__ == "__main__":
    # Crea tres nodos con valores 10, 20 y 30
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    
    # Conecta los nodos entre sí
    node1.set_next(node2)
    node2.set_next(node3)
    
    # Crea una lista enlazada y establece el primer nodo como la cabeza
    linked_list = LinkedList()
    linked_list.head = node1
    
    # Muestra los elementos de la lista enlazada
    print(linked_list.display())



