def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of the sorted part to the right to make room for the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into the correct position in the sorted part
        arr[j + 1] = key

    return arr
arr = [5, 2, 9, 1, 7, 6, 4]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # Output: [1, 2, 4, 5, 6, 7, 9]
