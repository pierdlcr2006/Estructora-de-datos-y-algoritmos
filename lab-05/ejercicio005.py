import random
import time

class Customer:
    def __init__(self, customer_id, item_count):
        self.customer_id = customer_id
        self.item_count = item_count
        self.arrival_time = time.time()
        self.wait_time = 0

    def process(self, processing_rate):
        # Time to process this customer is proportional to the number of items
        process_time = self.item_count / processing_rate
        print(f"  Procesando cliente #{self.customer_id} con {self.item_count} items (tiempo: {process_time:.2f}s)")
        time.sleep(process_time)  # Simulate processing time
        self.wait_time = time.time() - self.arrival_time
        print(f"  Cliente #{self.customer_id} procesado. Tiempo de espera: {self.wait_time:.2f}s")

class CheckoutLane:
    def __init__(self, lane_id, processing_rate):
        self.lane_id = lane_id
        self.processing_rate = processing_rate
        self.queue = []

    def add_customer(self, customer):
        self.queue.append(customer)
        print(f"  Añadido cliente #{customer.customer_id} con {customer.item_count} items a la caja #{self.lane_id}")

    def process_customer(self):
        if self.queue:
            customer = self.queue.pop(0)
            print(f"Caja #{self.lane_id} atendiendo al cliente #{customer.customer_id}")
            customer.process(self.processing_rate)
            return customer
        return None

    def get_waiting_time(self):
        return sum(customer.wait_time for customer in self.queue) / len(self.queue) if self.queue else 0

class Supermarket:
    def __init__(self, num_lanes, processing_rate):
        self.lanes = [CheckoutLane(i, processing_rate) for i in range(num_lanes)]
        self.customers_processed = 0
        self.total_wait_time = 0
        print(f"Supermercado creado con {num_lanes} cajas y velocidad de procesamiento {processing_rate}")

    def get_shortest_lane(self):
        # Choose the lane with the fewest customers
        shortest = min(self.lanes, key=lambda lane: len(lane.queue))
        print(f"Caja más corta: #{shortest.lane_id} con {len(shortest.queue)} clientes en espera")
        return shortest

    def simulate_customer_arrival(self, customer):
        # Add the customer to the shortest checkout lane
        print(f"\nCliente #{customer.customer_id} llega con {customer.item_count} items")
        shortest_lane = self.get_shortest_lane()
        shortest_lane.add_customer(customer)

    def process_customers(self):
        # Simulate processing customers in each lane
        print("\n--- Procesando clientes en todas las cajas ---")
        for lane in self.lanes:
            print(f"Caja #{lane.lane_id} tiene {len(lane.queue)} clientes en espera")
            customer = lane.process_customer()
            if customer:
                self.customers_processed += 1
                self.total_wait_time += customer.wait_time
                print(f"Cliente #{customer.customer_id} completado - Tiempo de espera: {customer.wait_time:.2f}s")
            else:
                print(f"Caja #{lane.lane_id} está vacía")

    def average_wait_time(self):
        avg = self.total_wait_time / self.customers_processed if self.customers_processed else 0
        print(f"\nTiempo promedio de espera: {avg:.2f}s")
        return avg

    def throughput(self):
        elapsed_time = time.time() - self.start_time
        throughput_rate = self.customers_processed / elapsed_time
        print(f"Tasa de procesamiento: {throughput_rate:.2f} clientes/segundo (Total: {self.customers_processed} clientes en {elapsed_time:.2f}s)")
        return throughput_rate

# Example simulation
print("=== SIMULACIÓN DE SUPERMERCADO ===")
supermarket = Supermarket(num_lanes=3, processing_rate=1)

# Simulate 10 customers arriving
print("\n--- Llegada de clientes ---")
for customer_id in range(10):
    items = random.randint(1, 20)  # Random number of items per customer
    customer = Customer(customer_id, items)
    supermarket.simulate_customer_arrival(customer)

# Simulate processing of customers
print("\n--- Iniciando procesamiento ---")
start_time = time.time()
supermarket.start_time = start_time
for i in range(10):
    print(f"\nRonda de procesamiento #{i+1}")
    supermarket.process_customers()

# Output statistics
print("\n=== ESTADÍSTICAS FINALES ===")
average_wait_time = supermarket.average_wait_time()
throughput = supermarket.throughput()
print(f"\nResumen: Tiempo promedio de espera = {average_wait_time:.2f}s, Tasa de procesamiento = {throughput:.2f} clientes/segundo")