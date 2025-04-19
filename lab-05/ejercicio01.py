class QueueWithTwoStacks:
    """Implementación de cola usando dos pilas."""

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        """Agrega un elemento al final de la cola."""
        self.stack_in.append(item)

    def dequeue(self):
        """Elimina y retorna el elemento al frente."""
        if self.is_empty():
            raise IndexError("La cola está vacía")

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        """Muestra el elemento al frente sin eliminarlo."""
        if self.is_empty():
            raise IndexError("La cola está vacía")

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return not self.stack_in and not self.stack_out

    def size(self):
        """Retorna el número de elementos."""
        return len(self.stack_in) + len(self.stack_out)


# 🧪 Prueba
if __name__ == "__main__":
    q = QueueWithTwoStacks()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.dequeue())  # 10
    q.enqueue(40)
    print(q.peek())     # 20
    print(q.dequeue())  # 20
