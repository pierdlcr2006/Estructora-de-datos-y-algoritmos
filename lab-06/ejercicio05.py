class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0
    
    def add(self, data):
        if self.count == self.size:
            # Sobrescribe el dato más antiguo
            self.head = (self.head + 1) % self.size
        else:
            self.count += 1
        
        self.buffer[self.tail] = data
        self.tail = (self.tail + 1) % self.size
    
    def get_latest(self):
        return self.buffer
    
    def stats(self):
        return {
            'size': self.size,
            'elements': self.count
        }

# Ejemplo de uso
cb = CircularBuffer(3)
cb.add(1)
cb.add(2)
cb.add(3)
cb.add(4)  # Sobrescribe el dato 1
print("Elementos en el búfer:", cb.get_latest())
print("Estadísticas del búfer:", cb.stats())
