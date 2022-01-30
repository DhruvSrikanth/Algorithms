def binary_search_r(arr, x, start, end):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search_r(arr, x, mid + 1, end)
        else:
            return binary_search_r(arr, x, start, mid - 1)
    else:
        return -1

def binary_search_i(arr, x, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search_r(arr, x, 0, len(arr) - 1)
# print(result)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [12, 11, 13, 5, 6]
# print('Array before sorting - {}'.format(arr))
# insertion_sort(arr)
# print('Array after sorting - {}'.format(arr))

def binary_insertion_sort(arr):

    def binary_search(arr, x, start, end): 
        if start > end:
            return start
        else:
            if arr[start] > x:
                return start
            else:
                return start + 1

        if start < end:
            mid = (start + end) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binary_search(arr, x, start, mid - 1)
            else:
                return binary_search(arr, x, mid + 1, end)
            

    for i in range(1,len(arr)):
        x_idx = binary_search(arr[:i], arr[i], 0, i - 1)
        print(arr)
        arr.insert(x_idx, arr[i])
        del arr[i + 1]
        print(arr)
        print('------x-----')

arr = [12, 11, 13, 5, 6]
print('Array before sorting - {}'.format(arr))
binary_insertion_sort(arr)
print('Array after sorting - {}'.format(arr))
