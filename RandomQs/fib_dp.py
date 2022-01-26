# Compute the fibonacci number n.
# Follow up -  Do it in linear time.

# Time complexity O(2^n)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Time complexity O(n)
def fib_dp(n):
    dp = [-1 for i in range(n+2)]

    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+2):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

import time

n = 30

s = time.time()
res1 = fib(n)
e = time.time()
t_naive = round(e-s,4)

s = time.time()
res2 = fib_dp(n)
e = time.time()
t_dp = round(e-s,4)


print('Our result is {}.\nBoth approaches lead to the same answer - {}.\nThe naive approach take {} seconds.\nThe DP approach takes {} seconds.'.format(res1, res1 == res2, t_naive, t_dp))
