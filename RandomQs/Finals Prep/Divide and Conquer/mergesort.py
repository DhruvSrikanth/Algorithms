def merge(arr, m):
    left = arr[:m]
    right = arr[m:]
    n = len(left)
    m = len(right)
    sorted_array = [-1] * (m + n)
    i = j = k = 0
    while i < n and j < m:
        if left[i] < right[j]:
            sorted_array[k] = left[i]
            i += 1
        else:
            sorted_array[k] = right[j]
            j += 1
        k += 1
    
    while i < n:
        sorted_array[k] = left[i]
        i += 1
        k += 1
        
    while j < m:
        sorted_array[k] = right[j]
        j += 1
        k += 1
    
    arr = sorted_array[::]

def mergesort_helper(arr, s, e):
    if s < e:
        m = (s + e) // 2
        mergesort_helper(arr, s, m)
        mergesort_helper(arr, m + 1, e)
        merge(arr, m)

def mergesort(arr):
    s = 0
    e = len(arr) - 1
    return mergesort_helper(arr, s, e)


cases = [
    [1,2,3,4,5],
    [9,8,7,6,5],
    [4,8,1,9,2],
    [8,3,4,9,1]]

for case in cases:
    print("Original Array ->",case)
    mergesort(case)
    print("Sorted Array ->",case)
    print("x---x")
