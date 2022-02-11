# Time Complexity - O (log n) all the time

def binary_search_recursive(arr, x, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search_recursive(arr, x, start, mid - 1)
    else:
        return binary_search_recursive(arr, x, mid + 1, end)

def binary_search_iterative(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1

arr = [1,2,4,6,8,9]
x = 2
print(binary_search_recursive(arr, x, 0, len(arr) - 1))
print(binary_search_iterative(arr, x))


def binary_search_variants(arr, x):
    start = 0
    end = len(arr) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            end = mid - 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1

    return ans

arr = [1,2,2,3,4,5,6]
x = 2
print(binary_search_variants(arr, x))


def rotated_binary_search(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[start] <= arr[mid]:
            if arr[start] <= x and x <= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] <= arr[end]:
            if arr[mid] <= x <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            print("Problem in algorithm")

    return -1

arr = [4,5,6,1,2,3]
x = 2

print(rotated_binary_search(arr, x))
