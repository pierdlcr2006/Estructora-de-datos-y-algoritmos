# Algoritmos y Estructuras de Datos  
## Lab02: Recursion and Backtracking  

### Capacidades  
- Conocer, comprender y aplicar los algoritmos de recursión y backtracking en la resolución de problemas de software.

### Seguridad  
- Generar un ambiente seguro.
- Evitar el consumo de alimentos.
- Dejar el ambiente ordenado y limpio.

### Preparación  
- El alumno debe revisar previamente el material cargado.

### Recursos  
- Computadora.

---

## Instrucciones  
Cada integrante del grupo debe seleccionar un ejercicio diferente y desarrollarlo con la siguiente estructura:

- **Nombre del alumno**
- **Ejercicio a desarrollar**
- **Prompt engineering**
  - Prompt ingresado y/o captura
  - Análisis del prompt
  - Ajustes del prompt y/o captura
  - Comentarios de los compañeros
- **Código**
  - Código desarrollado
  - Análisis del código
  - Captura de la ejecución del código
  - Comentarios de los compañeros

> *Desarrollar todo el código en inglés.*

---

## Ejercicios  
Para todo ejercicio realizar lo siguiente:
- Explicar cómo funciona el algoritmo
- Hacer su diagrama de cómo se ejecuta.
- Comentarios del problema
- Hacer 3 casos de prueba

### Recursividad

# 1. Factorial usando Recursividad

## 📌 Ejercicio a desarrollar
Calcular el factorial de un número utilizando una función recursiva en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función recursiva en Python para calcular el factorial de un número."

### **Análisis del prompt:**
El prompt es claro, pero no especifica si el número debe ser positivo, si se debe manejar el caso de cero o si se esperan validaciones para entradas no válidas.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que calcule el factorial de un número entero positivo. Si el número es menor a 0, debe retornar un mensaje de error."

### **Comentarios de los compañeros:**
- *Toledo:* "El ajuste es útil, porque evita errores con números negativos."
- *De la Cruz:* "Sería bueno especificar qué hacer con valores no enteros."

---

## 💻 Código desarrollado
```python
def factorial(n):
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

---

## 📊 Análisis del código
- La función verifica si `n` es negativo y devuelve un mensaje de error en ese caso.
- Si `n` es `0` o `1`, devuelve `1` (caso base).
- Para otros valores, usa recursión multiplicando `n` por el factorial de `n-1`.
- La complejidad del algoritmo es **O(n)** debido a la cantidad de llamadas recursivas.

---

## 🖥️ Captura de la ejecución del código
```python
print(factorial(5))  # 120
print(factorial(0))  # 1
print(factorial(-3)) # Error: No se puede calcular el factorial de un número negativo.
```

**Salida esperada:**
```
120
1
Error: No se puede calcular el factorial de un número negativo.
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "El código es eficiente y claro. Tal vez podríamos agregar un chequeo para valores decimales."
- *De la Cruz:* "Me gusta que se manejen los errores adecuadamente."



# 2. Potencia usando Recursividad

## 📌 Ejercicio a desarrollar
Calcular la potencia de un número usando una función recursiva en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función recursiva en Python para calcular la potencia de un número x elevado a n."

### **Análisis del prompt:**
El prompt es claro, pero no menciona si `x` puede ser un número decimal o si `n` puede ser negativo.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que calcule la potencia de un número entero `x` elevado a un exponente `n` positivo."

### **Comentarios de los compañeros:**
- *Toledo:* "Podríamos agregar soporte para exponentes negativos."
- *De la Cruz:* "Es importante definir si `x` puede ser un decimal."

---

## 💻 Código desarrollado
```python
def potencia(x, n):
    if n == 0:
        return 1
    return x * potencia(x, n - 1)
```

---

