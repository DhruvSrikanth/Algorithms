def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [12, 11, 13, 5, 6]
print('Array before sorting - {}'.format(arr))
insertion_sort(arr, len(arr))
print('Array after sorting - {}'.format(arr))
