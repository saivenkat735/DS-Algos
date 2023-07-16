def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
arr = [5, 2, 9, 1, 7, 6, 4]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # Output: [1, 2, 4, 5, 6, 7, 9]
