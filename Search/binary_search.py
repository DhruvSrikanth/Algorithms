def binary_search(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search(array, element, start, mid-1)
    else:
        return binary_search(array, element, mid+1, end)

x = 3
arr = [1,2,3]
res = arr.index(x)

print(binary_search(arr, x, 0, len(arr) - 1) == res)
