class StringReverser:
    def __init__(self):
        self.stack = []
    
    def reverse_string(self, text: str) -> str:
        # Añadir cada caracter a la pila
        for char in text:
            self.stack.append(char)
        
        # Construir la cadena invertida
        reversed_string = ''
        while self.stack:
            reversed_string += self.stack.pop()
            
        return reversed_string

# Ejemplo de uso
reverser = StringReverser()
print(reverser.reverse_string("Hola Mundo")) 