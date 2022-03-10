def sqrt(x):
    s = 1
    e = x // 2
    ans = -1
    while s <= e:
        m = (s + e) // 2
        if m*m == x:
            ans = m
            break
        elif m*m > x:
            e = m - 1
        else:
            s = m + 1
            ans = m
    return ans

x = 16
print(sqrt(x))
