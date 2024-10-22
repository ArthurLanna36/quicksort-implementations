def quicksort_median_of_three(arr, low, high, comparisons=0, swaps=0):
    if low < high:
        pivot = median_of_three(arr, low, high)
        pivot_index, comparisons, swaps = partition(arr, low, high, comparisons, swaps)
        comparisons, swaps = quicksort_median_of_three(arr, low, pivot_index - 1, comparisons, swaps)
        comparisons, swaps = quicksort_median_of_three(arr, pivot_index + 1, high, comparisons, swaps)
    return comparisons, swaps

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid]  # Coloca o pivô no final
    return arr[high]

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
