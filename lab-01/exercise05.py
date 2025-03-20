import functions as f

# 5. Consecutive statements - O(n + n²) = O(n²)
def consecutive_statements(n):
    """Algorithm with O(n + n²) complexity"""
    for _ in range(n):
        pass

    for _ in range(n):
        for _ in range(n):
            pass
quadratic_n_values = [100, 400, 600, 800, 1000, 1100]

f.run_algorithm(consecutive_statements, quadratic_n_values, "Consecutive Statements - Mixed Complexity")