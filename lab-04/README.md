# Laboratorio 4: Pilas (Stacks)

<p align="center">
  <img src="../img/tecsupLogo.png" alt="Tecsup Logo">
</p>

## 🎯 Objetivos

- Definir las reglas básicas para la implementación de pilas
- Elaborar y diseñar pilas con listas estáticas, dinámicas y enlazadas
- Implementar aplicaciones prácticas usando pilas

## 📋 Requisitos

### Preparación
- Revisar el material proporcionado previamente
- Tener instalado Python 3.x

### Recursos
- Computadora con entorno de desarrollo
- Editor de código (recomendado: VS Code)
- Git para control de versiones

## 🔬 Estructura del Laboratorio

### 1. Conceptos Fundamentales de Pilas

Una pila (stack) es una estructura de datos que sigue el principio LIFO (Last In, First Out). Las operaciones básicas son:

- `push`: Añade un elemento al tope
- `pop`: Remueve y retorna el elemento del tope
- `peek`: Retorna el elemento del tope sin removerlo
- `isEmpty`: Verifica si la pila está vacía
- `size`: Retorna el número de elementos

### 2. Implementaciones

#### 2.1 Array Fijo
```python
class ArrayStack:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.top = -1
```

#### 2.2 Array Dinámico 
```python
class DynamicArrayStack:
    def __init__(self):
        self.data = []
```

#### 2.3 Lista Enlazada
```python
class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0
```

## 📝 Ejercicios

1. **Inversión de Cadenas**
   - Usar una pila para invertir una cadena
   - Implementar casos de prueba

2. **Evaluación de Expresiones**
   - Implementar evaluador de expresiones infijas
   - Convertir expresiones infijas a postfijas

3. **Pila con Función getMin()**
   - Implementar una pila que mantenga el mínimo
   - Todas las operaciones deben ser O(1)

4. **Historial de Navegador**
   - Implementar funcionalidad de "atrás/adelante"
   - Manejar historial de navegación

5. **Validador de HTML**
   - Verificar balance de etiquetas HTML
   - Detectar etiquetas mal anidadas

### 3. Soluciones de Ejercicios

#### 3.1 Inversión de Cadenas
```python
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
print(reverser.reverse_string("Hola Mundo"))  # Output: odnuM aloH
```

#### 3.2 Evaluador de Expresiones
```python
class ExpressionEvaluator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    def infix_to_postfix(self, expression: str) -> str:
        stack = []
        postfix = []
        
        for token in expression.split():
            if token.isalnum():  # Operando
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Descartar el '('
            else:  # Operador
                while (stack and stack[-1] != '(' and 
                       self.operators[stack[-1]] >= self.operators[token]):
                    postfix.append(stack.pop())
                stack.append(token)
        
        while stack:
            postfix.append(stack.pop())
            
        return ' '.join(postfix)

# Ejemplo de uso
evaluator = ExpressionEvaluator()
print(evaluator.infix_to_postfix("3 + 4 * 2"))  # Output: 3 4 2 * +
```

#### 3.3 Pila con getMin()
```python
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
print(min_stack.get_min())  # Output: 1
```

#### 3.4 Historial de Navegador
```python
class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = None
    
    def visit(self, url: str) -> None:
        if self.current:
            self.back_stack.append(self.current)
        self.current = url
        self.forward_stack = []  # Limpiar historial hacia adelante
    
    def back(self) -> str:
        if not self.back_stack:
            return self.current
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        return self.current
    
    def forward(self) -> str:
        if not self.forward_stack:
            return self.current
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        return self.current

# Ejemplo de uso
browser = BrowserHistory()
browser.visit("google.com")
browser.visit("youtube.com")
print(browser.back())  # Output: google.com
```

#### 3.5 Validador HTML
```python
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
```

## 🚀 Reto

Resolver un problema de [adventjs.dev](https://adventjs.dev/) (del 1 al 8) e iterar hasta obtener 5 estrellas.

## 📊 Evaluación

| Criterio | Puntaje |
|----------|----------|
| Repositorio | 0-5 |
| Código fuente | 0-5 |
| Informe | -10-0 |
| Exposición | 0-10 |

## 📦 Entregables

1. Código fuente comentado
2. Informe técnico con:
   - Explicación de implementaciones
   - Análisis de complejidad
   - Casos de prueba
3. Presentación de resultados

## 🏆 Conclusiones

[Espacio para que los estudiantes agreguen sus conclusiones]

## 📚 Referencias

- Estructuras de Datos en Python
- [Documentación de Python](https://docs.python.org/)
- [adventjs.dev](https://adventjs.dev/)