## 📊 Análisis del código
- La función implementa la recursión multiplicando `x` por la potencia de `x` elevado a `n-1`.
- El caso base es cuando `n` es `0`, devolviendo `1`.
- No maneja exponentes negativos ni valores decimales, lo que podría ser una mejora futura.
- La complejidad del algoritmo es **O(n)** debido a la cantidad de llamadas recursivas.

---

## 🖥️ Captura de la ejecución del código
```python
print(potencia(2, 3))  # 8
print(potencia(5, 0))  # 1
print(potencia(3, 4))  # 81
```

**Salida esperada:**
```
8
1
81
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "Falta considerar exponentes negativos."
- *De la Cruz:* "Tal vez podríamos usar un caso base más eficiente o implementar optimización con exponentes pares."

# 3. Suma de dígitos usando Recursividad

## 📌 Ejercicio a desarrollar
Calcular la suma de los dígitos de un número utilizando una función recursiva en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función recursiva en Python para calcular la suma de los dígitos de un número."

### **Análisis del prompt:**
El prompt es claro, pero no especifica si el número puede ser negativo o si debe manejarse con valores no enteros.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que calcule la suma de los dígitos de un número entero positivo. Si el número es negativo, debe convertirlo a positivo."

### **Comentarios de los compañeros:**
- *Toledo:* "Mejor especificar qué hacer con números negativos."
- *De la Cruz:* "Sería bueno indicar qué ocurre si el número contiene decimales."

---

## 💻 Código desarrollado
```python
def suma_digitos(n):
    n = abs(n)  # Convertir a positivo si es negativo
    if n == 0:
        return 0
    return n % 10 + suma_digitos(n // 10)
```

---

## 📊 Análisis del código
- La función convierte el número a positivo si es negativo.
- Extrae el último dígito con `n % 10` y lo suma recursivamente con los dígitos restantes.
- El caso base ocurre cuando `n` es `0`, retornando `0`.
- La complejidad del algoritmo es **O(log n)** debido a la reducción del número en cada llamada recursiva.

---

## 🖥️ Captura de la ejecución del código
```python
print(suma_digitos(123))  # 6
print(suma_digitos(-456)) # 15
print(suma_digitos(0))    # 0
```

**Salida esperada:**
```
6
15
0
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "Buen manejo de números negativos, pero sería interesante ver qué ocurre con decimales."
- *De la Cruz:* "Tal vez podríamos agregar validación para evitar entradas no numéricas."



# Verificar si una cadena es palíndromo usando Recursividad

## 📌 Ejercicio a desarrollar
Determinar si una cadena es un palíndromo utilizando una función recursiva en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función recursiva en Python para verificar si una cadena es un palíndromo."

### **Análisis del prompt:**
El prompt es claro, pero no menciona si la comparación debe ser sensible a mayúsculas/minúsculas o si se deben ignorar espacios y caracteres especiales.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que verifique si una cadena es un palíndromo. La función debe ignorar mayúsculas y espacios."

### **Comentarios de los compañeros:**
- *Toledo:* "Es una buena idea ignorar espacios y mayúsculas para hacer la comparación más flexible."
- *De la Cruz:* "También podríamos eliminar caracteres especiales para comparar solo letras."

---

## 💻 Código desarrollado
```python
import re

def es_palindromo(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  # Limpiar cadena
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return es_palindromo(s[1:-1])
```

---

## 📊 Análisis del código
- Se eliminan espacios y caracteres no alfanuméricos utilizando `re.sub`.
- Se convierte la cadena a minúsculas para hacer una comparación uniforme.
- Se compara el primer y último carácter de la cadena y se llama recursivamente con el resto de la cadena.
- La condición base es cuando la longitud de la cadena es 1 o 0, devolviendo `True`.
- La complejidad del algoritmo es **O(n)**.

---

## 🖥️ Captura de la ejecución del código
```python
print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("Python"))             # False
print(es_palindromo("A Santa at NASA"))     # True
```

**Salida esperada:**
```
True
False
True
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "La limpieza de la cadena es clave para mejorar la precisión."
- *De la Cruz:* "Me gusta que se usen expresiones regulares para filtrar caracteres no deseados."


# Invertir una cadena usando Recursividad

## 📌 Ejercicio a desarrollar
Invertir una cadena utilizando una función recursiva en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función recursiva en Python para invertir una cadena."

### **Análisis del prompt:**
El prompt es claro, pero no especifica si debe conservar los espacios y mayúsculas o si la entrada puede contener caracteres especiales.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que invierta una cadena sin modificar espacios ni caracteres especiales."

### **Comentarios de los compañeros:**
- *Toledo:* "Podría ser útil manejar casos donde la cadena tenga solo un carácter."
- *De la Cruz:* "También podríamos agregar una versión que elimine espacios antes de invertir."

---

## 💻 Código desarrollado
```python
def invertir_cadena(s):
    if len(s) == 0:
        return ""
    return s[-1] + invertir_cadena(s[:-1])
```

---

## 📊 Análisis del código
- La función usa recursión para tomar el último carácter de la cadena y concatenarlo con la versión invertida del resto de la cadena.
- El caso base ocurre cuando la cadena es vacía, devolviendo `""`.
- La complejidad del algoritmo es **O(n)**, ya que la función se llama `n` veces.

---

## 🖥️ Captura de la ejecución del código
```python
print(invertir_cadena("hola"))  # "aloh"
print(invertir_cadena("Python")) # "nohtyP"
print(invertir_cadena(""))      # ""
```

**Salida esperada:**
```
aloh
nohtyP

```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "El código es simple y efectivo, pero podríamos probarlo con caracteres especiales."
- *De la Cruz:* "Sería interesante ver una versión que invierta palabras en lugar de caracteres."


# Suma de elementos en una lista usando Recursividad

## 📌 Ejercicio a desarrollar
Calcular la suma de los elementos en una lista utilizando una función recursiva en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función recursiva en Python para calcular la suma de los elementos de una lista."

### **Análisis del prompt:**
El prompt es claro, pero no menciona si la lista puede contener valores negativos o si debe manejar listas vacías.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que calcule la suma de los elementos de una lista de números enteros. Si la lista está vacía, debe retornar `0`."

### **Comentarios de los compañeros:**
- *Toledo:* "Es bueno definir qué ocurre con listas vacías."
- *De la Cruz:* "Podríamos agregar soporte para listas con valores flotantes."

---

## 💻 Código desarrollado
```python
def suma_lista(lst):
    if not lst:
        return 0
    return lst[0] + suma_lista(lst[1:])
```

---

## 📊 Análisis del código
- La función revisa si la lista está vacía y retorna `0` en ese caso.
- Si la lista no está vacía, toma el primer elemento y lo suma con la recursión del resto de la lista.
- La complejidad del algoritmo es **O(n)**, ya que la función recursiva se llama `n` veces.

---

## 🖥️ Captura de la ejecución del código
```python
print(suma_lista([1, 2, 3, 4, 5]))  # 15
print(suma_lista([-1, 10, -3]))     # 6
print(suma_lista([]))               # 0
```

**Salida esperada:**
```
15
6
0
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "El código es eficiente, pero podríamos agregar un chequeo para validar que todos los elementos sean numéricos."
- *De la Cruz:* "Sería interesante permitir listas con números flotantes."


# Fibonacci usando Recursividad

## 📌 Ejercicio a desarrollar
Calcular el término n de la secuencia de Fibonacci utilizando una función recursiva en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función recursiva en Python para calcular el término n de la secuencia de Fibonacci."

### **Análisis del prompt:**
El prompt es claro, pero no menciona cómo manejar valores negativos ni optimizaciones para evitar recomputaciones innecesarias.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que calcule el término `n` de la secuencia de Fibonacci. Si `n` es menor a 0, debe retornar un mensaje de error."

### **Comentarios de los compañeros:**
- *Toledo:* "Sería útil agregar una versión optimizada con memoización."
- *De la Cruz:* "Podríamos considerar valores negativos y evitar recomputaciones."

---

## 💻 Código desarrollado
```python
def fibonacci(n):
    if n < 0:
        return "Error: No se puede calcular Fibonacci de un número negativo."
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## 📊 Análisis del código
- La función maneja valores negativos con un mensaje de error.
- Utiliza la fórmula `F(n) = F(n-1) + F(n-2)` con casos base `F(0) = 0` y `F(1) = 1`.
- La complejidad del algoritmo es **O(2ⁿ)**, lo que lo hace ineficiente para valores grandes.

---

## 🖥️ Captura de la ejecución del código
```python
print(fibonacci(5))   # 5
print(fibonacci(10))  # 55
print(fibonacci(-3))  # Error: No se puede calcular Fibonacci de un número negativo.
```

**Salida esperada:**
```
5
55
Error: No se puede calcular Fibonacci de un número negativo.
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "El código es correcto, pero la versión recursiva sin optimización es lenta para valores grandes."
- *De la Cruz:* "Podríamos implementar memoización para mejorar el rendimiento."


# Torre de Hanoi usando Recursividad

## 📌 Ejercicio a desarrollar
Resolver el problema de la Torre de Hanoi utilizando una función recursiva en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función recursiva en Python para resolver el problema de la Torre de Hanoi."

### **Análisis del prompt:**
El prompt es claro, pero no especifica cuántos discos se deben mover ni si la salida debe imprimirse paso a paso.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que resuelva la Torre de Hanoi para `n` discos y muestre los movimientos paso a paso."

### **Comentarios de los compañeros:**
- *Toledo:* "Es importante que el código muestre el proceso paso a paso para entender mejor la solución."
- *De la Cruz:* "Podríamos agregar una versión que retorne la secuencia en lugar de solo imprimirla."

---

## 💻 Código desarrollado
```python
def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco de {origen} a {destino}")
        return
    hanoi(n - 1, origen, destino, auxiliar)
    print(f"Mover disco de {origen} a {destino}")
    hanoi(n - 1, auxiliar, origen, destino)
```

---

## 📊 Análisis del código
- La función mueve `n-1` discos al poste auxiliar, luego mueve el disco más grande al destino y finalmente mueve los `n-1` discos del auxiliar al destino.
- El caso base ocurre cuando hay un solo disco (`n == 1`).
- La complejidad del algoritmo es **O(2ⁿ - 1)**, lo que lo hace ineficiente para valores grandes de `n`.

---

## 🖥️ Captura de la ejecución del código
```python
hanoi(3, "A", "B", "C")
```

**Salida esperada:**
```
Mover disco de A a C
Mover disco de A a B
Mover disco de C a B
Mover disco de A a C
Mover disco de B a A
Mover disco de B a C
Mover disco de A a C
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "El código es claro y fácil de entender. Tal vez podríamos agregar una versión que almacene los pasos en una lista."
- *De la Cruz:* "Sería útil visualizar los movimientos en una interfaz gráfica."

### Backtracking (Seleccionar 1)
# Generar strings de dígitos binarios de longitud N usando Backtracking

## 📌 Ejercicio a desarrollar
Generar todas las combinaciones de cadenas de dígitos binarios de longitud `N` utilizando Backtracking en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función en Python que genere todas las combinaciones de cadenas binarias de longitud `N` utilizando recursión."

### **Análisis del prompt:**
El prompt es claro, pero no menciona si las combinaciones deben imprimirse directamente o almacenarse en una lista.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que genere todas las combinaciones de cadenas binarias de longitud `N`. La función debe imprimir cada combinación generada."

### **Comentarios de los compañeros:**
- *Toledo:* "El ajuste deja claro que la función debe imprimir los resultados."
- *De la Cruz:* "También podríamos agregar una opción para retornar las combinaciones en una lista."

---

## 💻 Código desarrollado
```python
def generar_binarios(n, prefix=""):
    if n == 0:
        print(prefix)
        return
    generar_binarios(n - 1, prefix + "0")
    generar_binarios(n - 1, prefix + "1")
```

---

## 📊 Análisis del código
- La función usa Backtracking para generar todas las combinaciones posibles de `N` bits.
- Si `n == 0`, imprime el string generado.
- Llama recursivamente a sí misma agregando `0` y `1` en cada nivel de recursión.
- La complejidad del algoritmo es **O(2ⁿ)**, ya que genera todas las combinaciones posibles.

---

## 🖥️ Captura de la ejecución del código
```python
generar_binarios(3)
```

**Salida esperada:**
```
000
001
010
011
100
101
110
111
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "Código limpio y eficiente. Se podría optimizar para retornar los valores en una lista si es necesario."
- *De la Cruz:* "El código funciona bien, pero podríamos documentarlo un poco más."



# Combinaciones de strings de T/F de longitud N usando Backtracking

## 📌 Ejercicio a desarrollar
Generar todas las combinaciones de cadenas que contienen los caracteres `T` y `F` de longitud `N` utilizando Backtracking en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función en Python que genere todas las combinaciones de strings de `T` y `F` de longitud `N` usando recursión."

### **Análisis del prompt:**
El prompt es claro, pero no menciona si las combinaciones deben imprimirse o almacenarse en una lista.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que genere todas las combinaciones de cadenas con `T` y `F` de longitud `N`. La función debe imprimir cada combinación generada."

### **Comentarios de los compañeros:**
- *Toledo:* "El ajuste deja claro que la función debe imprimir los resultados."
- *De la Cruz:* "Podríamos agregar una opción para retornar las combinaciones en una lista."

---

## 💻 Código desarrollado
```python
def generar_tf(n, prefix=""):
    if n == 0:
        print(prefix)
        return
    generar_tf(n - 1, prefix + "T")
    generar_tf(n - 1, prefix + "F")
```

---

## 📊 Análisis del código
- La función usa Backtracking para generar todas las combinaciones posibles de `N` caracteres `T` y `F`.
- Si `n == 0`, imprime el string generado.
- Llama recursivamente a sí misma agregando `T` y `F` en cada nivel de recursión.
- La complejidad del algoritmo es **O(2ⁿ)**, ya que genera todas las combinaciones posibles.

---

## 🖥️ Captura de la ejecución del código
```python
generar_tf(2)
```

**Salida esperada:**
```
TT
TF
FT
FF
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "El código es claro y eficiente. Se podría optimizar para retornar los valores en una lista."
- *De la Cruz:* "El código funciona bien, pero podríamos documentarlo un poco más y agregar un parámetro opcional para almacenar los resultados."

# Generar números con los valores 1, 2 y 3 de N dígitos usando Backtracking

## 📌 Ejercicio a desarrollar
Generar todas las combinaciones posibles de números formados por los dígitos `1`, `2` y `3` de longitud `N` utilizando Backtracking en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función en Python que genere todos los números posibles con los dígitos `1`, `2` y `3` de longitud `N` usando recursión."

### **Análisis del prompt:**
El prompt es claro, pero no menciona si los números deben imprimirse o almacenarse en una lista.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que genere todas las combinaciones de números de longitud `N` usando solo los dígitos `1`, `2` y `3`. La función debe imprimir cada combinación generada."

### **Comentarios de los compañeros:**
- *Toledo:* "El ajuste permite que el código genere combinaciones de manera clara."
- *De la Cruz:* "Sería útil agregar una opción para almacenar las combinaciones en una lista."

---

## 💻 Código desarrollado
```python
def generar_numeros(n, prefix=""):
    if n == 0:
        print(prefix)
        return
    for i in "123":
        generar_numeros(n - 1, prefix + i)
```

---

## 📊 Análisis del código
- La función usa Backtracking para generar todas las combinaciones posibles de `N` dígitos con valores `1`, `2` y `3`.
- Si `n == 0`, imprime el número generado.
- Se usa un bucle `for` para recorrer los posibles valores (`1`, `2`, `3`) y se llama recursivamente a la función con un nuevo prefijo.
- La complejidad del algoritmo es **O(3ⁿ)**, ya que genera todas las combinaciones posibles de `N` dígitos con 3 opciones por posición.

---

## 🖥️ Captura de la ejecución del código
```python
generar_numeros(2)
```

**Salida esperada:**
```
11
12
13
21
22
23
31
32
33
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "El código es eficiente y fácil de entender. Tal vez podríamos optimizarlo almacenando los resultados en una lista."
- *De la Cruz:* "Sería interesante agregar una validación para evitar números repetidos en ciertas combinaciones si se requiere."

# Suma de subconjuntos dando el valor de N usando Backtracking

## 📌 Ejercicio a desarrollar
Encontrar todas las combinaciones de subconjuntos de una lista dada cuya suma sea igual a un valor `N`, utilizando Backtracking en Python.

## 🎯 Prompt engineering

### **Prompt ingresado:**
"Escribe una función en Python que encuentre todos los subconjuntos de una lista que sumen un valor `N` usando recursión."

### **Análisis del prompt:**
El prompt es claro, pero no menciona si los elementos pueden repetirse o si deben considerarse en orden específico.

### **Ajustes del prompt:**
"Escribe una función recursiva en Python que encuentre todos los subconjuntos de una lista de enteros cuya suma sea exactamente `N`. La función debe imprimir cada subconjunto encontrado."

### **Comentarios de los compañeros:**
- *Toledo:* "El ajuste deja claro que la función debe encontrar subconjuntos exactos."
- *De la Cruz:* "Podríamos agregar una opción para devolver los resultados en una lista en lugar de solo imprimirlos."

---

## 💻 Código desarrollado
```python
def suma_subconjuntos(nums, target, subset=[], index=0):
    if sum(subset) == target:
        print(subset)
        return
    if index >= len(nums) or sum(subset) > target:
        return
    # Incluir el número actual
    suma_subconjuntos(nums, target, subset + [nums[index]], index + 1)
    # No incluir el número actual
    suma_subconjuntos(nums, target, subset, index + 1)
```

---

## 📊 Análisis del código
- La función utiliza Backtracking para explorar todas las combinaciones posibles de elementos.
- Si la suma del subconjunto actual es igual al objetivo `target`, se imprime el subconjunto.
- Si la suma excede `target` o si se han procesado todos los elementos, se retorna.
- La función prueba dos caminos: incluir o no incluir el elemento actual.
- La complejidad del algoritmo es **O(2ⁿ)**, ya que se prueban todas las combinaciones posibles.

---

## 🖥️ Captura de la ejecución del código
```python
suma_subconjuntos([1, 2, 3, 4, 5], 5)
```

**Salida esperada:**
```
[1, 4]
[2, 3]
[5]
```

---

## 💬 Comentarios de los compañeros
- *Toledo:* "El código es eficiente, pero podríamos optimizarlo usando poda para evitar exploraciones innecesarias."
- *De la Cruz:* "Sería interesante devolver los subconjuntos en una lista para un uso más flexible."


---

### Proponer un algoritmo que emplee backtracking o recursividad:
- Explicar cómo funciona el algoritmo.
- Hacer su diagrama de flujo.
- Comentarios del problema.

---

## Reto  
Proponer un algoritmo que resuelva un problema del 1 al 8 de la siguiente web: [adventjs.dev](https://adventjs.dev/) e iterar hasta tener 5 estrellas.

---

## Desarrollo  

---

## Incrementos  
- Repositorio
- Código fuente
- Informe

---

## Conclusiones  
1.
