class Task:
    def __init__(self, name, total_time):
        self.name = name
        self.total_time = total_time
        self.remaining_time = total_time

def round_robin_scheduling(tasks, time_quantum):
    queue = tasks[:]
    total_waiting = total_turnaround = elapsed = completed = 0
    index = 0

    while completed < len(queue):
        task = queue[index]

        if task.remaining_time > 0:
            time_slice = min(task.remaining_time, time_quantum)
            task.remaining_time -= time_slice
            elapsed += time_slice

            if task.remaining_time == 0:
                turnaround = elapsed
                waiting = turnaround - task.total_time
                total_turnaround += turnaround
                total_waiting += waiting
                print(f"{task.name} completado. Espera: {waiting}, Retorno: {turnaround}")
                completed += 1

        index = (index + 1) % len(queue)

    n = len(tasks)
    print(f"\nPromedio espera: {total_waiting / n:.2f}")
    print(f"Promedio retorno: {total_turnaround / n:.2f}")

# Ejemplo de uso
tasks = [Task("T1", 10), Task("T2", 5), Task("T3", 8)]
round_robin_scheduling(tasks, time_quantum=4)
