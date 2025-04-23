class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    
    def pop(self) -> int:
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    
    def get_min(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]

# Ejemplo de uso
min_stack = MinStack()
min_stack.push(3)
min_stack.push(1)
min_stack.push(2)
print(min_stack.get_min())  # Output: 1S