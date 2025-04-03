<p align="center">
<img src="../img/tecsupLogo.png" align="center"> 
</p>

# Algoritmos y Estructuras de Datos  
## Lab03: Linked lists

## Capacidades

- Definir las reglas básicas para la creación de listas enlazadas.

## Seguridad

- Generar un ambiente seguro
- Evitar el consumo de alimentos
- Dejar el ambiente ordenado y limpio

## Preparación

- El alumno debe revisar previamente el material cargado

## Recursos

- Computadora

## Instrucciones

Cada integrante del grupo debe seleccionar un ejercicio diferente y desarrollarlo con la siguiente estructura.

- **Nombre del alumno**
- **Ejercicio a desarrollar**
- **Prompt engineering**

    - Prompt ingresado y captura
    - Análisis del prompt
    - Ajustes de prompt y captura
    - Comentarios de los compañeros

- **Código**
    - Código desarrollado
    - Análisis del código
    - Comentarios de los compañeros

Desarrollar todo el código en inglés

# Linked Lists Laboratory 

## Introduction

Welcome to the Linked Lists Laboratory! In this lab, you'll gain hands-on experience implementing and working with linked lists in Python. This step-by-step guide will help you understand the core concepts of linked lists and their operations.

## Learning Objectives

By the end of this lab, you should be able to:

1. Implement a singly linked list data structure
2. Understand the basic operations of linked lists
3. Analyze the time and space complexity of different operations
4. Apply linked lists to solve practical problems

# Part 1: The Node Class
 
``` python

    class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

```

# Part 2: The LinkedList Class

``` Python

    from .node import Node

    class LinkedList:
        def __init__(self):
            self.head = None

```

# Part3: Basic Operations

## Exercise 1: Displaying the List

Implement a method to display all elements in the list.

```Python

def display(self):
        current = self.head
        while current:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print("None")

```

## Exercise 2: Counting Nodes

Implement a method to count the number of nodes in the linked list.

```Python

    def list_length(self):
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.get_next()
            return count

```

## Exercise 3: Insertion at the Beginning

Implement a method to insert a new node at the beginning of the list.

```Python

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

```

## Exercise 4: Insertion at the End

Implement a method to insert a new node at the end of the list.


``` Python

    def insert_at_end(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.get_next():
                    current = current.get_next()
                current.set_next(new_node)

```

## Exercise 5: Insertion at a Specific Position

Implement a method to insert a new node at a specific position in the list.


``` Python

      def insert_at_position(self, position, data):
        """Insert a new node at the specified position (0-based)."""
        # Check if position is valid
        if position < 0 or position > self.length:
            return False

        # Insert at the beginning
        if position == 0:
            return self.insert_at_beginning(data)

        # Insert at the end
        if position == self.length:
            return self.insert_at_end(data)

        # Insert at the middle
        new_node = Node(data)
        current = self.head
        count = 0

        # Traverse to the node just before the insertion point
        while count < position - 1:
            current = current.get_next()
            count += 1

        new_node.set_next(current.get_next())
        current.set_next(new_node)

        self.length += 1
        return True

```

# Part 4: More Advanced Operations

## Exercise 6: Deletion from the Beginning

Implement a method to delete a node from the beginning of the list.

```Python
    
    def delete_from_beginning(self):
    """Delete and return the data from the first node."""
    if self.head is None:
        return None
    
    data = self.head.get_data()
    self.head = self.head.get_next()
    self.length -= 1
    
    return data
    
```

## Exercise 7: Deletion from the End

Implement a method to delete a node from the end of the list.

```Python

    def delete_from_end(self):
        """Delete and return the data from the last node."""
        if self.head is None:
            return None

        # If there's only one node
        if self.head.get_next() is None:
            data = self.head.get_data()
            self.head = None
            self.length -= 1
            return data

        current = self.head

        # Traverse to the second-to-last node
        while current.get_next().get_next() is not None:
            current = current.get_next()

        data = current.get_next().get_data()
        current.set_next(None)
        self.length -= 1

        return data

```

## Exercise 8: Deletion from a Specific Position

Implement a method to delete a node from a specific position in the list.

``` Python

     def delete_from_position(self, position):
        """Delete and return data from node at the specified position."""
        # Check if position is valid
        if position < 0 or position >= self.length or self.head is None:
            return None

        # Delete from the beginning
        if position == 0:
            return self.delete_from_beginning()

        # Delete from the end
        if position == self.length - 1:
            return self.delete_from_end()

        # Delete from the middle
        current = self.head
        count = 0

        # Traverse to the node just before the deletion point
        while count < position - 1:
            current = current.get_next()
            count += 1

        node_to_delete = current.get_next()
        data = node_to_delete.get_data()

        current.set_next(node_to_delete.get_next())
        self.length -= 1

        return data

    def search(self, data):
        """Find the position of data in the list, or return -1 if not found."""
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

```

## Exercise 10: Finding the Nth Node from the End

Implement a method to find the nth node from the end of the list.

``` Python

    def get_nth_from_end(self, n):
        """Return the data of the nth node from the end (1-based indexing)."""
        if n <= 0 or n > self.length or self.head is None:
            return None

        # The nth node from the end is the (length-n+1)th node from the beginning
        position = self.length - n

        current = self.head
        count = 0

        while count < position:
            current = current.get_next()
            count += 1

        return current.get_data()

```

## Exercise 11: Clearing the List

Implement a method to clear all nodes from the list.

``` Python

    def clear(self):
        """Remove all nodes from the list."""
        self.head = None
        self.length = 0
        return True

```

# Part 5: Testing Your Implementation

