class CircularDeque:
    """Cola doble circular con capacidad fija."""

    def __init__(self, k):
        self.capacity = k
        self.data = [None] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.data[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.count -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.data[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity


# 🧪 Prueba
if __name__ == "__main__":
    deque = CircularDeque(3)
    print(deque.insertLast(1))   # True
    print(deque.insertLast(2))   # True
    print(deque.insertFront(3))  # True
    print(deque.insertFront(4))  # False (llena)
    print(deque.getRear())       # 2
    print(deque.isFull())        # True
    print(deque.deleteLast())    # True
    print(deque.insertFront(4))  # True
    print(deque.getFront())      # 4
