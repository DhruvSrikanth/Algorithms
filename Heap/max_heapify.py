# Time Complexity - O (log n)

def get_left_child(i):
    return 2*i + 1

def get_right_child(i):
    return 2*i + 2

def max_heapify(arr, k):
    largest = k
    l = get_left_child(k)
    r = get_right_child(k)
    if l < len(arr) and arr[l] > arr[largest]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != k:
        arr[k], arr[largest] = arr[largest], arr[k]
        max_heapify(arr, largest)
