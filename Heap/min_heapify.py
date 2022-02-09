# Time Complexity - O (log n)

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def min_heapify(arr, parent_node):
    smallest = parent_node
    l = left(parent_node)
    r = right(parent_node)
    if l < len(arr) and arr[l] < arr[smallest]:
        smallest = l
    if r < len(arr) and arr[r] < arr[smallest]:
        smallest = r
    if smallest != parent_node:
        arr[smallest], arr[parent_node] = arr[parent_node], arr[smallest]
        min_heapify(arr, smallest)

