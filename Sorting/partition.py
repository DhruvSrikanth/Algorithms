# Time complexity - O (n)

def partition(A,p,r):
    x = A[r] # last element in our array will be the pivot element
    i = p - 1 # boundary marker is i, A[:i] <= x and A[i+1:] > x
    for j in range(p, r): # range has a non inclusive upper bound so we are doing this until the element right before the pivot
        if A[j] <= x:
            i += 1 # increase the boundary by 1
            A[i], A[j] = A[j], A[i] # move A[j] before the boundary and A[i] after the boundary
    A[i+1], A[r] = A[r], A[i+1] # finally exchange the pivot with the element right after the boundary to maintain the invariant
    return i + 1 # boundary now shifted up by 1 due to exchange of the pivot in the previous line

