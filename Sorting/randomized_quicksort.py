# Use random sampling to choose the pivot in order to almost always achieve a time complexity of quicksort close to the best case - O (n log n)

from partition import partition
import random

def randomized_partition(A,p,r):
    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]
    return partition(A,p,r)

def randomized_quicksort(A,p,r):
    if p < r:
        q = randomized_partition(A,p,r) # get the index of the boundary which splits array into two left and right sorted arrays
        randomized_quicksort(A,p,q-1) # elements to the left of the partition
        randomized_quicksort(A,q+1,r) # elements to the right of the partition
