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


# 1. Logarithmic complexity - O(log n)
def logarithmic_algorithm(n):
    """Algorithm with O(log n) complexity"""
    i = n
    while i > 0:
        # //
        i = i // 2
        print(i)


# 2. Simple Loop - O(n)
def simple_loop(n):
    """Algorithm with O(n) complexity"""
    for _ in range(n):
        pass


# 3. If-then-else statements - O(n)
def if_then_else(n):
    """Algorithm with conditional O(n) complexity"""
    if n % 2 == 0:
        for _ in range(n):
            pass
    else:
        for _ in range(n):
            pass


# 4. Nested Loops - O(n²)
def nested_loops(n):
    """Algorithm with O(n²) complexity"""
    for _ in range(n):
        for _ in range(n):
            pass


# 5. Consecutive statements - O(n + n²) = O(n²)
def consecutive_statements(n):
    """Algorithm with O(n + n²) complexity"""
    for _ in range(n):
        pass

    for _ in range(n):
        for _ in range(n):
            pass


log_condt= [1,10,100,1000,10000,100000]

run_algorithm(if_then_else,log_condt,'Linear Complexity')



