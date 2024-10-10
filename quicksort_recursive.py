# Partition function
def partition(array, low, high):
    # Choose the pivot
    pivot = array[high]

    # Index of smaller element and indicates
    # the right position of pivot found so far
    i = low - 1

    # Traverse array[low...high] and move all smaller
    # elements to the left side. Elements from low to
    # i are smaller after every iteration
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            swap(array, i, j)

    # Move pivot after smaller elements and
    # return its position
    swap(array, i + 1, high)
    return i + 1

# Swap function
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# The QuickSort function implementation
def quicksort_recursive(array, low, high):
    if low < high:
        # pivot_index is the partition return index of pivot
        pivot_index = partition(array, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quicksort_recursive(array, low, pivot_index - 1)
        quicksort_recursive(array, pivot_index + 1, high)