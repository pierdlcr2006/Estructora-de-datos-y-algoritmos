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

        # Insert at the beginning
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Traverse the list to the node before the desired position
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return  # Invalid position (greater than the length of the list)
            current = current.next

        if current is None:
            return  # Invalid position

        # Insert the new node
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        """Prints the linked list."""
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

chucooo