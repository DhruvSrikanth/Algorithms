'''

Given an arrayA[1..n] ofncharactersR(red) andW(white) in any order,writepseudocodefor  an  algorithm  to  rearrange  the  array  elements  sothat all thered’s come before all thewhite’s.  Your algorithm should bein-place, meaning you cannot allocate another array to temporarily hold the items, and run in O(n) time. 

Example:

Input:[R W W R W W R R W R W R]

Output:[R R R R R R W W W W W W]

'''

def partition(A,start,end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] == pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[end] = A[end], A[i+1]
    return A

inp = ['R','W','W','R','W','W','R','R','W','R','W','R']
print(partition(inp,0,len(inp)-1))
