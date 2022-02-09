# Time Complexity - O (n * log n)

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def heapify(arr, n, i, max_min):
    if max_min == 'max':
        def comp(ele,large):
            return ele > large
    elif max_min == 'min':
        def comp(ele, small):
            return ele < small
    else:
        raise Exception('Mode other than max and min provided to heapify...refer to heapsort source code.')
    extreme = i
    l = left(i)
    r = right(i)
    if l < n and comp(arr[l], arr[extreme]):
        extreme = l
    if r < n and comp(arr[r], arr[extreme]):
        extreme = r
    if extreme != i:
        arr[extreme], arr[i] = arr[i], arr[extreme]
        heapify(arr, n, extreme, max_min)

def heap_sort(arr, key):
    if key == 'asc':
        max_min = 'min'
    elif key == 'desc':
        max_min = 'max'
    else:
        raise Exception('Incorrect key provided...options are:\n1. asc - Ascending\n2. desc - Descending')
    
    n = len(arr)
    temp = arr[::]
    for i in range((n//2) - 1, -1, -1):
        heapify(temp, n, i, max_min)
    
    for i in range(n):
        arr[i]  = temp.pop(0)
        heapify(temp, len(temp), 0, max_min)

arr = [5,4,3,2,1,4,7,9,2]
key = 'asc'
print('After Sorting: \n{}'.format(arr))
heap_sort(arr, key)
print('Before Sorting: \n{}'.format(arr))
    


