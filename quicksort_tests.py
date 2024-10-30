import matplotlib.pyplot as plt
import pandas as pd
import random
import math
import time

from quicksort_recursive import quicksort_recursive
from quicksort_recursive_cutoff import quicksort_recursive_cutoff
from quicksort_median_of_three import quicksort_median_of_three

def generate_test_data(n, order="random"):
    if order == "random":
        return [random.randint(1, 1000) for _ in range(n)]
    elif order == "sorted":
        return list(range(1, n, +1))
    elif order == "reverse":
        return list(range(n, 0, -1))

def time_standard_quicksort(array):
    # Recursive quicksort
    start_time = time.process_time()
    operations = quicksort_recursive(array, 0, len(array) - 1)
    cpu_time = time.process_time() - start_time
    return (cpu_time, operations)

def time_cutoff_quicksort(array, M):
    start_time = time.process_time()
    operations = quicksort_recursive_cutoff(array, 0, len(array) - 1, M)
    cpu_time = time.process_time() - start_time
    return (cpu_time, operations)

def time_median_quicksort(array):
    start_time = time.process_time()
    operations = quicksort_median_of_three(array, 0, len(array) - 1)
    cpu_time = time.process_time() - start_time
    return (cpu_time, operations)

#--------------------Test Routines--------------------

# Test all
def run_quicksort_tests(array_length):
    array = generate_test_data(array_length, order="random")

    # Recursive quicksort
    standard_quicksort_cpu_time, standard_quicksort_operations = time_standard_quicksort(array.copy())

    # Recursive quicksort dividing the array in smaller parts when M is small enough
    M = 10  # M value can be adjusted
    cutoff_quicksort_cpu_time, cutoff_quicksort_operations = time_cutoff_quicksort(array.copy(), M)

    # Quicksort using median of three strategy
    median_cutoff_quicksort_cpu_time, median_of_three_quicksort_operations = time_median_quicksort(array.copy())

    total_operations = {
        'comparisonsTotal': [
            standard_quicksort_operations[0],
            cutoff_quicksort_operations[0],
            median_of_three_quicksort_operations[0]
        ],
        'swapsTotal': [
            standard_quicksort_operations[1],
            cutoff_quicksort_operations[1],
            median_of_three_quicksort_operations[1]
        ]
    }

    cpu_times = [
        standard_quicksort_cpu_time,
        cutoff_quicksort_cpu_time,
        median_cutoff_quicksort_cpu_time
    ]

    return total_operations, cpu_times

# Find the best m
# array_length -> Array Length
def find_best_m(array_length, start_m, end_m, fit):
    if start_m < 1:
        start_m = 1
    if end_m > array_length:
        end_m = array_length
    m = start_m

    m_run_times = 10
    best_cpu_time = math.inf
    average_list = []
    m_list = []

    while m < end_m:
        m_cpu_time = 0

        for _ in range(m_run_times):
            array = generate_test_data(array_length, order="random")
            cpu_time, operations = time_cutoff_quicksort(array, m)
            m_cpu_time = m_cpu_time + cpu_time

        average_m_cpu_time = m_cpu_time / m_run_times

        if average_m_cpu_time < best_cpu_time:
            best_cpu_time = average_m_cpu_time

        print("Best= ", best_cpu_time, ", Average= ", average_m_cpu_time, ", M= ", m)

        average_list.append(average_m_cpu_time)
        m_list.append(m)

        m = m + fit

    df = pd.DataFrame({
        'M': m_list,
        'Cpu_time': average_list
    })

    plt.figure(figsize=(10, 6))
    plt.plot(df['M'], df['Cpu_time'], marker='o')
    plt.title('M vs Cpu_time')
    plt.xlabel('M')
    plt.ylabel('Cpu_time')
    plt.grid(True)
    plt.xticks(m_list, rotation=45)
    plt.show()

    return m
