# Time Complexity - O (n log n)

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def min_heapify(arr, parent):
    smallest = parent
    l = left(parent)
    r = right(parent)
    if l < len(arr) and arr[l] < arr[smallest]:
        smallest = l
    if r < len(arr) and arr[r] < arr[smallest]:
        smallest = r
    if smallest != parent:
        arr[smallest], arr[parent] = arr[parent], arr[smallest]
        min_heapify(arr, smallest)

def build_min_heap(arr):
    for i in range((len(arr)//2) - 1, -1, -1):
        min_heapify(arr, i)

def print_heap(arr):
    for i in range(len(arr)):
        print(arr.pop(0))
        min_heapify(arr, 0)


arr = [12,11,13,5,6,7]
build_min_heap(arr)
print(arr)
print_heap(arr)

