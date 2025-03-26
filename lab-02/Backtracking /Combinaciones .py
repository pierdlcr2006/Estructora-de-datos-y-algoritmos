def generar_tf(n, prefix=""):
    if n == 0:
        print(prefix)
        return
    generar_tf(n - 1, prefix + "T")
    generar_tf(n - 1, prefix + "F")

# Ejemplo: Generar combinaciones de T/F de longitud 2
generar_tf(2)
