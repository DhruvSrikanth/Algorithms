'''

def min_heap_insert(A[1..n], key):
    heapsize(A) = heapsize(A) + 1
    i = heapsize[A]
    while i > 1 and A[Parent(i)] > key:
        A[i] = A[Parent(i)]
        i = Parent(i)
    A[i] = key


min_decrease_key(A, i (position that we are going to decrease the key), k (value we are going to decrease key to)) - Similar psuedocode to insert




'''
