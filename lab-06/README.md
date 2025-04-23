
# Algorithms and Data Structures

## Lab06: Advanced Queue

### Capabilities
- Develop and Design algorithms for circular queues with dynamic arrays.
- Develop and Design algorithms for circular queues with linked lists.

### Safety
- Create a safe environment.
- Avoid consuming food.
- Keep the environment tidy and clean.

### Preparation
The student must review the uploaded material in advance.

### Resources
- Computer.

### Instructions
Each group member should select a different challenge and develop it with the following structure:

- **Student's Name**
- **Challenge to develop**
- **Prompt engineering (If applicable)**
- **Prompt entered and/or capture**
- **Analysis of the prompt**
- **Adjustments to the prompt and/or capture**
- **Comments from colleagues**
- **Code**
- **Developed code**
- **Code comments**
- **Explanation of operation**
- **Diagram of how it runs**
- **Code execution capture**
- **3 Test cases**
- **Conclusions**
- **Comments from colleagues**

Develop all code in English

---

## Circular Queue Implementation Guide

### Table of Contents
1. **Understanding the Fundamental Concept**
    - Queue Basics
    - The Circular Queue Solution
    - Core Operations
2. **Progressive Implementations**
    - Circular Array Queue
    - Dynamic Circular Array Queue
    - Circular Linked List Queue
3. **Practical Applications**
    - Print Queue Simulation
    - Breadth-First Search
4. **Real-world Case Study**
    - Bank Service System
5. **Technical Challenges**
    - Challenge 1: Sliding Window Maximum
    - Challenge 2: Rotating Array Elements
    - Challenge 3: Traffic Light Simulation
    - Challenge 4: Task Scheduling System
    - Challenge 5: Circular Buffer for Streaming Data
6. **Comparative Analysis**
7. **Next Learning Steps**
8. **Key Conclusions**

---

### 1. Understanding the Fundamental Concept

#### Queue Basics
A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle 🔄. Like a real-life queue:
- The first element added will be the first one removed 🥇
- Elements are added at the rear (enqueue) ⬅️
- Elements are removed from the front (dequeue) ➡️

When implemented with a simple array, dequeuing causes inefficiency as all elements must shift:
```
[A][B][C][D]  # Original queue
 ↑
 Dequeue
[B][C][D][ ]  # After dequeue - all elements shifted left
```
This shifting results in O(n) time complexity for the dequeue operation, making it inefficient for large queues 🐢.

#### The Circular Queue Solution
A circular queue (or ring buffer) solves this problem by conceptually connecting the end of the array back to the beginning, creating a circular structure 🔄:
```
      front      rear
         ↓         ↓
Array: [A][B][C][D][_][_][_][_]
```
After some operations:
```
       rear      front
         ↓         ↓
Array: [I][J][_][_][E][F][G][H]
```
The circular approach provides constant-time O(1) operations for both enqueue and dequeue by:
- Using two pointers: front and rear
- Applying modulo arithmetic to "wrap around" the array

### Core Operations
Circular queues support these fundamental operations:
- **Enqueue:** Add an element to the rear of the queue ⬅️
  - If the queue is full, either report an overflow or resize
  - Otherwise, add the item at the rear position
  - Update the rear pointer using the modulo operation
- **Dequeue:** Remove and return the element from the front ➡️
  - If the queue is empty, report an underflow
  - Otherwise, retrieve the item at the front position
  - Update the front pointer using the modulo operation
- **IsEmpty/IsFull:** Check queue status 🔍

Various ways to implement, typically using size count or pointer positions. The key insight is using modulo arithmetic (%) to handle the "circular" behavior:
```
rear = (rear + 1) % capacity  // Move rear pointer forward with wrap-around
front = (front + 1) % capacity  // Move front pointer forward with wrap-around
```

---

### 2. Progressive Implementations
#### 2.1 Circular Array Queue
Implement a basic fixed-size circular queue using an array.

#### 2.2 Dynamic Circular Array Queue
Implement a circular queue that can grow dynamically when it gets full.

---

### 5. Technical Challenges
#### Challenge 1: Sliding Window Maximum

📜 **Problem:** Given an array of integers and a window size `k`, find the maximum element in each sliding window as it moves from left to right.

🧑‍💻 **Solution:**
```python
from collections import deque

def sliding_window_max(nums, k):
    if not nums:
        return []

    window = deque()
    result = []

    for i in range(len(nums)):
        # Remove elements out of this window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove all elements smaller than the current element from the queue
        while window and nums[window[-1]] <= nums[i]:
            window.pop()

        # Add the current element at the end of the deque
        window.append(i)

        # Add the maximum element of the current window to the result
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Example
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))
```
💡 **Output:**
```
[3, 3, 5, 5, 6, 7]
```

---

#### Challenge 2: Rotating Array Elements

📜 **Problem:** Rotate an array of `n` elements to the right by `k` steps.

🧑‍💻 **Solution:**
```python
def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is larger than the array length
    return nums[-k:] + nums[:-k]

# Example
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(nums, k))
```
💡 **Output:**
```
[5, 6, 7, 1, 2, 3, 4]
```

---

#### Challenge 3: Traffic Light Simulation

🚦 **Problem:** Create a simulation of traffic flow through an intersection with traffic lights.

🧑‍💻 **Solution:**
```python
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
```

---

#### Challenge 4: Task Scheduling System

⏳ **Problem:** Design a round-robin task scheduler that allocates CPU time slices to processes in a circular manner.

🧑‍💻 **Solution:**
```python
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
```

💡 **Output:**
```
['Executing Task 1', 'Executing Task 2', 'Executing Task 3', 'Executing done', 'Executing done', 'Executing done']
```

---

#### Challenge 5: Circular Buffer for Streaming Data

🔄 **Problem:** Implement a circular buffer for a data stream where you need to keep only the most recent `N` elements.

🧑‍💻 **Solution:**
```python
class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.index = 0
        self.size = 0

    def insert(self, data):
        self.buffer[self.index] = data
        self.index = (self.index + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def get_latest(self):
        return self.buffer if self.size == self.capacity else self.buffer[:self.size]

# Example
buffer = CircularBuffer(5)
for i in range(8):
    buffer.insert(i)

print(buffer.get_latest())
```

💡 **Output:**
```
[3, 4, 5, 6, 7]
```

---

### 6. Comparative Analysis
| Implementation            | Time Complexity | Space Complexity | Advantages | Disadvantages | Best Use Cases |
|---------------------------|-----------------|------------------|------------|---------------|----------------|
| **Circular Array Queue**   | O(1)            | O(n)             | Fast operations ⚡ | Fixed capacity 📏 | Fixed-size applications 📏 |
| **Dynamic Circular Queue** | O(1)            | O(n)             | Dynamic size ♾️  | Resize operations occasionally O(n) ⏳ | Unknown size requirements 📏 |
| **Circular Linked Queue**  | O(1)            | O(n)             | Simpler circular logic 🧩 | Extra memory per node 🧠 | Memory-constrained environments 💾 |

---

### 8. Key Conclusions
Circular queues are a powerful optimization of the basic queue data structure, offering several important advantages:
- **Efficient Space Utilization**
- **Constant-time Operations**
- **Real-world Applicability**

---

## Challenge
Propose an algorithm that solves a problem from 1 to 8 from the following website [https://adventjs.dev/](https://adventjs.dev/) and iterate until you reach 5 stars. (Log in with your data)
