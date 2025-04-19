class Task:
    def __init__(self, name, time_needed, priority):
        self.name = name
        self.remaining = time_needed
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0

    def __str__(self):
        return f"{self.name} (restante: {self.remaining})"


class TaskScheduler:
    def __init__(self, time_slice):
        self.queue = []
        self.time_slice = time_slice
        self.current_time = 0
        self.completed_tasks = []

    def add_task(self, name, time_needed, priority):
        self.queue.append(Task(name, time_needed, priority))

    def schedule(self):
        index = 0
        while self.queue:
            task = self.queue[index]

            # Ejecutar por un ciclo
            time_run = min(self.time_slice, task.remaining)
            task.remaining -= time_run
            self.current_time += time_run

            # Aumentar tiempo de espera en otras tareas
            for i, t in enumerate(self.queue):
                if i != index and t.remaining > 0:
                    t.waiting_time += time_run

            if task.remaining == 0:
                task.turnaround_time = self.current_time
                self.completed_tasks.append(task)
                self.queue.pop(index)
                if index >= len(self.queue):
                    index = 0
            else:
                index = (index + 1) % len(self.queue)

    def report(self):
        total_waiting = 0
        total_turnaround = 0
        print("Informe de tareas completadas:")
        for task in self.completed_tasks:
            print(f"{task.name}: espera={task.waiting_time}, retardo={task.turnaround_time}")
            total_waiting += task.waiting_time
            total_turnaround += task.turnaround_time

        n = len(self.completed_tasks)
        if n > 0:
            print(f"Promedio espera: {total_waiting / n:.2f}")
            print(f"Promedio retardo: {total_turnaround / n:.2f}")


# 🧪 Prueba
if __name__ == "__main__":
    scheduler = TaskScheduler(time_slice=2)
    scheduler.add_task("T1", 5, 1)
    scheduler.add_task("T2", 3, 2)
    scheduler.add_task("T3", 6, 1)
    scheduler.schedule()
    scheduler.report()
