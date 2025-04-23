
class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.index = 0
        self.size = 0

    def insert(self, data):
        self.buffer[self.index] = data
        self.index = (self.index + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def get_latest(self):
        return self.buffer if self.size == self.capacity else self.buffer[:self.size]

# Example
buffer = CircularBuffer(5)
for i in range(8):
    buffer.insert(i)

print(buffer.get_latest())