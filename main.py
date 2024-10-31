import random
import time
from quicksort_recursive import quicksort_recursive
from quicksort_tests import find_best_m

if __name__ == "__main__":
    arrayLength = 80000
    arrayHigherLimit = 1000

    # Generates a random array with the length above
    # The values of these numbers must follow this rule: 0 <= numberGenerated <= arrayHigherLimit
    numbersArray = [random.randint(0, arrayHigherLimit) for _ in range(arrayLength)]
    auxiliaryNumbersArray = []

    for number in numbersArray:
        auxiliaryNumbersArray.append(number)

    # Starts the CPU time counting before the execution of the recursive Quicksort algorithm
    startTime = time.process_time()

    quicksort_recursive(numbersArray, 0, len(numbersArray) - 1)

    # Gets the full executing time to sort the array
    sortingTime = time.process_time() - startTime

    print("\nCPU execution time to sort the array:", sortingTime)

    find_best_m(1000)