<!-- ![](../img/tecsupLogo.png) -->
<p align="center">
<img src="../img/tecsupLogo.png" align="center"> 
</p>

# Algoritmos y Estructuras de Datos

## Lab01: Introducction to algorithm design

## Capacidades

- Identificar las importancia de los algoritmos en programación

## Seguridad

- Generar un ambiente seguro
- Evitar el consumo de alimentos
- Dejar el ambiente ordenado y limpio

## Preparación

- El alumno debe revisar previamente el material cargado

## Recursos

- Computadora

## Instrucciones

Cada integrante del grupo debe seleccionar un ejercicio diferente y desarrollarlo con la siguiente estructura.

- **Nombre del alumno**
- **Ejercicio a desarrollar**
- **Prompt engineering**

    - Prompt ingresado y captura
    - Análisis del prompt
    - Ajustes de prompt y captura
    - Comentarios de los compañeros

- **Código**
    - Código desarrollado
    - Análisis del código
    - Comentarios de los compañeros

Desarrollar todo el código en inglés

## Algoritmos y Estructura de Datos 

Dependency Matplotlib

```python
  pip install matplotlib
```

```python

  import matplotlib.pyplot as plt
  data = {10:0.3, 100:0,5 ,1000:0.8}
  plt.scatter(x=data.keys(), y=data.values() , color="Red")
  plt.tittle('Loops')  
  plt.xlabel('Iteractions')
  plt.ylabel('Time(s)')
  plt.show()

```

## Ejercicios

Se debe realizar los ejercicios planteados y un gráfico del tiempo de procesamiento versus los valores de n.

**Funciones que nos permiten realizar medir el tiempo, visualizar la gráfica y ejecutar el algoritmo:**

```python
def measure_time(func, n):
    """Measures execution time of a function"""
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time


def plot_times(n_values, times, title):
    """Plots execution times"""
    plt.plot(n_values, times, 'o-')
    plt.title(title)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()


def run_algorithm(algorithm_func, n_values, title):
    """Runs algorithm and measures execution time for different n values"""
    times = []

    for n in n_values:
        time_taken = measure_time(algorithm_func, n)
        times.append(time_taken)
        print(f"n = {n}, time = {time_taken:.8f} seconds")

    plot_times(n_values, times, title)

```

1. **Logarithmic complexity - O(log n)**

    Calcular el tiempo de procesamiento para un condicional con un bucle simple, los valores de n serán : 1,10, 100, 1000, 10000 , 100000, 1000000.

```python

    def logarithmic_algorithm(n):
    """Algorithm with O(log n) complexity"""
    i = n
    while i > 0:
        i = i // 2

```

2. **Simple Loop - O(n)**

    Calcular el tiempo de procesamiento para un bucle simple, los valores de n serán: 10^2, 10^3, 10^4, 10^5 y 10^6.

```python

  def simple_loop(n):
    """Algorithm with O(n) complexity"""
    for _ in range(n):
        pass

```

3. **If-then-else statements - O(n)**

    Calcular el tiempo de procesamiento para un condicional con un bucle simple, los valores de n serán: 1, 10, 100, 1000, 10000, 100000.

```python

    def if_then_else(n):
    """Algorithm with conditional O(n) complexity"""
    if n % 2 == 0:
        for _ in range(n):
            pass
    else:
        for _ in range(n):
            pass

```

4. **Nested Loops - O(n²)**

    Calcular el tiempo de procesamiento para un bucle anidado de nivel 2, los valores de n serán: 100, 400, 600, 800, 1000, 1100.

```python

    def nested_loops(n):
    """Algorithm with O(n²) complexity"""
    for _ in range(n):
        for _ in range(n):
            pass

```

5. **Nested Loops - O(n²)**

    Calcular el tiempo de procesamiento para un bucle simple unido a un bucle anidado de nivel 2, los valores de n serán: 100, 400, 600, 800, 1000, 1100.

```python

    def consecutive_statements(n):
    """Algorithm with O(n + n²) complexity"""
    for _ in range(n):
        pass

    for _ in range(n):
        for _ in range(n):
            pass

```

## Identificar Algoritmo

1. Algoritmo 1: n =  1, 10, 100, 1000, 10000

```python

  


  

```

2. Algoritmo 2: n=  1, 10, 100, 1000 

```python

  


  

```

3. Algoritmo 3: n = 1,5,10,50,100,500,1000,5000,10000,50000,100000

```python

  


  

```

**Propuesta de algoritmo**

Proponer un algoritmo que resuelva problema e iterar para que mejore.

```python

  


  

```

## Conclusiones
1. 

