def potencia(x, n):
    if n == 0:
        return 1
    return x * potencia(x, n - 1)
print(potencia(2, 3))