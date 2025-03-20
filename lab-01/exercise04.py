import functions as f
def nested_loops(n):
    """Algorithm with O(n²) complexity"""
    for _ in range(n):
        for _ in range(n):
            pass

quadratic_n_values = [100, 400, 600, 800, 1000, 1100]
f.run_algorithm(nested_loops, quadratic_n_values, "Nested Loops - Quadratic Complexity")