class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_position(self, position, data):
        """Inserts a new node at a specific position in the list."""
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                return  
            current = current.next

        if current is None:
            return  

        new_node.next = current.next
        current.next = new_node

    def delete_from_end(self):
        """Deletes the last node from the list and returns its value."""
        if self.head is None:
            return None 

        if self.head.next is None:
            data = self.head.data
            self.head = None  
            return data

        current = self.head
        while current.next and current.next.next:
            current = current.next

        data = current.next.data 
        current.next = None 
        return data 

    def print_list(self):
        """Prints the linked list."""
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
