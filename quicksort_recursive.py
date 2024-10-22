def quicksort_recursive(arr, low, high, comparisons=0, swaps=0):
    if low < high:
        pivot_index, comparisons, swaps = partition(arr, low, high, comparisons, swaps)
        comparisons, swaps = quicksort_recursive(arr, low, pivot_index - 1, comparisons, swaps)
        comparisons, swaps = quicksort_recursive(arr, pivot_index + 1, high, comparisons, swaps)
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
