# O (n log n) Time Complexity

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
  
        merge_sort(L)
        merge_sort(R)
  
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

cases = [
    [1,2,3,4,5],
    [9,8,7,6,5],
    [4,8,1,9,2],
    [8,3,4,9,1]]

for case in cases:
    print("Original Array ->",case)
    print("Sorted Array ->",merge_sort(case))
    print("x---x")
