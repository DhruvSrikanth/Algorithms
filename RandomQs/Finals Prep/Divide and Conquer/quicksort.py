def partition(arr, s, e):
    pivot = arr[e]
    bound = s - 1
    for i in range(s, e):
        if arr[i] <= pivot:
            bound += 1
            arr[i], arr[bound] = arr[bound], arr[i]
    bound += 1
    arr[e], arr[bound] = arr[bound], arr[e]
    return bound


def randomized_partition(arr, s, e):
    import random
    pivot = random.randint(s, e)
    arr[e], arr[pivot] = arr[pivot], arr[e]
    return partition(arr, s, e)

def quicksort_helper(arr, s, e):
    if s < e:
        partition_id = randomized_partition(arr, s, e)
        quicksort_helper(arr, s, partition_id - 1)
        quicksort_helper(arr, partition_id + 1, e)
        
        
def quicksort(arr):
    s = 0
    e = len(arr) - 1
    quicksort_helper(arr, s, e)


cases = [
    [1,2,3,4,5],
    [9,8,7,6,5],
    [4,8,1,9,2],
    [8,3,4,9,1]]

for case in cases:
    print("Original Array ->",case)
    quicksort(case)
    print("Sorted Array ->",case)
    print("x---x")
    
