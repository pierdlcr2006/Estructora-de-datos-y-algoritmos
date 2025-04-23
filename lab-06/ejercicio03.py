import random
import time

def simulate_traffic():
    traffic_lights = ['Red', 'Green']
    current_light = 'Red'
    vehicles = 0

    # Simulating 10 cycles of traffic light changes
    for cycle in range(10):
        print(f"Cycle {cycle + 1}: Light is {current_light}")
        if current_light == 'Red':
            vehicles += random.randint(1, 10)  # Vehicles arrive during red light
        else:
            vehicles -= min(vehicles, random.randint(1, 10))  # Vehicles pass during green light

        print(f"Vehicles in queue: {max(vehicles, 0)}")
        current_light = 'Green' if current_light == 'Red' else 'Red'  # Switch light
        time.sleep(1)


simulate_traffic()