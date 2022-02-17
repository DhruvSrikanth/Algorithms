def search(arr,x):
    if len(arr) == 0:
        return search.res
    if arr[0] == x:
        search.res.append(x)
    # print(search.res)
    return search(arr[1:], x)

arr = [1,2,3,4,5,5,6,7]
x = 5
f = search
f.res = []

res_ = f(arr,x)
print(res_)



