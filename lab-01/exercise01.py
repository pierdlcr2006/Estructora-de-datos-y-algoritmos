import time
import matplotlib.pyplot as plt

def measure_time(func, n):
    """Measure the execution time of a function with input n."""
    start_time = time.time()
    func(n)
    return time.time() - start_time

def plot_times(n_values, times, title):
    """Plot execution times against input sizes."""
    plt.figure(figsize=(8, 5))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b', label='Tiempo de ejecución (s)')
    plt.xscale('log')  # Set logarithmic scale for better visualization
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.title(title)
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()

def run_algorithm(algorithm_func, n_values, title):
    """Run algorithm and measure execution time for different n values."""
    times = [measure_time(algorithm_func, n) for n in n_values]

    # Print results in a formatted way
    for n, t in zip(n_values, times):
        print(f"n = {n:7}, tiempo = {t:.8e} segundos")

    plot_times(n_values, times, title)

def logarithmic_algorithm(n):
    """Algorithm with O(log n) complexity (binary reduction)."""
    while n > 0:
        n //= 2  # Integer division by 2 to simulate logarithmic complexity

# Define input sizes
n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]

# Run and visualize the algorithm
run_algorithm(logarithmic_algorithm, n_values, "Complejidad Logarítmica - O(log n)")