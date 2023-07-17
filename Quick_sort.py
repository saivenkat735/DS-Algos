def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and obtain the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort the subarrays
        quick_sort(arr, low, pivot_index - 1)  # Sort elements before the pivot
        quick_sort(arr, pivot_index + 1, high)  # Sort elements after the pivot

    return arr
arr = [5, 2, 9, 1, 7, 6, 4]
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
print(sorted_arr)  # Output: [1, 2, 4, 5, 6, 7, 9]
