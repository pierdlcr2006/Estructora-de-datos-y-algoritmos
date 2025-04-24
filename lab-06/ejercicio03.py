from collections import deque
import random
import time

def traffic_light_simulation():
    # Simulamos el flujo de tráfico en una intersección
    lanes = {
        'North': deque(),
        'South': deque(),
        'East': deque(),
        'West': deque()
    }
    
    # Agregar vehículos aleatorios a cada carril
    for lane in lanes:
        lanes[lane].extend([f"Car{i}" for i in range(random.randint(1, 5))])
    
    # Ciclo de semáforo: alternar entre direcciones
    directions = ['North', 'South', 'East', 'West']
    
    for direction in directions:
        print(f"\nSemáforo para {direction} en verde:")
        # Simulamos el tráfico
        while lanes[direction]:
            car = lanes[direction].popleft()
            print(f"El vehículo {car} ha pasado.")
            time.sleep(1)  # Simulamos el tiempo de espera para cada vehículo

    print("Simulación de tráfico completada.")

traffic_light_simulation()
