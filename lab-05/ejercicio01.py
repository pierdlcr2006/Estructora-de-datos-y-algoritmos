class QueueWithTwoStacks:
    def __init__(self):
        self.stack_in = []  # Stack for enqueue operations
        self.stack_out = []  # Stack for dequeue operations

    def enqueue(self, value):
        self.stack_in.append(value)  # Add element to the enqueue stack

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        
        # If the dequeue stack is empty, transfer all elements from the enqueue stack
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())  # Reverse the order
            
        return self.stack_out.pop()  # Remove and return the front element

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        
        # If the dequeue stack is empty, transfer all elements from the enqueue stack
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())  # Reverse the order
        
        return self.stack_out[-1]  # Look at the front element without removing it

    def isEmpty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0  # Queue is empty if both stacks are empty

    def size(self):
        return len(self.stack_in) + len(self.stack_out)  # Total size is sum of elements in both stacks


# Example usage
queue = QueueWithTwoStacks()
queue.enqueue(1)
print("Después de enqueue(1):", "Tamaño:", queue.size())

queue.enqueue(2)
print("Después de enqueue(2):", "Tamaño:", queue.size())

queue.enqueue(3)
print("Después de enqueue(3):", "Tamaño:", queue.size())

dequeued = queue.dequeue()
print("Elemento extraído (dequeue):", dequeued)

front_element = queue.peek()
print("Elemento al frente (peek):", front_element)

current_size = queue.size()
print("Tamaño actual de la cola:", current_size)

# También puedes imprimir varias operaciones juntas
print("\nResultado de operaciones múltiples:")
print("dequeue():", queue.dequeue())
print("peek():", queue.peek())
print("size():", queue.size())
