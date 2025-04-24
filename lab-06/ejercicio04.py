from collections import deque

def round_robin_scheduler(tasks, quantum):
    queue = deque(tasks)
    while queue:
        task = queue.popleft()
        print(f"Ejecutando tarea: {task}")
        # Si la tarea necesita más tiempo, vuelve a la cola
        if task != "Tarea final":
            queue.append(task)
        time.sleep(1)  # Simula el tiempo de ejecución de cada tarea

    print("Todas las tareas han sido completadas.")

# Ejemplo de uso
tasks = ["Tarea 1", "Tarea 2", "Tarea 3", "Tarea final"]
quantum = 2
round_robin_scheduler(tasks, quantum)
