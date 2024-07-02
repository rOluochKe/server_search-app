import matplotlib.pyplot as plt

# Algorithm names
algorithms = ['Linear Search', 'Binary Search',
              'Regex Search', 'Grep Search', 'Mmap Search']

# Execution times
execution_times = [1.335e-05, 3.552e-05, 0.000537, 0.013053, 0.078020]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(algorithms, execution_times, color='skyblue')
plt.xlabel('Algorithms')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Different Search Algorithms')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
