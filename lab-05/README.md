# Queue Data Structure Laboratory Guide

## Table of Contents

- [Queue Data Structure Laboratory Guide](#queue-data-structure-laboratory-guide)
  - [Table of Contents](#table-of-contents)
  - [1. Understanding the Concept](#1-understanding-the-concept)
    - [Basic Operations:](#basic-operations)
    - [Time Complexity:](#time-complexity)
  - [2. Queue Implementations](#2-queue-implementations)
    - [2.1 Simple List-based Implementation](#21-simple-list-based-implementation)
    - [2.2 Circular Array Implementation](#22-circular-array-implementation)
    - [2.3 Linked List Implementation](#23-linked-list-implementation)
  - [3. Practical Applications](#3-practical-applications)
    - [3.1 Print Queue Simulation](#31-print-queue-simulation)
    - [3.2 Breadth-First Search (BFS)](#32-breadth-first-search-bfs)
  - [5. Practical Exercises](#5-practical-exercises)
    - [Exercise 1: Implement a Queue with Two Stacks](#exercise-1-implement-a-queue-with-two-stacks)
      - [**Solución:**](#solución)
    - [Exercise 2: Level Order Traversal of a Binary Tree](#exercise-2-level-order-traversal-of-a-binary-tree)
      - [**Solución:**](#solución-1)
    - [Exercise 3: Hot Potato Game Simulation](#exercise-3-hot-potato-game-simulation)
      - [**Solución:**](#solución-2)
    - [Exercise 4: Sliding Window Maximum](#exercise-4-sliding-window-maximum)
      - [**Solución:**](#solución-3)
    - [Exercise 5: Design a Supermarket Checkout System](#exercise-5-design-a-supermarket-checkout-system)
      - [**Solución:**](#solución-4)
  - [6. Implementation Comparison](#6-implementation-comparison)
  - [7. Next Steps](#7-next-steps)
  - [8. Conclusions](#8-conclusions)

---

## 1. Understanding the Concept

A queue is a linear data structure that follows the **First-In-First-Out (FIFO)** principle, which means:

- The first element added is the first one to be removed.
- New elements are added at the rear and removed from the front.

### Basic Operations:

- **Enqueue**: Add an element to the rear of the queue.
- **Dequeue**: Remove and return the element from the front.
- **Peek/Front**: View the front element without removing it.
- **isEmpty**: Check if the queue is empty.
- **size**: Get the number of elements in the queue.

### Time Complexity:
- **Enqueue**: O(1)
- **Dequeue**: O(1)
- **Peek**: O(1)
- **isEmpty**: O(1)
- **size**: O(1)

---

## 2. Queue Implementations

### 2.1 Simple List-based Implementation

The simplest way to implement a queue in Python using a list. However, this implementation has **O(n)** time complexity for dequeue operations, as it requires shifting elements.

```python
class SimpleQueue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return f"Queue: {self.items}"
```

### 2.2 Circular Array Implementation

A circular array allows both **enqueue** and **dequeue** operations to occur in **O(1)** time by using a fixed-size array and circular indexing.

```python
class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size_count = 0
    
    def is_empty(self):
        return self.size_count == 0
    
    def is_full(self):
        return self.size_count == self.capacity
    
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full!")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size_count -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.queue[self.front]
    
    def size(self):
        return self.size_count
```

### 2.3 Linked List Implementation

This implementation uses a linked list for dynamic queue size. Each element is a node, and each node points to the next.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_count = 0
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size_count -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.front.data
    
    def size(self):
        return self.size_count
    
    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        
        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next
        
        return f"Queue: [{', '.join(result)}]"
```

---

## 3. Practical Applications

### 3.1 Print Queue Simulation

A **printer queue** is a perfect example of a real-world queue, processing print jobs in the order they are received.

```python
class PrintJob:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

class Printer:
    def __init__(self, pages_per_minute):
        self.page_rate = pages_per_minute
        self.current_job = None
        self.time_remaining = 0
    
    def is_busy(self):
        return self.current_job is not None
    
    def start_next_job(self, job):
        self.current_job = job
        self.time_remaining = job.pages * 60 / self.page_rate
    
    def tick(self):
        if self.is_busy():
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_job = None
                return True
        return False
```

### 3.2 Breadth-First Search (BFS)

Queues are used in **BFS** to explore nodes level by level, such as in graph traversal.

```python
def breadth_first_search(graph, start_node):
    queue = LinkedQueue()
    visited = set()
    queue.enqueue(start_node)
    visited.add(start_node)
    
    result = []
    
    while not queue.is_empty():
        current = queue.dequeue()
        result.append(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
    
    return result
```

---

## 5. Practical Exercises

### Exercise 1: Implement a Queue with Two Stacks

Implement a queue using two stacks, with amortized O(1) time complexity for all operations.

#### **Solución:**

```python
class QueueWithTwoQueues:
    def __init__(self):
        self.queue_in = LinkedQueue()  # Cola para las operaciones de enqueue
        self.queue_out = LinkedQueue()  # Cola para las operaciones de dequeue

    def is_empty(self):
        return self.queue_in.is_empty() and self.queue_out.is_empty()

    def enqueue(self, item):
        self.queue_in.enqueue(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        
        if self.queue_out.is_empty():
            while not self.queue_in.is_empty():
                self.queue_out.enqueue(self.queue_in.dequeue())
        
        return self.queue_out.dequeue()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        
        if self.queue_out.is_empty():
            while not self.queue_in.is_empty():
                self.queue_out.enqueue(self.queue_in.dequeue())
        
        return self.queue_out.peek()

    def size(self):
        return self.queue_in.size() + self.queue_out.size()

# Prueba
queue = QueueWithTwoQueues()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # 1
print(queue.peek())     # 2
```

### Exercise 2: Level Order Traversal of a Binary Tree

Realiza el recorrido por niveles de un árbol binario utilizando una **cola (queue)**.

#### **Solución:**

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []
    
    queue = LinkedQueue()  # Usamos la implementación de cola ligada
    result = []
    
    queue.enqueue(root)
    
    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)
        
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    
    return result

# Crear un árbol binario
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(level_order_traversal(root))  # [1, 2, 3, 4, 5]
```

### Exercise 3: Hot Potato Game Simulation

Simula el juego de "Papas Calientes" usando una **cola (queue)**.

#### **Solución:**

```python
import random

class HotPotatoGame:
    def __init__(self, players, max_passes):
        self.players = LinkedQueue()
        for player in players:
            self.players.enqueue(player)
        self.max_passes = max_passes

    def play(self):
        while self.players.size() > 1:
            passes = random.randint(1, self.max_passes)
            for _ in range(passes):
                self.players.enqueue(self.players.dequeue())
            eliminated = self.players.dequeue()
            print(f"{eliminated} was eliminated!")
        
        return self.players.dequeue()

# Simulación del juego
players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
game = HotPotatoGame(players, 5)
winner = game.play()
print(f"The winner is {winner}")
```

### Exercise 4: Sliding Window Maximum

Encuentra el valor máximo en cada ventana deslizante de tamaño `k` en un arreglo usando una **cola (queue)**.

#### **Solución:**

```python
from collections import deque

class SlidingWindowMax:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        self.queue = LinkedQueue()  # Usamos la cola para almacenar índices
        self.result = []

    def calculate(self):
        for i in range(len(self.nums)):
            while not self.queue.is_empty() and self.nums[self.queue.peek()] <= self.nums[i]:
                self.queue.dequeue()
            self.queue.enqueue(i)
            
            # Eliminar los índices que están fuera de la ventana
            if self.queue.peek() <= i - self.k:
                self.queue.dequeue()
            
            # Agregar el máximo de la ventana actual al resultado
            if i >= self.k - 1:
                self.result.append(self.nums[self.queue.peek()])
        
        return self.result

# Ejemplo
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
sliding_window = SlidingWindowMax(nums, k)
print(sliding_window.calculate())  # [3, 3, 5, 5, 6, 7]
```

### Exercise 5: Design a Supermarket Checkout System

Simula un sistema de cajas de supermercado con múltiples líneas de caja usando **colas (queues)**.

#### **Solución:**

```python
class Customer:
    def __init__(self, customer_id, item_count):
        self.customer_id = customer_id
        self.item_count = item_count

class CheckoutLane:
    def __init__(self):
        self.queue = LinkedQueue()

    def add_customer(self, customer):
        self.queue.enqueue(customer)
    
    def process_customer(self):
        if not self.queue.is_empty():
            customer = self.queue.dequeue()
            print(f"Processed customer {customer.customer_id} with {customer.item_count} items")
            return customer
        return None

class Supermarket:
    def __init__(self, lanes):
        self.lanes = [CheckoutLane() for _ in range(lanes)]
    
    def assign_customer(self, customer):
        shortest_lane = min(self.lanes, key=lambda lane: lane.queue.size())
        shortest_lane.add_customer(customer)
    
    def process_all(self):
        for lane in self.lanes:
            while not lane.queue.is_empty():
                lane.process_customer()

# Crear el supermercado
supermarket = Supermarket(3)

# Crear clientes
customers = [Customer(1, 5), Customer(2, 3), Customer(3, 8), Customer(4, 2)]

# Asignar clientes a las cajas
for customer in customers:
    supermarket.assign_customer(customer)

# Procesar todos los clientes
supermarket.process_all()
```

---

## 6. Implementation Comparison

Compare different queue implementations based on time complexity, space complexity, and best use cases:

| Implementation        | Time Complexity       | Space Complexity    | Best Use Cases                      |
|-----------------------|-----------------------|---------------------|--------------------------------------|
| List-based Queue      | O(1) (Enqueue), O(n) (Dequeue) | O(n)                | Small queues, educational use       |
| Circular Array Queue  | O(1) (Enqueue/Dequeue) | O(n)                | Performance-critical systems        |
| Linked List Queue     | O(1) (Enqueue/Dequeue) | O(n)                | Dynamic size, frequent size changes |

---

## 7. Next Steps

After mastering queues, explore their variations such as **Priority Queues** and **Double-Ended Queues (Deque)**. You can also apply your knowledge to build systems like **job schedulers** or **message brokers**.

---

## 8. Conclusions

Queues are essential in computer science and real-world systems. By understanding their implementation and use cases, you can efficiently solve a wide range of problems.
```
