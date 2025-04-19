class PriorityQueue:
    """Implementación de una cola con prioridad."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, item, priority):
        """Inserta un elemento con su prioridad."""
        self.items.append((priority, item))

    def peek(self):
        """Devuelve el elemento de mayor prioridad sin eliminarlo."""
        if self.is_empty():
            raise IndexError("La cola está vacía")

        highest = self.items[0]
        for pair in self.items:
            if pair[0] > highest[0]:
                highest = pair
        return highest[1]

    def dequeue(self):
        """Elimina y devuelve el elemento de mayor prioridad."""
        if self.is_empty():
            raise IndexError("La cola está vacía")

        max_idx = 0
        for i in range(1, len(self.items)):
            if self.items[i][0] > self.items[max_idx][0]:
                max_idx = i
        return self.items.pop(max_idx)[1]


# 🧪 Prueba
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Tarea1", 2)
    pq.enqueue("TareaUrgente", 5)
    pq.enqueue("TareaMedia", 3)
    print(pq.peek())       # TareaUrgente
    print(pq.dequeue())    # TareaUrgente
    print(pq.dequeue())    # TareaMedia
    print(pq.dequeue())    # Tarea1
