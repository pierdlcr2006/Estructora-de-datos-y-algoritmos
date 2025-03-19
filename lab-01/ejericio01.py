import time
import matplotlib.pyplot as plt 
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

def logarithmic_algorithm(n):
    """Algorithm with O(log n) complexity"""
    i = n
    while i > 0:
        i = i // 2
        pass
log_n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
run_algorithm(logarithmic_algorithm, log_n_values, "Logarithmic Complexity")
import matplotlib.pyplot as plt

# Extraer valores de n y tiempos
n_values, times = zip(*execution_times)

# Crear la gráfica
plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', color='b', label='Tiempo de ejecución (s)')

# Configurar escala logarítmica en el eje x
plt.xscale('log')

# Etiquetas y título
plt.xlabel('n (tamaño de entrada)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Complejidad Logarítmica - O(log n)')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Mostrar la gráfica
plt.show()
