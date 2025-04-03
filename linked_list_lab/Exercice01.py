class Node:
    def __init__(self, data=None):

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

class LinkedList:

    def __init__(self):
        self.head = None
    
    def display(self):
        """
    Display all elements in the linked list.
    
    Returns:
        str: A string representation of the linked list
    """
        if self.head is None:
            return "Empty list"
        
        current = self.head
        result = ""
        
        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()
        
        return result + "None"

if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    
    node1.set_next(node2)
    node2.set_next(node3)
    
    linked_list = LinkedList()
    linked_list.head = node1
    
    print(linked_list.display())



