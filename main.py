import random
from quicksort_recursive import quicksort_recursive

if __name__ == "__main__":
    # Length of the array
    arrayLength = 1000
    arrayHigherLimit = 1000

    # Generates a random array with the length above
    # The values of these numbers must follow this rule: 0 <= numberGenerated <= arrayHigherLimit
    numbersArray = [random.randint(0, arrayHigherLimit) for _ in range(arrayLength)]
    auxiliaryNumbersArray = []

    for number in numbersArray:
        auxiliaryNumbersArray.append(number)

    quicksort_recursive(numbersArray, 0, len(numbersArray) - 1)

    print("Original array")
    for number in auxiliaryNumbersArray:
        print(number, end=" ")

    print("\nSorted array")
    for number in numbersArray:
        print(number, end=" ")
