def sum_natural_numbers_optimized(n):
    """Suma los primeros n números naturales utilizando una fórmula matemática."""
    return n * (n + 1) // 2

# Ejemplo de uso
n = 100
print(f"La suma de los primeros {n} números naturales es: {sum_natural_numbers_optimized(n)}")