# Time Complexity - O(n log n)


def max_heapify(arr, p):
    largest = p
    l = 2*p + 1
    r = 2*p + 2
    if l < len(arr) and arr[l] > arr[largest]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != p:
        arr[largest], arr[p] = arr[p], arr[largest]
        max_heapify(arr, largest)

def build_max_heap(arr):
    for p in range((len(arr)//2) - 1, -1, -1):
        max_heapify(arr, p)

def print_heap(arr):
    for i in range(len(arr)):
        print(arr.pop(0))
        max_heapify(arr,0)

arr = [3,9,2,1,4,5]
build_max_heap(arr)
print(arr)
print_heap(arr)
