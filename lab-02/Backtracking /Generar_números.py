def generar_numeros(n, prefix=""):
    if n == 0:
        print(prefix)
        return
    for i in "123":
        generar_numeros(n - 1, prefix + i)

# Ejemplo: Generar números de longitud 3 con los dígitos 1, 2 y 3
generar_numeros(3)
