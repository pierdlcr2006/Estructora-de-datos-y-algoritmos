from collections import deque

def task_scheduler(tasks, time_quantum):
    queue = deque(tasks)
    result = []

    while queue:
        task = queue.popleft()
        result.append(f"Executing {task}")
        if task != 'done':
            queue.append('done')  # Add a task back to the queue if it's not finished

    return result

# Example
tasks = ['Task 1', 'Task 2', 'Task 3']
time_quantum = 2  # Simulated by the order
print(task_scheduler(tasks, time_quantum))