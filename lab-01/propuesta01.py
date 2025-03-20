def sum_natural_numbers(n):
    """Suma los primeros n números naturales."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Ejemplo de uso
n = 100
print(f"La suma de los primeros {n} números naturales es: {sum_natural_numbers(n)}")