def quicksort_recursive_cutoff(arr, low, high, M, comparisons=0, swaps=0):
    if high - low + 1 <= M:
        comparisons, swaps = insertion_sort(arr, low, high, comparisons, swaps)
    elif low < high:
        pivot_index, comparisons, swaps = partition(arr, low, high, comparisons, swaps)
        comparisons, swaps = quicksort_recursive_cutoff(arr, low, pivot_index - 1, M, comparisons, swaps)
        comparisons, swaps = quicksort_recursive_cutoff(arr, pivot_index + 1, high, M, comparisons, swaps)
    return comparisons, swaps

def insertion_sort(arr, low, high, comparisons, swaps):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key
    return comparisons, swaps

def partition(arr, low, high, comparisons, swaps):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    return i + 1, comparisons, swaps
