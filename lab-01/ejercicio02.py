from timeit import default_timer as timer
import matplotlib.pyplot as plt

# List of n values
n_values = [10**2, 10**3, 10**4, 10**5, 10**6]
times = []

# Measure processing time for each value of n
for n in n_values:
    start = timer()
    
    # Simple loop
    for i in range(n):
        pass  # Empty loop to measure only time for iteration

    end = timer()
    proc_time = end - start
    times.append(proc_time)
    print(f"Processing time for n = {n}: {proc_time} seconds")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, marker='o', linestyle='-', color='b')
plt.title('Processing Time vs Size of n')
plt.xlabel('Size of n')
plt.ylabel('Processing Time (seconds)')
plt.xscale('log')  # Logarithmic scale for n
plt.yscale('log')  # Logarithmic scale for time
plt.grid(True)

# Show plot
plt.show()
