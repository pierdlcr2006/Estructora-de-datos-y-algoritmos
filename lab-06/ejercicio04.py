class Task:
    def __init__(self, name, total_time):
        self.name = name
        self.total_time = total_time  # Tiempo total requerido por el proceso
        self.remaining_time = total_time  # Tiempo restante para el proceso

def round_robin_scheduling(tasks, time_quantum):
    queue = tasks[:]  # Hacemos una copia de la lista de tareas
    total_waiting_time = 0
    total_turnaround_time = 0
    time_elapsed = 0
    completed_tasks = 0  # Para llevar el control de los procesos completados

    front = 0  # Índice que indica el primer proceso (frente de la cola)

    while completed_tasks < len(tasks):  # Mientras no todos los procesos estén completos
        task = queue[front]  # Tomamos el primer proceso de la cola

        if task.remaining_time > time_quantum:
            # Si el proceso necesita más tiempo que el quantum, reduce el tiempo restante
            task.remaining_time -= time_quantum
            time_elapsed += time_quantum
        else:
            # Si el proceso termina en este ciclo
            time_elapsed += task.remaining_time
            turnaround_time = time_elapsed
            waiting_time = turnaround_time - task.total_time
            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time
            print(f"Proceso {task.name} completado. Tiempo de espera: {waiting_time}, Tiempo de retorno: {turnaround_time}")
            completed_tasks += 1  # Incrementamos los procesos completados
            task.remaining_time = 0  # El proceso ha terminado

        # Avanzamos cíclicamente al siguiente proceso (simulando una cola circular)
        front = (front + 1) % len(queue)

    # Calcular los promedios de tiempo de espera y tiempo de retorno
    num_tasks = len(tasks)
    avg_waiting_time = total_waiting_time / num_tasks
    avg_turnaround_time = total_turnaround_time / num_tasks

    print(f"\nTiempo promedio de espera: {avg_waiting_time}")
    print(f"Tiempo promedio de retorno: {avg_turnaround_time}")

# Ejemplo de uso
tasks = [
    Task("T1", 10),  # Proceso con tiempo total de 10 unidades
    Task("T2", 5),   # Proceso con tiempo total de 5 unidades
    Task("T3", 8)    # Proceso con tiempo total de 8 unidades
]

round_robin_scheduling(tasks, time_quantum=4)