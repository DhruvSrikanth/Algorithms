'''


Extarct min returns the root value and then deletes this value from the heap.

def heap_extract_min(A):
    min = A[1]
    A[1] = A[heapsize(A)]
    heapsize(A) = heapsize(A) - 1
    min_heapify(A, 1, heapsize(A))
    return min

def min_heapify(A, i, heapsize):
    if Left(i) <= heapsize[A] and A[Left(i)] < A[i]:
        smallest = Left(i)
    else:
        smallest = i


    if Right(i) <= heapsize[A] and A[Right(i)] < A[i]:
        smallest = Right(i)
    

    if smallest != i
        exchange A[i] and A[smallest]
        min_heapify(A, smallest, heapsize)

'''
