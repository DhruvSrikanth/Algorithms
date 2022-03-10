
def first_pos_num(f):
    def find_range(f):
        lower = higher = 0
        while True:
            if f(lower) < 0:
                break
            lower -= 1

        while True:
            if f(higher) > 0:
                break
            higher += 1
        return lower*2, higher*2

    start, end = find_range(f)

    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if f(mid) > 0 and f(mid - 1) < 0:
            ans = mid
            break
        elif f(mid) > 0:
            e = mid - 1
        else:
            s = mid + 1
    return ans



def f(x):
    return 3*x - 100

print(first_pos_num(f))
