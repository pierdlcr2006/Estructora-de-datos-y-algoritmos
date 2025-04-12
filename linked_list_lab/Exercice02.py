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
        last.next = neLa implementación con listas enlazadas me pareció interesante porque te da más flexibilidad en la memoria. No tienes que predecir el tamaño de la pila con anticipación y, al insertar o eliminar, puedes ajustar las referencias sin mover todos los elementos, lo que puede ser más eficiente en ciertos casos. Sin embargo, las implementaciones con arreglos pueden ser más rápidas para acceder a los elementos y son más simples de gestionar si el tamaño es fijo o relativamente pequeño.﻿w_node

    def list_length(self):
        """
        Calcula la longitud de la lista enlazada.
        
        Returns:
            int: El número de nodos en la lista.
        """
        count = 0
        current = self.headS
        # Recorre la lista y cuenta los nodos
        while current is not None:
            count += 1
            current = current.next
        return count

# Bloque principal
lista = LinkedList()

# Agrega nodos a la lista enlazada
lista.append(10)
lista.append(20)
lista.append(30)
lista.append(35)

# Imprime el número de nodos en la lista enlazada
print("Número de nodos:", lista.list_length())
