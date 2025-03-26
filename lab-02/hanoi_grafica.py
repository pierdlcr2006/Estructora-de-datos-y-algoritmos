import time
import matplotlib.pyplot as plt

# Función recursiva para resolver las Torres de Hanoi
def towers_of_hanoi(n, from_tower=1, to_tower=3, tmp_tower=2):
    if n == 1:
        return
    towers_of_hanoi(n - 1, from_tower, tmp_tower, to_tower)
    towers_of_hanoi(n - 1, tmp_tower, to_tower, from_tower)

# Lista de discos a evaluarS
disks = list(range(1, 15))
times = []

# Medir el tiempo de ejecución para cada cantidad de discos
for n in disks:
    start_time = time.time()
    towers_of_hanoi(n)
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)

# Graficar los resultados
plt.figure(figsize=(8, 5))
plt.plot(disks, times, marker='o', linestyle='-', color='b', label="Tiempo de ejecución")
plt.xlabel("Número de discos")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de ejecución del algoritmo de Torres de Hanoi")
plt.legend()
plt.grid(True)
plt.show()
