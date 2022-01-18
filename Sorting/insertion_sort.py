# O (n^2) Time Complexity
def ins_sort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i>=0 and arr[i]>key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr

cases = [
    [1,2,3,4,5],
    [9,8,7,6,5],
    [4,8,1,9,2],
    [8,3,4,9,1]]

for case in cases:
    print("Original Array ->",case)
    print("Sorted Array ->",ins_sort(case))
    print("x---x")
