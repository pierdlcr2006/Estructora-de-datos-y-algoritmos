class Node:
    """A Node in a linked list."""

    def __init__(self, data=None):
        """Initialize a new Node."""
        self.data = data
        self.next = None

class LinkedList:
    """A simple linked list class."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """Display all elements in the linked list."""
        current = self.head
        result = ""
        while current:
            result += f"[{current.data}] -> "
            current = current.next
        result += "None"
        return result

# Testing the implementation
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(15)
    linked_list.insert_at_beginning(16)
    linked_list.insert_at_beginning(20)

    print(linked_list.display())
