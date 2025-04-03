class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, position, data):
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

    def delete_from_beginning(self):
        if self.head is None:
            return None 

        data = self.head.data  
        self.head = self.head.next  
        return data 

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
