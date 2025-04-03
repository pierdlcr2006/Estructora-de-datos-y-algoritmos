class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)
    
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def get_nth_from_end(self, n):
        length = self.get_length()
        if n <= 0 or n > length:
            return None
        
        position = length - n
        current = self.head
        count = 0
        
        while count < position:
            current = current.get_next()
            count += 1
        
        return current.get_data()

# Example Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

print(linked_list.get_nth_from_end(2))  # Output: 40
print(linked_list.get_nth_from_end(5))  # Output: 10
print(linked_list.get_nth_from_end(6))  # Output: None
