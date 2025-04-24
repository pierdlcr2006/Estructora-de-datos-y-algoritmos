from collections import deque
import time

def traffic_light_simulation():
    # Simulamos el flujo de tráfico en una intersección
    lanes = {
        'Norte': deque(['Car1', 'Car2', 'Car3']),
        'Sur': deque(['Car1', 'Car2']),
        'Este': deque(['Car1', 'Car2', 'Car3', 'Car4']),
        'Oeste': deque(['Car1', 'Car2', 'Car3'])
    }
    
    # Ciclo de semáforo: alternar entre direcciones
    directions = ['Norte', 'Sur', 'Este', 'Oeste']
    
    for direction in directions:
        print(f"\nSemáforo para {direction} en verde:")
        # Simulamos el tráfico
        while lanes[direction]:
            car = lanes[direction].popleft()
            print(f"El vehículo {car} ha pasado.")
            time.sleep(1)  # Simulamos el tiempo de espera para cada vehículo

    print("Simulación de tráfico completada.")

traffic_light_simulation()

