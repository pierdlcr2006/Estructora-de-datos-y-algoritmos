import matplotlib.pyplot as plt
import time

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



# 5. Consecutive statements - O(n + n²) = O(n²)
def consecutive_statements(n):
    """Algorithm with O(n + n²) complexity"""
    for _ in range(n):
        pass

    for _ in range(n):
        for _ in range(n):
            pass
quadratic_n_values = [100, 400, 600, 800, 1000, 1100]

run_algorithm(consecutive_statements, quadratic_n_values, "Consecutive Statements - Mixed Complexity")