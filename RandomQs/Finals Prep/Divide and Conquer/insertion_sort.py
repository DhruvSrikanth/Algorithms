def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

cases = [
    [1,2,3,4,5],
    [9,8,7,6,5],
    [4,8,1,9,2],
    [8,3,4,9,1]]

for case in cases:
    print("Original Array ->",case)
    insertion_sort(case)
    print("Sorted Array ->",case)
    print("x---x")
