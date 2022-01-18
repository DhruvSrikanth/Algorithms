# Time complexity - O(TODO)
# This is an in-place sort like insertion sort

from partition import partition
def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r) # get the index of the boundary which splits array into two left and right sorted arrays
        quicksort(A,p,q-1) # elements to the left of the partition
        quicksort(A,q+1,r) # elements to the right of the partition
