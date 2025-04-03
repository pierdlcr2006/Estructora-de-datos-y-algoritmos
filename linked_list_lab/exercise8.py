class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def delete_from_position(self, position):
        if position < 0 or position >= self.length or self.head is None:
            return None

        if position == 0:
            return self.delete_from_beginning()

        if position == self.length - 1:
            return self.delete_from_end()

        current = self.head
        count = 0
        while count < position - 1:
            current = current.next
            count += 1

        node_to_delete = current.next
        data = node_to_delete.data
        current.next = node_to_delete.next
        self.length -= 1
        return data

    def delete_from_beginning(self):
        if self.head is None:
            return None  

        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data

    def delete_from_end(self):
        if self.head is None:
            return None  

        if self.head.next is None:
            data = self.head.data
            self.head = None  
            self.length -= 1
            return data

        current = self.head
        while current.next and current.next.next:
            current = current.next

        data = current.next.data
        current.next = None
        self.length -= 1
        return data

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
