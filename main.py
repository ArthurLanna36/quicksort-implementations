import time
import random
from quicksort_recursive import quicksort_recursive
from quicksort_recursive_cutoff import quicksort_recursive_cutoff
from quicksort_median_of_three import quicksort_median_of_three
from create_bar_graph import create_bar_graph

def generate_test_data(n, order="random"):
    if order == "random":
        return [random.randint(1, 10000) for _ in range(n)]
    elif order == "sorted":
        return list(range(1, n+1))
    elif order == "reverse":
        return list(range(n, 0, -1))

def run_quicksort_tests():
    numbers_array_length = 1000
    numbers_array = generate_test_data(numbers_array_length, order="random")

    print(f"\nArray length: {numbers_array_length}")

    # Recursive quicksort
    numbers_array_copy = numbers_array.copy()
    start_time = time.process_time()
    standard_quicksort_operations = quicksort_recursive(numbers_array_copy, 0, len(numbers_array_copy) - 1)
    end_time = time.process_time()
    print("\n--- Recursive Quicksort ---")
    print(f"CPU time spent to sort the array: {end_time - start_time}s, Comparisons: {standard_quicksort_operations[0]}, Swaps: {standard_quicksort_operations[1]}")

    # Recursive quicksort dividing the array in smaller parts when M is small enough
    M = 10  # M value can be adjusted
    numbers_array_copy = numbers_array.copy()
    start_time = time.process_time()
    cutoff_quicksort_operations = quicksort_recursive_cutoff(numbers_array_copy, 0, len(numbers_array_copy) - 1, M)
    end_time = time.process_time()
    print("\n--- Recursive Quicksort using the cutoff strategy ---")
    print(f"CPU time spent to sort the array: {end_time - start_time}s, Comparisons: {cutoff_quicksort_operations[0]}, Swaps: {cutoff_quicksort_operations[1]}")

    # Quicksort using median of three strategy
    numbers_array_copy = numbers_array.copy()
    start_time = time.process_time()
    median_of_three_quicksort_operations = quicksort_median_of_three(numbers_array_copy, 0, len(numbers_array_copy) - 1)
    end_time = time.process_time()
    print("\n--- Recursive Quicksort using the median of three strategy ---")
    print(f"CPU time spent to sort the array: {end_time - start_time}s, Comparisons: {median_of_three_quicksort_operations[0]}, Swaps: {median_of_three_quicksort_operations[1]}")

    total_operations = {
        'comparisonsTotal': [standard_quicksort_operations[0], cutoff_quicksort_operations[0], median_of_three_quicksort_operations[0]],
        'swapsTotal': [standard_quicksort_operations[1], cutoff_quicksort_operations[1], median_of_three_quicksort_operations[1]]
    }

    return total_operations

if __name__ == "__main__":
    totalOperations = run_quicksort_tests()

    # Creating a bar graph that shows the quantity of comparisons
    # executed by each of the quicksort algorithms
    create_bar_graph(
        totalOperations['comparisonsTotal'],
        'Total comparisons from each Quicksort algorithm',
        ['Quicksort', 'Cutoff Quicksort', 'Median of Three\nQuicksort']
    )