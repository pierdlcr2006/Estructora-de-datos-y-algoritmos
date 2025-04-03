class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def list_length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def clear(self):
        self.head = None
        return True  

lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(30)

print("Number of nodes before clearing:", lista.list_length())

lista.clear()

print("Number of nodes after clearing:", lista.list_length())  
