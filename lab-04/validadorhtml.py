class HTMLValidator:
    def __init__(self):
        self.stack = []
    
    def is_valid(self, html: str) -> bool:
        tag = ""
        is_opening = False
        
        for char in html:
            if char == '<':
                is_opening = True
                tag = ""
            elif char == '>':
                is_opening = False
                if tag.startswith('/'):
                    if not self.stack or self.stack.pop() != tag[1:]:
                        return False
                else:
                    self.stack.append(tag)
                tag = ""
            elif is_opening:
                tag += char
                
        return len(self.stack) == 0

# Ejemplo de uso
validator = HTMLValidator()
print(validator.is_valid("<html><body></body></html>"))  # Output: True
print(validator.is_valid("<html><body></html></body>"))  # Output: False