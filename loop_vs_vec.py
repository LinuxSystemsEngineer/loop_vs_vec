# loop_vs_vec.py program
import numpy as np
import timeit
import statistics
from tqdm import tqdm
from tabulate import tabulate
from colorama import Fore, Style

# Function to time the for loop
def time_for_loop(large_vector):
    squared_roots_loop = np.zeros(len(large_vector))
    for i in range(len(large_vector)):
        squared_roots_loop[i] = np.sqrt(large_vector[i])

# Function to time the vectorized operation
def time_vectorized(large_vector):
    squared_roots_vector = np.sqrt(large_vector)

def performancetest():
    large_vector = np.random.rand(1_000_000)

    # Number of repetitions
    n_runs = 10

    print(Fore.CYAN + "\n[INFO] Running performance test with {} repetitions...".format(n_runs) + Style.RESET_ALL)

    # Measure execution times: vectorized test first, then for loop
    vector_times = timeit.repeat(lambda: time_vectorized(large_vector), repeat=n_runs, number=1)
    loop_times = timeit.repeat(lambda: time_for_loop(large_vector), repeat=n_runs, number=1)

    # Compute statistics
    vector_avg = statistics.mean(vector_times)
    loop_avg = statistics.mean(loop_times)
    vector_stddev = statistics.stdev(vector_times)
    loop_stddev = statistics.stdev(loop_times)

    # Compute speedup (how many times faster vectorized is compared to for loop)
    speedup = loop_avg / vector_avg

    # Display results with vectorized test first
    results_table = [
        ["Technique", "Avg Time (s)", "Standard Deviation (s)"],
        ["Vectorized", f"{vector_avg:.6f}", f"{vector_stddev:.6f}"],
        ["For Loop", f"{loop_avg:.6f}", f"{loop_stddev:.6f}"],
        ["Speedup", f"{speedup:.2f}x faster", "-"]
    ]
    
    print(Fore.YELLOW + "\n[RESULTS]" + Style.RESET_ALL)
    print(tabulate(results_table, headers="firstrow", tablefmt="fancy_grid"))

if __name__ == "__main__":
    performancetest()

